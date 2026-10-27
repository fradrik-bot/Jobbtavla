"""Bygger index.html från template.html och senaste jobs.json."""
import json
d = json.load(open("jobs.json", encoding="utf-8"))
s = open("template.html", encoding="utf-8").read()
open("index.html", "w", encoding="utf-8").write(s.replace("__SNAPSHOT__", json.dumps(d, ensure_ascii=False).replace("</", "<\\/")))
