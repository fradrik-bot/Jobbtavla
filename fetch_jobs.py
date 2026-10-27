#!/usr/bin/env python3
"""Hämtar lediga jobb runt Järpen/Åre från flera källor och skriver jobs.json.

Källor:
  - Platsbanken (Arbetsförmedlingens JobSearch API)
  - JobTech Links (annonser från andra jobbsajter, t.ex. offentligajobb.se)
  - LinkedIn (publika jobbsök-sidan, kräver ingen inloggning)
  - SkiStar (karriärsidan via Jobylon)
Körs dagligen av GitHub Actions (se .github/workflows/update.yml) eller för hand: python fetch_jobs.py
"""
import json, re, math, time, html, codecs, sys, datetime, urllib.request, urllib.parse

HOME = (63.412945, 13.366713)    # Hemma, Bonäshamn 665, Järpen
RADIUS_KM = 160                  # hur långt ut vi hämtar
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"

PLACES = {  # ort -> (lat, lon)
 "åre":(63.399,13.081),"järpen":(63.348,13.470),"duved":(63.392,12.928),"undersåker":(63.342,13.355),
 "storlien":(63.318,12.100),"mörsil":(63.306,13.668),"hallen":(63.183,14.077),"kall":(63.474,13.244),
 "mattmar":(63.318,13.766),"vålådalen":(63.150,12.950),"bydalen":(63.100,13.780),"åre björnen":(63.385,13.120),
 "östersund":(63.176,14.636),"ostersund":(63.176,14.636),"frösön":(63.190,14.560),"krokom":(63.327,14.456),
 "brunflo":(63.076,14.830),"nälden":(63.340,14.270),"föllinge":(63.670,14.610),"trångsviken":(63.336,14.010),
 "ås":(63.250,14.560),"lit":(63.310,14.830),"bräcke":(62.750,15.420),"sveg":(62.034,14.360),
 "funäsdalen":(62.540,12.550),"vemdalen":(62.440,13.860),"hede":(62.420,13.500),"strömsund":(63.850,15.550),
 "hammerdal":(63.590,15.350),"hammarstrand":(63.100,16.350),"svenstavik":(62.770,14.430),"tännäs":(62.450,12.660),
 "lofsdalen":(62.120,13.270),"gäddede":(64.500,14.150),"ragunda":(63.100,16.380),"berg":(62.770,14.430),
 "härjedalen":(62.034,14.360),"jämtland":(63.176,14.636),"jämtlands län":(63.176,14.636),
}
_geo_cache = {}

def get(url, accept="application/json", tries=3):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": accept})
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.read().decode("utf-8", "replace")
        except Exception as e:
            if i == tries - 1: raise
            time.sleep(2 + i * 3)

def km(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    h = math.sin((la2-la1)/2)**2 + math.cos(la1)*math.cos(la2)*math.sin((lo2-lo1)/2)**2
    return 6371 * 2 * math.asin(math.sqrt(h))

def geocode(place):
    if not place: return None
    p = place.lower().split(",")[0].strip()
    p = re.sub(r"\s+(kommun|county|län)$", "", p)
    if p in PLACES: return PLACES[p]
    if p in _geo_cache: return _geo_cache[p]
    try:  # OpenStreetMap Nominatim, sparsamt och cachat
        q = urllib.parse.urlencode({"q": p + ", Sverige", "format": "json", "limit": 1})
        d = json.loads(get("https://nominatim.openstreetmap.org/search?" + q))
        time.sleep(1.1)
        _geo_cache[p] = (float(d[0]["lat"]), float(d[0]["lon"])) if d else None
    except Exception:
        _geo_cache[p] = None
    return _geo_cache[p]

def add_drive(jobs):
    """Bilväg och körtid hemifrån via OSRM, en gång per unik plats."""
    pts = sorted({(round(j["lat"], 4), round(j["lon"], 4)) for j in jobs if j.get("lat") is not None and not j.get("remote")})
    res = {}
    for i in range(0, len(pts), 90):
        chunk = pts[i:i+90]
        coords = ";".join([f"{HOME[1]},{HOME[0]}"] + [f"{p[1]},{p[0]}" for p in chunk])
        try:
            d = json.loads(get(f"https://router.project-osrm.org/table/v1/driving/{coords}?sources=0&annotations=distance,duration"))
            for p, dist, dur in zip(chunk, d["distances"][0][1:], d["durations"][0][1:]):
                if dist is not None: res[p] = (round(dist / 1000), round(dur / 60))
        except Exception as e:
            print("OSRM fel:", e, file=sys.stderr)
        time.sleep(1)
    for j in jobs:
        if j.get("lat") is None or j.get("remote"): continue
        r = res.get((round(j["lat"], 4), round(j["lon"], 4)))
        if r: j["drive_km"], j["drive_min"] = r

def type_short(l):
    l = l or ""
    if re.search("Vanlig|Tillsvidare|Fast", l): return "Fast"
    if re.search("Säsong|Sommar", l): return "Säsong"
    if "Behov" in l: return "Behov"
    if "Vikariat" in l: return "Vikariat"
    if "Tidsbeg" in l: return "Visstid"
    return l

# ---------- Platsbanken ----------
def platsbanken():
    out = []
    def page(base, maxn):
        off, total = 0, 1
        while off < min(total, maxn):
            d = json.loads(get(f"{base}&limit=100&offset={off}"))
            total = d["total"]["value"]
            for h in d["hits"]: out.append(h)
            off += 100
    page(f"https://jobsearch.api.jobtechdev.se/search?position={HOME[0]},{HOME[1]}&position.radius={RADIUS_KM}", 2000)
    n_local = len(out)
    page("https://jobsearch.api.jobtechdev.se/search?remote=true", 300)
    jobs = []
    for i, h in enumerate(out):
        wa = h.get("workplace_address") or {}
        c = wa.get("coordinates") or [None, None]
        pos = (c[1], c[0]) if c and c[0] else geocode(wa.get("city") or wa.get("municipality"))
        city = wa.get("city") or ""
        if city.lower() not in PLACES: city = wa.get("municipality") or city
        if city.lower() == "ostersund": city = "Östersund"
        jobs.append({
            "id": "P" + h["id"], "title": h.get("headline", ""), "employer": (h.get("employer") or {}).get("name", ""),
            "place": city.capitalize() if city.isupper() else city, "muni": wa.get("municipality") or "",
            "lat": pos[0] if pos else None, "lon": pos[1] if pos else None,
            "occ": (h.get("occupation_group") or {}).get("label", ""),
            "type": type_short((h.get("employment_type") or {}).get("label")),
            "hours": (h.get("working_hours_type") or {}).get("label") or "",
            "deadline": (h.get("application_deadline") or "")[:10] or None,
            "published": (h.get("publication_date") or "")[:10] or None,
            "desc": ((h.get("description") or {}).get("text") or "")[:3500 if i < n_local else 1200],
            "remote": i >= n_local or bool(h.get("remote_work")),
            "sources": [{"name": "Platsbanken", "url": "https://arbetsformedlingen.se/platsbanken/annonser/" + h["id"]}],
        })
    return jobs

# ---------- JobTech Links ----------
def jobtech_links():
    jobs, off, total = [], 0, 1
    while off < min(total, 2000):
        d = json.loads(get(f"https://links.api.jobtechdev.se/joblinks?region=65Ms_7r1_RTG&limit=100&offset={off}"))
        total = d["total"]["value"]
        for h in d["hits"]:
            for s in h.get("source_links") or []:
                if s.get("label") == "arbetsformedlingen.se": continue
                wa = (h.get("workplace_addresses") or [{}])[0]
                pos = geocode(wa.get("municipality"))
                jobs.append({
                    "id": "L" + h["id"], "title": h.get("headline", ""), "employer": (h.get("employer") or {}).get("name", ""),
                    "place": wa.get("municipality") or "", "muni": wa.get("municipality") or "",
                    "lat": pos[0] if pos else None, "lon": pos[1] if pos else None,
                    "occ": (h.get("occupation_group") or {}).get("label", ""), "type": "", "hours": "",
                    "deadline": None, "published": (h.get("publication_date") or "")[:10] or None,
                    "desc": h.get("brief") or "", "remote": False,
                    "sources": [{"name": s.get("label"), "url": s.get("url")}],
                })
        off += 100
    return jobs

# ---------- LinkedIn ----------
def linkedin():
    jobs, seen = [], set()
    for loc in ["Åre, Jämtland County, Sweden", "Östersund, Jämtland County, Sweden", "Krokom, Jämtland County, Sweden"]:
        for start in range(0, 500, 25):
            url = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?" + urllib.parse.urlencode(
                {"location": loc, "distance": 25, "start": start})
            try: s = get(url, accept="text/html")
            except Exception: break
            cards = re.findall(r"<li>(.*?)</li>", s, re.S)
            if not cards: break
            for b in cards:
                t = re.search(r'base-search-card__title">\s*(.*?)\s*<', b, re.S)
                c = re.search(r'base-search-card__subtitle">.*?>\s*(.*?)\s*<', b, re.S)
                l = re.search(r'job-search-card__location">\s*(.*?)\s*<', b, re.S)
                u = re.search(r'href="(https://[a-z]+\.linkedin\.com/jobs/view/[^"?]+)', b)
                d = re.search(r'datetime="([\d-]+)"', b)
                if not (t and u): continue
                jid = re.search(r"-(\d+)$", u.group(1))
                key = jid.group(1) if jid else u.group(1)
                if key in seen: continue
                seen.add(key)
                place = html.unescape(l.group(1)).split(",")[0] if l else ""
                pos = geocode(place)
                jobs.append({
                    "id": "I" + key, "title": html.unescape(t.group(1)), "employer": html.unescape(c.group(1)) if c else "",
                    "place": place, "muni": place, "lat": pos[0] if pos else None, "lon": pos[1] if pos else None,
                    "occ": "", "type": "", "hours": "", "deadline": None, "published": d.group(1) if d else None,
                    "desc": "", "remote": False, "sources": [{"name": "LinkedIn", "url": u.group(1)}],
                })
            time.sleep(1.5)
    return jobs

# ---------- SkiStar (Jobylon) ----------
def skistar():
    s = get("https://cdn.jobylon.com/jobs/companies/2244/embed/v2/?page_size=200", accept="text/html")
    blk = s[s.find("JBL.embed_v2['jobs']"):]
    jobs = []
    dec = lambda x: codecs.decode(x, "unicode_escape").encode("latin1").decode("utf8", "ignore")
    for j in re.split(r"\n\s*\{\n\s*id: '", blk)[1:]:
        g = lambda k: (re.search(k + r":\s*'(.*?)',", j) or [None, ""])[1]
        places = [p for p in ["Åre", "Vemdalen", "Sälen", "Stockholm", "Trysil", "Hemsedal"] if f"'{p}'" in j]
        place = next((p for p in places if p in ("Åre", "Vemdalen")), None)
        if not place: continue
        pos = geocode(place)
        typ = "Säsong" if "Säsong" in j else ("Fast" if "Tillsvidare" in j or "Fast" in j else "")
        jobs.append({
            "id": "S" + j[:j.find("'")], "title": dec(g("title")), "employer": "SkiStar",
            "place": place, "muni": place, "lat": pos[0], "lon": pos[1], "occ": "", "type": typ, "hours": "",
            "deadline": sv_date(dec(g("to_date"))), "published": sv_date(dec(g("published_date"))),
            "desc": dec(g("summary")), "remote": False,
            "sources": [{"name": "SkiStar", "url": "https://emp.jobylon.com" + g("url")}],
        })
    return jobs

SV_MONTHS = {m: i+1 for i, m in enumerate(["januari","februari","mars","april","maj","juni","juli","augusti","september","oktober","november","december"])}
def sv_date(s):
    m = re.match(r"(\d{1,2}) ([a-zåäö]+) (\d{4})", (s or "").strip().lower())
    if not m or m.group(2) not in SV_MONTHS: return None
    return f"{m.group(3)}-{SV_MONTHS[m.group(2)]:02d}-{int(m.group(1)):02d}"

def norm(s):
    s = (s or "").lower()
    s = re.sub(r"\b(ab|aktiebolag|sverige|sweden|ekonomisk förening)\b", "", s)
    return re.sub(r"[^a-zåäö0-9]", "", s)

def main():
    all_jobs, report = [], {}
    for name, fn in [("Platsbanken", platsbanken), ("JobTech Links", jobtech_links), ("LinkedIn", linkedin), ("SkiStar", skistar)]:
        try:
            js = fn(); all_jobs += js; report[name] = len(js)
        except Exception as e:
            report[name] = "fel: " + str(e)[:80]
        print(name, report[name], file=sys.stderr)
    merged = {}
    for j in all_jobs:  # slå ihop samma jobb från flera källor
        k = norm(j["title"])[:60] + "|" + norm(j["employer"])[:6]
        if k in merged:
            m = merged[k]
            for s in j["sources"]:
                if s["name"] not in [x["name"] for x in m["sources"]]: m["sources"].append(s)
            for f in ("desc", "deadline", "type", "occ", "lat", "lon"):
                if not m.get(f) and j.get(f): m[f] = j[f]
        else:
            merged[k] = j
    # hämta annonstext för jobb som bara finns på LinkedIn
    for j in merged.values():
        if j["desc"] or [x["name"] for x in j["sources"]] != ["LinkedIn"]: continue
        if j["lat"] is not None and km(HOME, (j["lat"], j["lon"])) > RADIUS_KM: continue
        try:
            p = get("https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/" + j["id"][1:], accept="text/html")
            m = re.search(r'show-more-less-html__markup[^>]*>(.*?)</div>', p, re.S)
            if m:
                t = re.sub(r"<br\s*/?>|</p>|</li>", "\n", m.group(1))
                j["desc"] = html.unescape(re.sub("<[^>]+>", "", t)).strip()[:3500]
            time.sleep(1.2)
        except Exception:
            pass
    jobs = []
    for j in merged.values():
        if j["lat"] is not None:
            j["km"] = round(km(HOME, (j["lat"], j["lon"])))
            if j["km"] > RADIUS_KM and not j["remote"]: continue
        else:
            j["km"] = None
        jobs.append(j)
    add_drive(jobs)
    out = {"generated": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
           "home": {"name": "Hemma i Bonäshamn", "lat": HOME[0], "lon": HOME[1]}, "sources": report, "jobs": jobs}
    with open("jobs.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False)
    print(f"{len(jobs)} jobb skrivna till jobs.json", file=sys.stderr)

if __name__ == "__main__":
    main()
