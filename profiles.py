"""Profiler för jobbtavlorna. build.py bygger en sida per profil."""

DANIEL_CV = 'DANIEL JANSSON\nSäljare med teknisk bakgrund\n\nJag flyttar till Bonäshamn utanför Järpen vid årsskiftet. Min fru och jag har köpt hus där för att komma närmare familjen. Jag kan komma på intervju redan nu.\n\nPROFIL\nJag har jobbat som säljare av tekniska produkter i 24 år. Nio av dem drev jag eget bolag och sålde till elgrossister i hela Norden. Innan jag blev säljare stod jag sju år i elektronikproduktion, och det har jag haft nytta av varje gång en kund frågat hur något fungerar. I Åre kan jag tänka mig det mesta: sälja, stå i butik, jobba med teknik eller köra.\n\nARBETSLIVSERFARENHET\n2024–nu  Säljare, AMAX Konsult AB\nJag säljer ritningar och annan dokumentation som fastighetsägare behöver för att förvalta sina hus.\n- Kunderna är mest kommuner och kommunala bostadsbolag. Hittills har jag träffat 92 kunder.\n- Jag har sålt skanning av ritningsarkiv till en stor kommun i Skåne, drönarskanning av skötselytor till en annan och nu senast skanning av 400 ritningar i A1-format.\n\n2014–2023  Ägare och säljare, Cimco Nordic AB\nEget bolag. Jag sålde Cimcos handverktyg för elektriker till grossister i Norden.\n- Försäljningen gick från 1,5 miljoner euro 2015 till 2,2 miljoner 2022.\n- I Danmark, Finland och på Island träffade jag grossisterna själv några gånger om året. I Norge och Sverige sålde vi genom Melbye.\n- Mest stolt är jag över danska Lemvigh-Müller, som gick från ungefär 300 000 till 520 000 euro om året. Jag lade själv in alla nya artiklar i deras system, på danska.\n\n2005–2014  Säljare, Cimtools Scandinavia AB\nSamma verktyg och samma kunder. När jag startade eget följde kunderna med.\n\n2001–2005  Säljare, ESD Center AB\nSålde skydd mot statisk elektricitet till elektroniktillverkare: förpackningar, skydd för utrustning och personligt skydd.\n\n1994–2001  Elektronikmontör, SattControl, ABB Automation och Flextronics\nByggde ihop elektronik och apparatskåp åt kunder som Alfa Laval. På Flextronics hade jag också hand om underhållsgruppen och köpte in skyddsutrustning och inredning till produktionen.\n\n1988–1994  Butiksbiträde och verkstadsarbetare, Shell i Lysekil och Gökens Svets och Mekaniska i Uppsala\n\nIDROTT OCH LEDARSKAP\n2014–2025  Tränare, svenska landslaget i short track, Svenska Skridskoförbundet\nIdeellt vid sidan av jobbet, 15 till 20 timmar i veckan under de mest intensiva åren.\n- Hade tre till fem åkare och höll i träningar, planering och material.\n- Var förbundskapten på världscuper, EM, junior-VM och VM.\n- Bästa resultat var en niondeplats på 1 500 meter på EM 2018. Samma år tog vi en OS-plats.\n\n1989–1998  Landslagsåkare i short track\nÅkte själv i landslaget. Innan dess tävlade jag i alpint tills jag var 17.\n\nVARFÖR ÅRE\nVår son började som skidlärare i Åre 2016. Sedan dess har vi varit här två till tre gånger om året, både vinter och sommar. Nu flyttar vi upp för att komma närmare vårt barnbarn. Huset i Bonäshamn hittade vi av en slump och blev kära i direkt.\n\nÖPPEN FÖR\nJag kan tänka mig att sälja i en byggbutik eller köra taxi. Jag har också funderat på att skola om mig till elektriker. Pendlar gärna upp till fem mil.\n\nKOMPETENSER\n- Försäljning till företag (B2B)\n- Kundansvar och offerter\n- Butik och kundservice\n- Elektronik och montering\n- Underhåll och inköp\n- Ledarskap och träning\n\nUTBILDNING\n- Teknisk linje, maskin. Fyraårig, examen 1988\n- Internationella skridskoförbundets tränarutbildningar\n\nSPRÅK\n- Svenska och engelska\n- Klarar danska och norska i jobbet\n\nÖVRIGT\n- Egna skridskor: Har byggt ett tiotal skridskor själv, gjutna efter foten i läder och kolfiber.\n- Mark och trä: Lägger marksten och bygger trädäck. Har lärt mig hur viktigt underarbetet är.\n'

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
        "kwVersion": 2,
        "cvFiles": [
            {"name": "Designad (PDF)", "use": "När du mejlar en arbetsgivare eller lämnar över CV:t personligen", "file": "cv/Daniel_Jansson_CV.pdf"},
            {"name": "Enkel (PDF)", "use": "När du laddar upp i ett ansökningssystem, t.ex. hos kommunen eller SkiStar", "file": "cv/Daniel_Jansson_CV_enkel.pdf"},
            {"name": "Ren text", "use": "När ett formulär vill att du klistrar in ditt CV, eller när du ger det till en AI", "file": "cv/Daniel_Jansson_CV_text.txt"},
        ],
        "key": "daniel-jobbtavla-v2", "title": "Daniels jobbtavla", "name": "Daniel Jansson", "cv": DANIEL_CV, "dataFile": "jobs.json",
        "homes": {"hem": {"name": "hemma i Bonäshamn", "short": "Hemma", "lat": 63.412945, "lon": 13.366713},
                  "jarpen": {"name": "Järpen centrum", "short": "Järpen", "lat": 63.348, "lon": 13.470},
                  "are": {"name": "Åre", "short": "Åre", "lat": 63.399, "lon": 13.081}},
        "homeOpts": [["hem", "Hemma, Bonäshamn 665"], ["jarpen", "Järpen centrum"], ["are", "Åre"]],
        "defaultHome": "jarpen", "homeLabel": "Hemma, Bonäshamn 665",
        "kw": [["teknisk försäljning", 2], ["säljare", 2], ["försäljning", 2], ["b2b", 2], ["affärsutveckling", 2], ["kundansvarig", 2], ["key account", 2], ["account manager", 2], ["distriktsansvarig", 2], ["grossist", 2], ["elgrossist", 2], ["export", 1], ["kundrelationer", 1], ["offert", 1], ["förhandling", 1], ["nykund", 1], ["innesälj", 1], ["fältsälj", 1], ["butikssäljare", 2], ["byggvaruhus", 2], ["bygghandel", 2], ["järnhandel", 1], ["byggmaterial", 1], ["bauhaus", 1], ["byggmax", 1], ["xl-bygg", 1], ["beijer", 1], ["woody", 1], ["sportbutik", 1], ["skidor", 1], ["uthyrning", 1], ["elektriker", 2], ["elinstallation", 1], ["lärling", 1], ["installation", 1], ["elektronik", 1], ["industri", 1], ["underhåll", 1], ["inköp", 1], ["taxi", 2], ["chaufför", 1], ["förare", 1], ["fastighet", 1], ["ritning", 1], ["dokumentation", 1], ["offentlig sektor", 1], ["tränare", 1], ["ledarskap", 1], ["kundservice", 1], ["byggbutik", 2], ["trädgård", 1], ["skidlärare", 1], ["liftvärd", 1], ["drönare", 1], ["mässa", 1], ["danska", 1]],
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
                        "have": "24 år som säljare av tekniska produkter",
                        "say": "Jag har jobbat som säljare av tekniska produkter i 24 år. Innan dess stod jag sju år i elektronikproduktion, och det har jag haft nytta av varje gång en kund frågat hur något fungerar."
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
                        "have": "Eget bolag i nio år, försäljningen gick från 1,5 till 2,2 miljoner euro",
                        "say": "I nio år drev jag eget bolag och sålde handverktyg för elektriker till grossister i Norden. Försäljningen gick från 1,5 miljoner euro 2015 till 2,2 miljoner 2022."
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
                        "have": "Lemvigh-Müller gick från ungefär 300 000 till 520 000 euro om året",
                        "say": "Mest stolt är jag över danska Lemvigh-Müller, som gick från ungefär 300 000 till 520 000 euro om året. Jag lade själv in alla nya artiklar i deras system, på danska."
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
                        "have": "Säljer till kommuner och kommunala bostadsbolag, har träffat 92 kunder",
                        "say": "I dag säljer jag ritningar och dokumentation till kommuner och kommunala bostadsbolag. Hittills har jag träffat 92 kunder."
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
                        "have": "Sju år i elektronikproduktion, hade hand om underhåll och inköp på Flextronics",
                        "say": "Jag har stått sju år i elektronikproduktion hos SattControl, ABB och Flextronics. På Flextronics hade jag också hand om underhållsgruppen och köpte in utrustning."
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
                        "have": "Tränare för landslaget i short track i elva år, förbundskapten på VM och EM",
                        "say": "Vid sidan av jobbet har jag i elva år tränat svenska landslaget i short track och varit förbundskapten på världscuper, EM och VM."
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
                        "have": "Lägger marksten, bygger trädäck och har byggt egna skridskor",
                        "say": "Jag lägger marksten och bygger trädäck själv, och jag har byggt ett tiotal egna skridskor i läder och kolfiber. Så jag vet vad kunderna frågar efter."
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
                        "have": "B-körkort och egen bil, har kört mycket i jobbet",
                        "say": "Bilkörning har varit en stor del av mitt liv som säljare, och jag har B-körkort och egen bil."
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
                        "have": "Tävlade i alpint som ung, har varit i Åre flera gånger om året sedan 2016",
                        "say": "Jag tävlade i alpint som ung, och sedan vår son började som skidlärare i Åre 2016 har vi varit där flera gånger om året."
            }
        ],
        "draft": {
            "p1": "Hej!\n\nJag har läst er annons ”{title}” och söker gärna tjänsten. Vid årsskiftet flyttar min fru och jag till Bonäshamn utanför Järpen. Vi har köpt hus där för att komma närmare familjen.",
            "p4": "Jag berättar gärna mer om hur jag kan bidra hos {employer}. Jag är tillgänglig för intervju redan nu, på plats eller digitalt.\n\nVänliga hälsningar\n{name}",
        },
        "travelText": "Arbetsplatsen ligger cirka {km} km ({min}) med bil från hans nya hem i Bonäshamn.",
        "promptHead": "Skriv ett personligt brev på svenska för {name} till tjänsten nedan.",
        "promptRules": [
            "Högst 280 ord, så att det får plats på en A4 tillsammans med rubrik.",
                        "Koppla annonsens viktigaste krav till konkreta erfarenheter i CV:t.",
            "Nämn kort att han och frun flyttar till Bonäshamn utanför Järpen vid årsskiftet för att komma närmare familjen, och att huset redan är köpt. {travel}",
            "Daniel är öppen för många slags jobb: försäljning, butik (gärna bygghandel eller sport), teknik och körning. Välj vinkel efter just den här tjänsten och lyft de erfarenheter som passar bäst – för en butikstjänst hantverket och kundmötet, för en säljtjänst siffrorna från Cimco och Lemvigh-Müller.",
            "Använd gärna konkreta siffror från CV:t där de passar, men inte fler än två eller tre.",
            "Hitta inte på siffror, resultat eller erfarenheter som inte står i CV:t.",
            "Svara bara med brevtexten: börja med en hälsning och avsluta med \"Vänliga hälsningar\" och \"{name}\". Ingen rubrik, inga kontaktuppgifter, inga kommentarer.",
            "Skriv som personen själv pratar: korta, raka meningar på vardaglig men korrekt svenska. Det ska märkas att en människa har skrivit brevet.",
            "Använd inga tankstreck. Skriv hellre två meningar.",
            "Använd inte ord och fraser som driven, passionerad, brinner för, robust, noggrann, lagspelare, skapa värde, ständig utveckling eller spelat en avgörande roll.",
            "Ingen uppräkning i tre led för effekt, ingen sammanfattande slutkläm och inga överdrifter.",
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
            "Skriv som personen själv pratar: korta, raka meningar på vardaglig men korrekt svenska. Det ska märkas att en människa har skrivit brevet.",
            "Använd inga tankstreck. Skriv hellre två meningar.",
            "Använd inte ord och fraser som driven, passionerad, brinner för, robust, noggrann, lagspelare, skapa värde, ständig utveckling eller spelat en avgörande roll.",
            "Ingen uppräkning i tre led för effekt, ingen sammanfattande slutkläm och inga överdrifter.",
        ],
    },
}
PROFILES = [DANIEL, PROFIL2]
