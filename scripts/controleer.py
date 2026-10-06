"""Controles die bij elke wijziging moeten slagen. Lokaal: python3 scripts/controleer.py"""
import pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
LIMIET = 8000
fouten = []

# 1. De promptversie moet passen in platforms met een limiet van 8.000 tekens.
tekst = (ROOT / "prompt-versie/systeemprompt.md").read_text(encoding="utf-8")
delen = tekst.split("\n---\n")
if len(delen) < 3:
    fouten.append("systeemprompt.md: prompt niet gevonden tussen twee regels met ---")
else:
    lengte = len(delen[1].strip())
    print(f"Promptversie: {lengte} van {LIMIET} tekens")
    if lengte > LIMIET:
        fouten.append(f"systeemprompt.md: prompt is {lengte} tekens, maximaal {LIMIET}")

# 2. Elk referentiebestand vermeldt wanneer het inhoudelijk is gecontroleerd.
for pad in sorted((ROOT / "references").glob("*.md")):
    kop = pad.read_text(encoding="utf-8").splitlines()[:5]
    if not any(r.startswith("Laatst inhoudelijk gecontroleerd:") for r in kop):
        fouten.append(f"{pad.relative_to(ROOT)}: regel 'Laatst inhoudelijk gecontroleerd:' ontbreekt bovenaan")

# 3. SKILL.md verwijst alleen naar bestanden die bestaan.
import re
skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
for ref in sorted(set(re.findall(r"`(references/[\w-]+\.md)`", skill))):
    if not (ROOT / ref).exists():
        fouten.append(f"SKILL.md verwijst naar {ref}, maar dat bestand bestaat niet")

for f in fouten:
    print("FOUT:", f)
sys.exit(1 if fouten else 0)
