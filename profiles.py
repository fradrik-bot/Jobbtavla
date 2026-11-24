"""Profiler för jobbtavlorna. build.py bygger en sida per profil."""

DANIEL_CV = 'Daniel Jansson. Säljare som kan tekniken bakom produkten. Tränade svenska landslaget i Short Track.\nFlyttar med sin fru till Bonäshamn utanför Järpen vid årsskiftet, för att komma närmare familjen (sonen har jobbat som skidlärare i Åre sedan 2016). Huset är köpt, flytten beslutad och långsiktig. Öppen för många slags jobb: försäljning, butik (gärna bygghandel eller sport), teknisk kundkontakt, körning (t.ex. taxi), kan tänka sig att utbilda sig till elektriker. Vill pendla högst cirka 50 km. Tillgänglig för intervju redan nu, på plats eller digitalt. B-körkort, egen bil, bilkörning har varit en stor del av arbetslivet. Svenska (modersmål), engelska (mycket goda kunskaper).\nERFARENHET:\n- Säljare, AMAX Konsult AB (2024–): säljer dokumentation för långsiktig fastighetsförvaltning – arkitektritningar, underlag för brandskydd/SBA, ytor m.m. Har träffat 92 kunder, varav 85 kommuner eller kommunala bostadsbolag, 6 privata fastighetsbolag och 1 industri. Har sålt in skanning av ritningsunderlag till en stor kommun i Skåne, drönarskanning och uppritning av skötselytor till en annan kommun och senast skanning av 400 A1-ritningar. Offertarbete, flera beslutsfattare, långa relationer.\n- Ägare och säljare, Cimco Nordic AB (2014–2023): byggde och drev försäljningen av Cimcos verktyg till elgrossister i Norden. Försäljningen växte från cirka 1,5 miljoner euro (2015) till 2,2 miljoner euro (2022). Sista helåret: Danmark 47 %, Norge 36 %, Finland 7 %, Island 6 %, Sverige 4 %. Kunder bland annat Lemvigh-Müller och Solar (Danmark), SLO (Finland), Johan Rönning (Island); i Norge och Sverige via partnern Melbyes säljorganisation. Besökte grossisterna 2–4 gånger per år och deltog på mässor. Största framgång: danska Lemvigh-Müller växte från cirka 300 000 till 520 000 euro per år, och han lade själv in de nya artiklarna i kundens system, på danska.\n- Säljare, Cimtools Scandinavia AB (2005–2014): teknisk försäljning till samma grossistkunder, som han sedan tog med till Cimco Nordic. Nästan 20 år i samma bransch.\n- Säljare, ESD Center AB (2001–2005): sålde skydd mot statisk elektricitet (förpackningar, skydd för utrustning, personligt skydd) till elektroniktillverkare, stora som små.\n- Elektronikmontör, SattControl, ABB Automation, Flextronics (1994–2001): monterade elektronik i apparatskåp m.m. för kunder från lokala tillverkare till Alfa Laval. På Flextronics ansvarig för underhållsgruppen och för inköp av skyddsutrustning och produktionsinredning.\n- Butiksbiträde Shell Lysekil, verkstadsarbetare Gökens Svets och Mekaniska (1988–1994).\nLEDARSKAP OCH IDROTT: Elittränare, svenska landslaget i Short Track (2014–2025), till största delen ideellt, 15–20 timmar per vecka under 2014–2019. Tränade 3–5 åkare; tog en OS-plats till Pyeongchang 2018 (åkaren blev inte uttagen av SOK). Bästa resultat 9:e plats på 1 500 m vid EM 2018. Har varit förbundskapten vid världscuper, EM, JVM och VM. Har gått ISU:s tränarutbildningar i skridsko- och materialteknik. Landslagsåkare 1989–1998. Alpin tävlingsåkare från 10 till 17 års ålder.\nHANTVERK: har byggt ett tiotal formgjutna skridskor (gipsavgjutning av foten, läder och kolfiber). Har lagt marksten i alla former och konstruerat och byggt trädäck, både mot berg och hus och direkt på mark.\nKOMPETENS: teknisk försäljning, B2B, nykunds- och relationsförsäljning, offertarbete, förhandling, export, affärsutveckling, Norden, offentlig sektor, eget företagande, Microsoft 365.\nUTBILDNING: Fyraårig teknisk linje, maskin (1988). Värnplikt televapensoldat S1.'

DANIEL = {
    "file": "index.html", "data": "jobs.json",
    "TITLE": "Daniels jobbtavla", "H1": "Daniels jobbtavla",
    "INTRO": "Lediga jobb runt nya hemmet i Bonäshamn, Järpen och Åre från Platsbanken, LinkedIn, SkiStar och fler jobbsajter, sorterade efter hur väl de passar din bakgrund.",
    "quick": [(20, "20 km"), (30, "30 km"), (50, "50 km"), (75, "75 km"), (100, "100 km"), (150, "150 km")], "quickLabel": "Max avstånd",
    "sal": [30, 35, 40, 45, 50],
    "manual": """    <div class="card">
      <h2>Källor som inte går att läsa automatiskt</h2>
      <p>Indeed, Monster, Jooble och Careerjet stänger ute automatisk hämtning. Deras annonser i Jämtland är till största delen kopior av Platsbanken och LinkedIn, som redan finns med. Facebook-grupper kräver inloggning.</p>
      <div class="row">
        <a class="btn btn-line" href="https://se.indeed.com/jobs?q=&l=J%C3%A4rpen&radius=50" target="_blank" rel="noopener">Indeed runt Järpen</a>
        <a class="btn btn-line" href="https://www.google.com/search?q=facebook+grupp+jobb+i+%C3%85re" target="_blank" rel="noopener">Facebook-grupper för jobb i Åre</a>
      </div>
    </div>""",
    "sheet": """      <div class="sheet" id="sheet">
        <div class="lt-head">
          <div>
            <div class="lt-name">Daniel<br>Jansson</div>
            <div class="lt-tag">Säljare som kan tekniken bakom produkten. <span>Tränar svenska landslaget på fritiden.</span></div>
            <div class="lt-meta" id="ltContact"></div>
          </div>
          <svg class="lt-track" viewBox="0 0 200 100" aria-hidden="true"><rect x="4" y="10" width="192" height="80" rx="40" fill="none" stroke="#9DBFDB" stroke-width="1.5"/><rect x="26" y="26" width="148" height="48" rx="24" fill="none" stroke="#C9DCEB" stroke-width="1.2"/><path d="M110 90 Q170 90 190 60" fill="none" stroke="#1767A6" stroke-width="2.4"/><circle cx="110" cy="90" r="3.5" fill="#1767A6"/></svg>
        </div>
        <div class="lt-banner" id="ltBanner"></div>
        <div class="lt-row">
          <div class="lt-label">Personligt<br>brev</div>
          <div class="lt-body" id="ltBody" contenteditable="true" spellcheck="true"></div>
        </div>
        <div class="lt-foot"><span>Daniel Jansson · Personligt brev</span><span id="ltDate"></span></div>
      </div>""",
    "nameFields": False, "levelSel": False,
    "P": {
        "quickUnit": "km", "defaultMax": 50, "maxVersion": 1,
        "key": "daniel-jobbtavla-v2", "title": "Daniels jobbtavla", "name": "Daniel Jansson", "cv": DANIEL_CV, "dataFile": "jobs.json",
        "homes": {"hem": {"name": "hemma i Bonäshamn", "short": "Hemma", "lat": 63.412945, "lon": 13.366713},
                  "jarpen": {"name": "Järpen centrum", "short": "Järpen", "lat": 63.348, "lon": 13.470},
                  "are": {"name": "Åre", "short": "Åre", "lat": 63.399, "lon": 13.081}},
        "homeOpts": [["hem", "Hemma, Bonäshamn 665"], ["jarpen", "Järpen centrum"], ["are", "Åre"]],
        "defaultHome": "jarpen", "homeLabel": "Hemma, Bonäshamn 665",
        "kw": [["teknisk försäljning", 2], ["säljare", 2], ["försäljning", 2], ["b2b", 2], ["affärsutveckling", 2], ["kundansvarig", 2], ["key account", 2], ["account manager", 2], ["distriktsansvarig", 2], ["grossist", 2], ["elgrossist", 2], ["export", 1], ["kundrelationer", 1], ["offert", 1], ["förhandling", 1], ["nykund", 1], ["innesälj", 1], ["fältsälj", 1], ["butikssäljare", 2], ["byggvaruhus", 2], ["bygghandel", 2], ["järnhandel", 1], ["byggmaterial", 1], ["bauhaus", 1], ["byggmax", 1], ["xl-bygg", 1], ["beijer", 1], ["woody", 1], ["sportbutik", 1], ["skidor", 1], ["uthyrning", 1], ["elektriker", 2], ["elinstallation", 1], ["lärling", 1], ["installation", 1], ["elektronik", 1], ["industri", 1], ["underhåll", 1], ["inköp", 1], ["taxi", 2], ["chaufför", 1], ["förare", 1], ["fastighet", 1], ["ritning", 1], ["dokumentation", 1], ["offentlig sektor", 1], ["tränare", 1], ["ledarskap", 1]],
        "avoid": ["legitimerad", "sjuksköterska", "läkare", "förskollärare", "lärare", "socionom", "psykolog", "undersköterska", "kock", "tandläkare"],
        "regionLabel": "Jämtland/Västernorrland",
        "hideArea": {"label": "Dölj Östersund", "rx": "östersund|ostersund|frösön", "name": "Östersund"},
        "live": ["position=63.412945,13.366713&position.radius=160"], "liveComplete": True, "liveMax": 2000,
        "letterCity": "Järpen",
        "contactLine": ["$phone", "$email", "Svedala → Järpen", "B-körkort, egen bil", "svenska, engelska"],
        "fallback": 5,
                "evidence": [
            {
                        "k": [
                                    "försäljning",
                                    "säljare",
                                    "sälj",
                                    "b2b",
                                    "teknisk",
                                    "account",
                                    "kundansvar",
                                    "affär"
                        ],
                        "have": "24 år inom teknisk B2B-försäljning",
                        "say": "Jag har arbetat med teknisk B2B-försäljning i 24 år, och min styrka är att jag förstår tekniken bakom det jag säljer."
            },
            {
                        "k": [
                                    "affärsutveckl",
                                    "ansvar",
                                    "resultat",
                                    "driv",
                                    "självständig",
                                    "eget",
                                    "norden",
                                    "export",
                                    "distrikt",
                                    "grossist",
                                    "återförsälj",
                                    "tillväxt",
                                    "mål"
                        ],
                        "have": "Cimco Nordic: försäljningen växte från ca 1,5 till 2,2 miljoner euro per år (2015–2022)",
                        "say": "I nio år drev jag eget bolag, Cimco Nordic, och sålde verktyg till elgrossister i hela Norden. Under min tid växte försäljningen från cirka 1,5 till 2,2 miljoner euro per år."
            },
            {
                        "k": [
                                    "kundansvar",
                                    "key account",
                                    "nyckelkund",
                                    "grossist",
                                    "relation",
                                    "återförsälj",
                                    "artikel",
                                    "system",
                                    "kundvård"
                        ],
                        "have": "Ökade försäljningen till danska Lemvigh-Müller från ca 300 000 till 520 000 euro per år",
                        "say": "Min största kund, danska Lemvigh-Müller, växte från cirka 300 000 till 520 000 euro per år – och de nya artiklarna lade jag själv in i deras system, på danska."
            },
            {
                        "k": [
                                    "offentlig",
                                    "kommun",
                                    "fastighet",
                                    "förvaltning",
                                    "offert",
                                    "upphandl",
                                    "ritning",
                                    "dokumentation",
                                    "bostad",
                                    "beslutsfattare"
                        ],
                        "have": "AMAX: 92 kundmöten, varav 85 kommuner och kommunala bostadsbolag",
                        "say": "På AMAX har jag träffat 92 kunder, varav 85 kommuner och kommunala bostadsbolag, och sålt in allt från skanning av ritningsunderlag till drönarskanning av skötselytor."
            },
            {
                        "k": [
                                    "elektronik",
                                    "industri",
                                    "produktion",
                                    "installation",
                                    "montör",
                                    "tekni",
                                    "underhåll",
                                    "inköp",
                                    "elektriker",
                                    "verkstad",
                                    "maskin",
                                    "el-"
                        ],
                        "have": "Sju år i elektronikproduktion (SattControl, ABB, Flextronics), ansvarig för underhåll och inköp",
                        "say": "Min grund är sju år i elektronikproduktion hos SattControl, ABB och Flextronics, där jag också ansvarade för underhållsgruppen och inköp av utrustning."
            },
            {
                        "k": [
                                    "ledar",
                                    "team",
                                    "coach",
                                    "planering",
                                    "struktur",
                                    "engag",
                                    "utveckla",
                                    "idrott",
                                    "sport",
                                    "tränare",
                                    "instruktör"
                        ],
                        "have": "Elittränare för landslaget i Short Track, förbundskapten vid VM och EM, OS-plats 2018",
                        "say": "I elva år var jag elittränare för svenska landslaget i Short Track, med uppdrag som förbundskapten vid världscuper, EM och VM – och vi tog en OS-plats till Pyeongchang 2018."
            },
            {
                        "k": [
                                    "bygg",
                                    "byggvaru",
                                    "bygghandel",
                                    "trä",
                                    "mark",
                                    "sten",
                                    "verktyg",
                                    "material",
                                    "hantverk",
                                    "snickeri",
                                    "trädgård",
                                    "järn",
                                    "butik"
                        ],
                        "have": "Har själv lagt marksten, byggt trädäck och byggt formgjutna skridskor",
                        "say": "Jag har själv lagt marksten och byggt trädäck, och jag har byggt ett tiotal formgjutna skridskor i läder och kolfiber – så jag kan ge kunderna råd utifrån egen erfarenhet."
            },
            {
                        "k": [
                                    "körkort",
                                    "resa",
                                    "bil",
                                    "fält",
                                    "taxi",
                                    "chaufför",
                                    "förare",
                                    "kör",
                                    "region",
                                    "distrikt",
                                    "besök"
                        ],
                        "have": "B-körkort och egen bil, van att köra mycket i tjänsten",
                        "say": "Bilkörning har varit en stor del av mitt arbetsliv som säljare, och jag har B-körkort och egen bil."
            },
            {
                        "k": [
                                    "skid",
                                    "alpin",
                                    "åre",
                                    "fjäll",
                                    "turism",
                                    "uthyrning",
                                    "liftar",
                                    "besökare",
                                    "gäst"
                        ],
                        "have": "Före detta alpin tävlingsåkare, känner Åre sedan 2016",
                        "say": "Jag tävlade i alpint som ung, och sedan vår son blev skidlärare i Åre 2016 har vi varit där flera gånger om året, både vinter och sommar."
            }
        ],
        "draft": {
            "p1": "Hej!\n\nJag har läst er annons ”{title}” och söker gärna tjänsten. Vid årsskiftet flyttar min fru och jag till Bonäshamn utanför Järpen för att komma närmare familjen – huset är köpt och flytten är långsiktig.",
            "p4": "Jag berättar gärna mer om hur jag kan bidra hos {employer}. Jag är tillgänglig för intervju redan nu, på plats eller digitalt.\n\nVänliga hälsningar\n{name}",
        },
        "travelText": "Arbetsplatsen ligger cirka {km} km ({min}) med bil från hans nya hem i Bonäshamn.",
        "promptHead": "Skriv ett personligt brev på svenska för {name} till tjänsten nedan.",
        "promptRules": [
            "Högst 280 ord, så att det får plats på en A4 tillsammans med rubrik.",
            "Rak, varm och konkret ton. Inga klichéer som \"jag är en lagspelare\".",
            "Koppla annonsens viktigaste krav till konkreta erfarenheter i CV:t.",
            "Nämn kort att han och frun flyttar till Bonäshamn utanför Järpen vid årsskiftet för att komma närmare familjen, och att huset redan är köpt. {travel}",
            "Daniel är öppen för många slags jobb: försäljning, butik (gärna bygghandel eller sport), teknik och körning. Välj vinkel efter just den här tjänsten och lyft de erfarenheter som passar bäst – för en butikstjänst hantverket och kundmötet, för en säljtjänst siffrorna från Cimco och Lemvigh-Müller.",
            "Använd gärna konkreta siffror från CV:t där de passar, men inte fler än två eller tre.",
            "Hitta inte på siffror, resultat eller erfarenheter som inte står i CV:t.",
            "Svara bara med brevtexten: börja med en hälsning och avsluta med \"Vänliga hälsningar\" och \"{name}\". Ingen rubrik, inga kontaktuppgifter, inga kommentarer.",
        ],
    },
}

PROFIL2 = {
    "file": "data.html", "data": "jobs_data.json",
    "TITLE": "Jobbtavlan", "H1": "Jobbtavlan",
    "INTRO": "Lediga jobb inom data, analys och AI i Stockholm och på distans, från Platsbanken, LinkedIn och fler jobbsajter, sorterade efter hur väl de passar din profil.",
    "quick": [(20, "20 min"), (40, "40 min"), (60, "1 timme"), (90, "1,5 timme")],
    "sal": [50, 60, 70, 80, 90, 100],
    "manual": """    <div class="card">
      <h2>Källor som inte går att läsa automatiskt</h2>
      <p>Indeed och flera andra jobbsajter stänger ute automatisk hämtning. Seniora roller tillsätts dessutom ofta via rekryteringsfirmor och nätverk.</p>
      <div class="row">
        <a class="btn btn-line" href="https://se.indeed.com/jobs?q=head+of+data&l=Stockholm" target="_blank" rel="noopener">Indeed: Head of Data, Stockholm</a>
        <a class="btn btn-line" href="https://www.linkedin.com/jobs/search/?keywords=head%20of%20data&location=Stockholm" target="_blank" rel="noopener">LinkedIn: Head of Data</a>
      </div>
    </div>""",
    "sheet": """      <div class="sheet v2" id="sheet">
        <div class="v2-head">
          <div>
            <div class="lt-name" id="ltName">Ditt<br>Namn</div>
            <div class="v2-love" id="ltTag"></div>
            <div class="v2-role" id="ltRole"></div>
          </div>
          <div class="v2-contact" id="ltContact"></div>
        </div>
        <div class="v2-rule"></div>
        <div class="lt-row">
          <div class="lt-label"><span class="v2-num">01</span><br>Ansökan</div>
          <div>
            <div class="lt-banner" id="ltBanner"></div>
            <div class="lt-body" id="ltBody" contenteditable="true" spellcheck="true"></div>
          </div>
        </div>
        <div class="lt-foot"><span><span id="ltFootName"></span> · Personligt brev</span><span id="ltDate"></span></div>
      </div>""",
    "nameFields": True, "levelSel": True,
    "P": {
        "key": "jobbtavla-data-v1", "title": "Jobbtavlan", "name": "", "dataFile": "jobs_data.json",
        "homes": {"hem": {"name": "hemma", "short": "Hemma", "lat": 59.2760, "lon": 17.8900},
                  "city": {"name": "T-Centralen", "short": "T-Centralen", "lat": 59.3311, "lon": 18.0597}},
        "homeOpts": [["hem", "Hemma"], ["city", "T-Centralen"]],
        "defaultHome": "city", "homeLabel": "Hemma",
        "kw": [["head of data", 2], ["chief data", 2], ["data & analytics", 2], ["data and analytics", 2], ["analytics", 2], ["business intelligence", 2], ["data platform", 2], ["dataplattform", 2], ["data governance", 2], ["datastyrning", 2], ["microsoft fabric", 2], ["lakehouse", 2], ["semantic", 1], ["power bi", 1], ["fabric", 1], ["databricks", 1], ["azure", 1], ["dataarkitekt", 2], ["data architect", 2], ["arkitektur", 1], ["head of", 1], ["chef", 1], ["ledarskap", 1], ["leadership", 1], ["generative ai", 1], ["ai agent", 1], ["copilot", 1], ["machine learning", 1], ["gdpr", 1], ["försäkring", 1], ["insurance", 1], ["strategi", 1], ["strategy", 1], ["chief strategy officer", 2], ["head of strategy", 2], ["strategichef", 2], ["strategy director", 2], ["chief data officer", 2], ["chief digital officer", 2], ["director", 1], ["direktör", 1], ["ledningsgrupp", 2], ["executive management", 2], ["c-level", 1], ["transformation", 1]],
        "avoid": ["junior", "praktik", "internship", "trainee", "student", "sjuksköterska", "lärare", "säljare"],
        "regionLabel": "Stockholm",
        "domainRx": r"strateg|transformation|data|analy|\bbi\b|business intelligence|\bai\b|insight|arkitekt|architect|digital|\bit\b|it-|\bcdo\b|\bcto\b|\bcio\b|\bcso\b|teknik|technology|plattform|platform",
        "seniorRx": r"head|chef|chief|director|direktör|lead|ledare|manager|ansvarig|arkitekt|architect|principal|\bc[a-z]{1,2}o\b|\bvp\b|ledning",
        "capNonSenior": 55, "levels": True, "execBoost": 8,
        "hideArea": None,
        "live": ["region=CifL_Rzy_Mku&q=data", "region=CifL_Rzy_Mku&q=AI", "region=CifL_Rzy_Mku&q=analytics", "region=CifL_Rzy_Mku&q=business%20intelligence"],
        "liveComplete": False, "liveMax": 800,
        "letterCity": "",
        "contactLine": ["$city", "$phone", "$email"], "contactSep": "<br>",
        "fallback": 5,
        "evidence": [],  # personliga exempel läses in lokalt från profilfilen
        "draft": {
            "p1": "Hej!\n\nNär jag läste att {employer} söker {title_l} kände jag igen uppdraget direkt.",
            "p4": "Jag berättar gärna mer om hur jag kan bidra hos {employer}.\n\nMed vänlig hälsning\n{name}",
        },
        "travelText": "",
        "promptHead": "Skriv ett personligt brev för {name} till tjänsten nedan.",
        "promptRules": [
            "Skriv på samma språk som annonsen, svenska eller engelska.",
            "Högst 350 ord, så att det ryms på en A4.",
            "Börja med en kort rubrikrad som fångar kärnan i rollen, till exempel \"En kund, en order, en produkt – samma sak i hela bolaget\". Därefter brevtexten.",
            "Personlig, konkret och självsäker ton utan klichéer. Koppla annonsens viktigaste krav till konkreta exempel i CV:t.",
            "Var ärlig om eventuella luckor mot annonsen och visa hur de överbryggs.",
            "Hitta inte på siffror, resultat eller erfarenheter som inte står i CV:t.",
            "Avsluta med \"Med vänlig hälsning\" och namnet. Inga kontaktuppgifter, inga kommentarer.",
        ],
    },
}
PROFILES = [DANIEL, PROFIL2]
