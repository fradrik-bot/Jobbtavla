"""Bygger en sida per profil i profiles.py från template.html och jobbdata."""
import json, os
from profiles import PROFILES

tpl = open("template.html", encoding="utf-8").read()
for pr in PROFILES:
    if not os.path.exists(pr["data"]):
        print("hoppar över", pr["file"], "- saknar", pr["data"]); continue
    data = json.load(open(pr["data"], encoding="utf-8"))
    P = pr["P"]
    quick = "".join(f'<button data-min="{m}">{l}</button>' for m, l in pr["quick"]) + '<button data-min="9999">Alla</button>'
    sal = '<button data-sal="0">Alla</button>' + "".join(f'<button data-sal="{k*1000}">{k} tkr</button>' for k in pr["sal"])
    opts = "".join(f'<option value="{v}">{l}</option>' for v, l in P["homeOpts"])
    js = lambda o: json.dumps(o, ensure_ascii=False).replace("</", "<\\/")
    rep = {
        "__TITLE__": pr["TITLE"], "__H1__": pr["H1"], "__INTRO__": pr["INTRO"], "__HOME_OPTS__": opts,
        "__QUICK__": quick, "__SALBTNS__": sal, "__SHEET__": pr["sheet"], "__MANUAL__": pr["manual"],
        "__HIDEAREA_LABEL__": (P["hideArea"] or {}).get("label", ""),
        "__HIDEAREA_STYLE__": "" if P["hideArea"] else 'hidden',
        "__NAMEFIELD_STYLE__": "" if pr["nameFields"] else 'hidden',
        "__QUICK_LABEL__": pr.get("quickLabel", "Max restid"),
        "__LEVEL_STYLE__": "" if pr.get("levelSel") else 'hidden',
        "__PROFILE__": js(P), "__SNAPSHOT__": js(data),
    }
    out = tpl
    for k, v in rep.items(): out = out.replace(k, v)
    open(pr["file"], "w", encoding="utf-8").write(out)
    print("byggde", pr["file"])
