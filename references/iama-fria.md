# IAMA en FRIA: vragen per onderdeel

Laatst inhoudelijk gecontroleerd: 6 oktober 2026, tegen de IAMA versie 2 (februari 2026) met het toelichtingsdocument, en artikel 27 AI Act zoals gewijzigd door de Digitale omnibus inzake AI (Verordening (EU) 2026/1744).

## Inhoud

- Waarvoor en hoe
- Markering [feit] en [team]
- Deel 1. Waarom?
- Deel 2. Wat?
- Deel 3. Hoe?
- Deel 4. Grondrechten
- Deel 5. Afsluiting
- FRIA: wat artikel 27 vraagt
- Generatieve AI

## Waarvoor en hoe

De **IAMA** (Impact Assessment Mensenrechten en Algoritmes) is ontwikkeld door de Universiteit Utrecht in opdracht van BZK. Het is een instrument voor dialoog en besluitvorming over impactvolle algoritmes en hoog-risico-AI, voor AI én voor algoritmes zonder AI. Versie 2 (2026) sluit aan op artikel 27 AI Act.

De **FRIA** (beoordeling van de gevolgen voor de grondrechten, artikel 27 AI Act) is verplicht voor bepaalde gebruiksverantwoordelijken van hoog-risico-AI (zie `triage.md`). De IAMA is een manier om de FRIA uit te voeren.

De IAMA is bedoeld om **in een team** te bespreken: projectleider, data scientist, jurist en andere betrokkenen, samen 4 tot 7 mensen met een gespreksleider, verspreid over meerdere dagen, bijvoorbeeld twee sessies van drie uur of drie sessies van twee uur. Deel 4 vraagt juridisch uitzoekwerk. Jij vervangt die sessies niet. Jij helpt de gebruiker om de feitelijke vragen alvast te beantwoorden en de discussiepunten voor de teamsessie te verzamelen. Zeg dit aan het begin van de module in je eigen woorden.

Gebruik `crosswalk.md` om niets dubbel te vragen: veel vragen zijn al beantwoord in de gedeelde basis of de DPIA. Bevestig die alleen.

## Markering [feit] en [team]

- **[feit]**: stel deze vraag nu, als hij nog niet beantwoord is. Het gaat om feiten die de gebruiker kan weten of kan opzoeken.
- **[team]**: stel deze vraag niet nu. Noteer hem als agendapunt voor de teamsessie, eventueel met wat je al weet als startpunt.

Risico's en nadelige gevolgen voor mensen bespreek je niet in deze module, maar één keer in fase 4. Die risicolijst dient voor de DPIA, de IAMA en de FRIA.

## Deel 1. Waarom?

Dit deel komt eerst, vóór de techniek, omdat het doel bepaalt of de rest gerechtvaardigd is.

**1.1 Aanleiding en doel**
- [feit] Wat was de aanleiding? Welk probleem lost het algoritme op?
- [feit] Wat is het hoofddoel, en wat zijn de subdoelen?
Doorvragen bij "efficiëntie" of "slimmer werken": wat wordt concreet beter, voor wie, en hoe meet je dat?

**1.2 Publieke waarden** (maximaal zes per vraag)
- [team] Welke publieke waarden worden mogelijk positief geraakt? Bijvoorbeeld rechtvaardigheid, doelmatigheid, toegankelijkheid, veiligheid.
- [team] Welke publieke waarden worden mogelijk negatief geraakt? Bijvoorbeeld privacy, gelijke behandeling, menselijk contact, vertrouwen in de overheid.
Voor private organisaties: de waarden van klanten, medewerkers en samenleving.

**1.3 Wettelijke grondslag**
- [feit] Is het mogelijk een verboden AI-toepassing? (Zie `aanvullende-toetsen.md` A2.) Zo ja, meld het direct.
- [feit] Wordt het algoritme gebruikt voor een wettelijke taak? Welke wet? (Volgens de IAMA is voor een algoritme dat alleen voor interne processen wordt gebruikt en geen directe impact op mensen heeft, geen wettelijke taak als grondslag nodig. Worden persoonsgegevens verwerkt, dan blijft een AVG-grondslag altijd nodig; die bepaal je in de DPIA.)

**1.4 Verantwoordelijkheden**
- [feit] Welke partijen en functies zijn betrokken bij ontwikkeling, inzet en beheer?
- [feit] Wie is eindverantwoordelijk?
- [feit] Is er een exitstrategie als het algoritme later niet meer gewenst is?

## Deel 2. Wat?

Bij een ingekocht systeem staan veel antwoorden in de gebruiksaanwijzing of documentatie van de leverancier. Stel voor die op te vragen; ontbrekende antwoorden worden open punten voor de leverancier.

**2.1 Type algoritme**
- [feit] Is het zelflerend (een getraind model of generatieve AI) of niet-zelflerend (vaste regels)?
- [team] Welke alternatieven zijn er, en waarom is dit type het meest geschikt?

**2.2A Bij vaste regels**
- [feit] Hoe zijn de beslisregels tot stand gekomen, en door wie?
- [team] Welke aannames en mogelijke bias zitten in de regels?
- [feit] Welke indicatoren worden gebruikt, en zijn ze allemaal nodig? Stel hier ook de selectievragen uit `doorvragen.md` als die nog niet gesteld zijn.

**2.2B Bij een zelflerend model**
- [feit] Op welke gegevens is het model getraind en getest? (Vaak een open punt voor de leverancier.)
- [team] Zijn die gegevens van voldoende kwaliteit en representatief voor de situatie waarin jullie het gebruiken?
- [feit] Welke gegevens gebruikt het model, en zijn ze allemaal nodig?

**2.3 Inzet**
- [feit] Welke gegevens krijgt het algoritme straks als invoer, en uit welke bronnen? (Meestal al bekend uit de gedeelde basis.)
- [team] Welke aannames en bias zitten in die invoergegevens?

**2.4 Kwaliteit en nauwkeurigheid**
- [feit] Hoe wordt de kwaliteit gemeten, en wat zegt de leverancier over de nauwkeurigheid?
- [team] Wanneer is de kwaliteit goed genoeg?
- [feit] Welke fouten kan het algoritme maken? Denk aan ten onrechte geselecteerd worden en ten onrechte gemist worden. (De gevolgen daarvan komen in fase 4.)

**2.5 Datagovernance en beveiliging**
- [feit] Bij een externe partij: zijn eigenaarschap en beheer van het algoritme afgesproken?
- [feit] Wie heeft toegang tot de invoer- en uitvoergegevens, en hoe zijn die beveiligd? (Vaak al bekend uit de gedeelde basis.)

## Deel 3. Hoe?

Een algoritme veroorzaakt zelden zelf schade; het gaat mis in hoe het wordt gebruikt.

**3.1 Gebruikscontext**
- [feit] Wat gebeurt er met de uitkomst? Welke beslissingen volgen erop, en door wie?
- [feit] Wanneer wordt het ingezet, hoe lang, hoe vaak en waar (welke gebieden, groepen of zaken)?
- [team] Kan het onbedoelde gevolgen hebben voor andere processen of systemen?

**3.2 De rol van de medewerker**
- [feit] Welke rol speelt de medewerker (menselijke tussenkomst)?
- [feit] Kan de medewerker afwijken van de uitkomst? Gebeurt dat in de praktijk, en is daar tijd en ruimte voor?
- [feit] Welke training krijgen medewerkers (AI-geletterdheid)?
- [team] Gaat er kennis of vakmanschap verloren?

**3.3 Communicatie**
- [feit] Weten de mensen om wie het gaat dat het algoritme wordt gebruikt? Hoe worden ze geïnformeerd?
- [feit] Wie is verantwoordelijk voor de communicatie, intern en extern?
- [team] Hoe uitlegbaar is de uitkomst voor de mensen om wie het gaat?

**3.4 Monitoring en evaluatie**
- [feit] Hoe wordt het gebruik gevolgd, en wie kan bijsturen of stoppen?
- [feit] Kunnen medewerkers en de mensen om wie het gaat makkelijk melden of klagen? Wat gebeurt er dan?
- [team] Kan het algoritme later voor andere doelen worden gebruikt (function creep)? Hoe voorkom je dat?
- [feit] Wanneer is de inzet een succes, en wanneer wordt dat gemeten?

**3.5 Gevolgen voor mensen en samenleving**
- [feit] Welke mensen of groepen worden geraakt? Denk ook aan groepen die je niet direct ziet.
- [feit] Hebben betrokkenen inspraak, en is er een opt-out?
- [team] Welke positieve gevolgen zijn er?
- [team] Kan het leiden tot ongewenste maatschappelijke effecten, zoals afhankelijkheid van technologie of minder vertrouwen in instellingen?
- [team] Zijn er zorgen die nog niet aan bod zijn gekomen?
De risico's en nadelige gevolgen voor deze groepen bespreek je in fase 4.

## Deel 4. Grondrechten

Dit deel hoort in de teamsessie met een jurist. Bereid het voor na fase 4, op basis van de risicolijst.

**4.1 Welke grondrechten?** [team, met een korte voorzet]
Zet bij elk risico uit fase 4 het geraakte grondrecht, en vat dat samen per cluster uit de IAMA-toelichting:
1. **Aan de persoon gerelateerd**: menselijke waardigheid, privacy en bescherming van persoonsgegevens, lichamelijke en geestelijke integriteit, gezinsleven, goede arbeidsomstandigheden, bestaansminimum.
2. **Vrijheidsrechten**: meningsuiting, vereniging, godsdienst, bewegingsvrijheid.
3. **Gelijkheidsrechten**: gelijke behandeling en het verbod op discriminatie, direct en indirect.
4. **Procedurele rechten**: eerlijk proces, behoorlijk bestuur, motivering, toegang tot de rechter, effectief rechtsmiddel.

**4.2 Specifieke wetgeving** [team, uitzoekwerk voor de jurist]
Noteer als uitzoekvragen:
- Is het een hoog-risico-AI-systeem? (Voorlopige inschatting uit de triage.)
- Is een DPIA nodig? Zo ja: gebruik de IAMA-antwoorden in de DPIA en omgekeerd.
- Kan het algoritme direct of indirect onderscheid maken dat onder de gelijkebehandelingswetgeving valt?
- Gelden andere wetten, zoals de Algemene wet bestuursrecht, procesrecht, consumentenrecht of de DSA?
- Is er rechtspraak met concrete criteria?

**4.3 tot en met 4.5** [team] zijn alleen nodig als er een negatieve impact is waarover wetgeving of rechtspraak geen duidelijk antwoord geeft. Noteer als agenda: hoe zwaar weegt het geraakte grondrecht en hoe groot is de inbreuk (licht, medium of ernstig); is het algoritme echt geschikt; kan het doel ook zonder dit algoritme of met een aangepaste versie; welk restrisico blijft over. Hoe ernstiger de inbreuk, hoe effectiever en noodzakelijker het algoritme moet zijn.

## Deel 5. Afsluiting

[team] Bereid voor als agenda voor de besluitvorming, na fase 4:
- **Belangenafweging**: wat pleit voor de inzet (doelen, positieve waarden, effectiviteit) en wat ertegen (gevolgen voor mensen, maatschappelijke zorgen, ernst van de inbreuk, alternatieven, kosten)?
- **Advies**: wel of niet inzetten, onder welke voorwaarden en waarom. Het besluit ligt bij de bestuurlijk of inhoudelijk verantwoordelijke.
- **Restrisico's**: welke blijven over na alle maatregelen? De verantwoordelijke moet die bewust accepteren of afwijzen.

## FRIA: wat artikel 27 vraagt

Zorg dat deze zes onderdelen in het concept staan (artikel 27 lid 1). Waar je ze vindt, staat in `crosswalk.md`:
- (a) de processen waarin het systeem wordt gebruikt, volgens het beoogde doel
- (b) de periode en frequentie van gebruik
- (c) de categorieën personen en groepen die waarschijnlijk geraakt worden
- (d) de specifieke risico's op schade voor die groepen, rekening houdend met de informatie die de aanbieder moet geven (artikel 13)
- (e) hoe het menselijk toezicht volgens de gebruiksaanwijzing is geregeld
- (f) wat er gebeurt als risico's zich voordoen, inclusief interne governance en klachtenregelingen

Vraag of de gebruiksaanwijzing en de informatie van de aanbieder al beschikbaar zijn; zonder die stukken zijn (d) en (e) niet goed in te vullen.

Verder:
- De FRIA is nodig vóór het **eerste gebruik**. Bij vergelijkbare gevallen mag een eerdere FRIA of een beoordeling van de aanbieder worden hergebruikt. Wijzigt er iets, dan moet de FRIA worden bijgewerkt (lid 2).
- Na afloop moet de organisatie de **markttoezichthouder** informeren over de resultaten, met het ingevulde model van het AI Office (lid 3).
- De FRIA mag **verwijzen naar de DPIA** of delen ervan overnemen waar die al aan dezelfde eisen voldoet (lid 4, zoals gewijzigd).
- Het **AI Office** ontwikkelt een model-vragenlijst, ook als geautomatiseerd hulpmiddel (lid 5). Op 6 oktober 2026 was die nog niet gepubliceerd; laat de jurist controleren of dat inmiddels wel zo is.
- Tijdlijn: zie `aanvullende-toetsen.md` A6.

## Generatieve AI

Bij generatieve AI (zoals een taalmodel van een externe leverancier) zijn sommige vragen moeilijk te beantwoorden: de trainingsgegevens zijn vaak onbekend en het model is niet te doorgronden. Bias in het model is dan een gegeven. De IAMA-toelichting adviseert de aandacht te verleggen naar de **uitkomsten**: welke vormen van bias treden op in de output, en wat doe je om die op te vangen (bijvoorbeeld testen met voorbeelden, controle door een mens, duidelijke grenzen aan het gebruik)? Bij algemene AI-systemen is een heldere doelbinding extra belangrijk: leg vast waarvoor het wel en niet gebruikt mag worden.
