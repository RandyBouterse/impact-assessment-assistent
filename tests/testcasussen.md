# Testcasussen

Gebruik deze casussen om de assistent te testen na een wijziging, of om hem in een nieuw platform uit te proberen. Speel de gebruiker; geef bewust ook vage antwoorden. Vergelijk de assessmentkaart met de verwachte uitkomst. De verwachte uitkomst is een inschatting volgens de regels in deze skill, geen juridisch oordeel.

Controleer bij elke test ook het gedrag:
- één vraag per bericht, vraag als laatste
- uitleg op verzoek en daarna terug naar de vraag
- maximaal twee keer doorvragen, daarna een open punt
- geen juridisch eindoordeel
- tipsblok na de assessmentkaart

---

## 1. Gemeente: AI-score voor bijstandsaanvragen

**Situatie:** een gemeente wil een SaaS-dienst van een Amerikaanse leverancier die bijstandsaanvragen samenvat en een prioriteitsscore geeft voor extra onderzoek. Data "in Europa".
**Gedrag testen:** zeg "klantgegevens", "het is anoniem", "de consulent beslist toch"; vraag "wat is een grondslag?"; upload een projectplan met twee namen van aanvragers.
**Verwacht:**
- DPIA: nodig
- AI Act: systeem waarschijnlijk hoog risico vanwege de score (bijlage III 5a, profilering); de samenvatfunctie valt daaronder tenzij die als apart systeem wordt ingezet; jurist stelt vast
- AI Act-plichten gebruiksverantwoordelijke: waarschijnlijk nodig, vanaf 2 december 2027, uiterlijk 2 augustus 2030 voor bestaand overheidsgebruik
- FRIA: waarschijnlijk nodig (als hoog risico bevestigd)
- IAMA: waarschijnlijk nodig
- DTIA: nog onduidelijk (helpdesk of subverwerkers buiten de EER?); buitenlandse zeggenschap als risico in DPIA en cloudafweging
- Algoritmeregister: waarschijnlijk nodig; EU-databank bij hoog risico
- AI-geletterdheid: nodig
- Cloud en soevereiniteit: waarschijnlijk nodig (kerntaak, Amerikaanse leverancier; rijksbeleid als leidraad)
- Informatiebeveiliging: nodig (BIO2)
- Transparantie artikel 50: niet nodig; wel informatieplicht AVG en motiveringsplicht
- OR: nog onduidelijk; nodig (instemming) als gebruik per consulent wordt vastgelegd
- Richtwaarde duur: 60 tot 90 minuten
- Upload: melding zonder namen te herhalen, vandaag nog naar de FG, op de actielijst

## 2. Logistiek bedrijf: productiviteitsmonitoring met uitvalvoorspelling

**Situatie:** private onderneming, 600 medewerkers, handscanners meten productiviteit; AI-functie voorspelt uitval; hosting "in Europa" bij een hyperscaler.
**Gedrag testen:** zeg "met toestemming van de medewerkers" en "geen gevoelige gegevens"; vraag "waarom wil je dat weten?"; upload een eigen DPIA-format met acht hoofdstukken en een 5x5-risicomatrix.
**Verwacht:**
- DPIA: nodig (controle werknemers, stelselmatig)
- Grondslag: toestemming geproblematiseerd; voor de productiviteitsmeting route via gerechtvaardigd belang met belangenafweging
- Uitvalvoorspelling: waarschijnlijk een gezondheidsgegeven; dan geldt het verwerkingsverbod van artikel 9 AVG en volstaat gerechtvaardigd belang niet (artikel 30 UAVG biedt de werkgever slechts beperkte ruimte, vooral voor verzuimbegeleiding en re-integratie); belangrijkste aandachtspunt voor de jurist; tip bedrijfsarts
- AI Act: waarschijnlijk hoog risico (bijlage III punt 4); plichten artikel 26, inclusief werknemers vooraf informeren
- FRIA: niet nodig (private werkgever zonder openbare dienst), met de vermelding dat andere plichten wel gelden
- OR: instemming nodig
- Uitvoer in het eigen format; risico's in fase 4 direct gescoord op de 5x5-matrix van het format

## 3. Ministerie: generatieve AI-assistent voor beleidsmedewerkers

**Situatie:** een ministerie wil een taalmodel van een Amerikaanse aanbieder inzetten om beleidsnotities samen te vatten en concepten te schrijven, via een publieke clouddienst. Documenten bevatten soms persoonsgegevens.
**Verwacht:**
- DPIA: nodig (materieel cloudgebruik met persoonsgegevens, nieuwe technologie)
- Cloud en soevereiniteit: nodig (risicoanalyse, exitplan, melding CISO Rijk; documenten in principe niet in de publieke cloud)
- AI Act: waarschijnlijk minimaal risico; AI-geletterdheid; transparantie alleen bij gepubliceerde teksten zonder menselijke redactie
- DTIA: nog onduidelijk
- Algoritmeregister: nodig (Rijksoverheid)
- IAMA: niet nodig zolang het een interne schrijfhulp is zonder directe gevolgen voor burgers; aan te raden als het gebruik impactvol wordt
- Informatiebeveiliging: nodig (BIV-classificatie, BIO2)
- OR: waarschijnlijk nodig (advies, belangrijke technologische voorziening); instemming nodig als de dienst gebruiks- of promptlogs per medewerker vastlegt, anders nog onduidelijk
- Archief en Woo: signaleren

## 4. Webwinkel: chatbot voor klantenservice

**Situatie:** een webwinkel wil een AI-chatbot die vragen over bestellingen beantwoordt en toegang heeft tot ordergegevens.
**Verwacht:**
- DPIA: nog onduidelijk of waarschijnlijk nodig, afhankelijk van schaal en nieuwe technologie
- AI Act: transparantie (chatbot herkenbaar als AI); geen hoog risico
- Verwerkersovereenkomst en locatie: signaleren
- Cloud: geen apart assessment bij alleen buitenlandse zeggenschap zonder kritiek proces; wel als risico in de DPIA
- Informatiebeveiliging: lichte vorm (beveiligingsvragen aan de leverancier)

## 5. Ziekenhuis: AI-triage op de spoedeisende hulp

**Situatie:** een ziekenhuis (private organisatie die een openbare dienst verleent) wil een AI-systeem dat patiënten op de SEH een urgentie geeft.
**Verwacht:**
- DPIA: nodig (gezondheidsgegevens, kwetsbare personen)
- AI Act: waarschijnlijk hoog risico (bijlage III 5d, triage); mogelijk ook medisch hulpmiddel (bijlage I, vanaf 2 augustus 2028), via de vraag over productregels in T7; jurist stelt vast
- Geen vals verbodssignaal: meten van lichaamssignalen bij patiënten valt niet onder het verbod op emotieherkenning
- Tip: medische technologie of regulatory affairs
- FRIA: waarschijnlijk nodig (openbare dienst)

## 6. Hogeschool: online proctoring bij tentamens

**Situatie:** een hogeschool wil software die via de webcam fraude detecteert bij online tentamens, inclusief analyse van gezichtsuitdrukkingen.
**Verwacht:**
- AI Act: emotieherkenning op basis van gezichtsuitdrukking in het onderwijs is mogelijk verboden (artikel 5): belangrijkste aandachtspunt; fraudedetectie zonder emotieherkenning waarschijnlijk hoog risico (bijlage III 3d)
- DPIA: nodig
- FRIA: waarschijnlijk nodig als het systeem niet verboden blijkt (onderwijs als openbare dienst)
- Mogelijk verbod: direct gemeld in een apart bericht en in de eerste rij van de kaart
- Medezeggenschapsraad: signaleren
- Algoritmeregister: nog onduidelijk (eigen beleid of sectorafspraken)

## 7. Gemeente: slimme camera's in het centrum

**Situatie:** een gemeente wil camera's die drukte meten met beeldanalyse, zonder gezichtsherkenning, met opslag van beelden gedurende 28 dagen.
**Verwacht:**
- DPIA: nodig (monitoring van openbare ruimte)
- AI Act: afhankelijk van de analyse; geen biometrische identificatie bevestigen; jurist stelt vast
- Doorvragen op "geen gezichtsherkenning" en bewaartermijn

## 8. Bank: kredietscoremodel

**Situatie:** een bank laat een AI-model bepalen welke klanten een lening krijgen.
**Verwacht:**
- DPIA: nodig
- AI Act: waarschijnlijk hoog risico (bijlage III 5b)
- FRIA: waarschijnlijk nodig (kredietwaardigheid, ook voor een private partij)
- Doorvragen op geautomatiseerde besluitvorming (artikel 22 AVG)
- Rol: bij een zelf gebouwd model waarschijnlijk ook aanbieder; rij "AI Act-plichten aanbieder" op de kaart
- Sectorregels signaleren (onder meer DORA, toezicht DNB en AFM)

## 9. HR-afdeling: cv-screening met AI

**Situatie:** een bedrijf wil sollicitaties automatisch laten filteren en rangschikken.
**Verwacht:**
- DPIA: nodig
- AI Act: waarschijnlijk hoog risico (bijlage III 4a); plichten artikel 26; kandidaten informeren
- FRIA: niet nodig voor een gewone private werkgever, met vermelding van andere plichten
- OR: nodig (instemming, werving en selectie) als er een OR is; anders nog onduidelijk
- Doorvragen op discriminatie via indirecte kenmerken (in fase 3)

## 10. Intern team: Excel-rekenregel voor roosters

**Situatie:** een team gebruikt een spreadsheet met vaste regels om roosters te maken op basis van beschikbaarheid. Geen AI, alleen namen en beschikbaarheid.
**Verwacht:**
- DPIA: niet nodig of nog onduidelijk; onderbouwing vastleggen. Staan er gezondheidsopmerkingen in het bestand, dan als eenvoudige maatregel: die kolom schrappen
- AI Act: niet van toepassing (vaste regels, geen AI-systeem)
- Cloud: niet nodig (bestaand, al beoordeeld platform)
- Lichte route: korte uitkomst met onderbouwing, geen verdieping tenzij de gebruiker dat wil
