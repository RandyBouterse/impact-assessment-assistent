# Triage: welke assessments zijn nodig?

Laatst inhoudelijk gecontroleerd: 6 oktober 2026, tegen de brontekst van de AVG, de AI Act (Verordening (EU) 2024/1689) zoals gewijzigd door de Digitale omnibus inzake AI (Verordening (EU) 2026/1744), het Model DPIA Rijksdienst (augustus 2026), de IAMA (februari 2026) en de Herziening rijksbreed cloudbeleid 2026. Wetgeving en beleid veranderen; controleer bij twijfel de bron of vraag het de jurist.

## Inhoud

1. Hoe je de triage uitvoert
2. De triagevragen (T1 tot en met T16)
3. Beslisregels per assessment
4. De assessmentkaart en het tipsblok

De inhoudelijke uitwerking van AI Act, DTIA, cloud, beveiliging, OR en overige toetsen staat in `aanvullende-toetsen.md`. Deze triage bepaalt alleen wat nodig is.

## 1. Hoe je de triage uitvoert

- Haal eerst zoveel mogelijk antwoorden uit fase 1 (het verhaal of de documenten van de gebruiker). Stel alleen de vragen die nog open staan; bevestig de rest in één korte opsomming.
- Stel de vragen één voor één. Sla vragen over die door een eerder antwoord niet meer relevant zijn (geen persoonsgegevens: T2 tot en met T4 vervallen; geen algoritme of AI: T7 tot en met T8 vervallen).
- Doorvragen en "weet ik niet": volg de vaste regel in `SKILL.md` (regel 6).
- Een onduidelijk antwoord telt in de beslisregels als "mogelijk ja". Liever een assessment als "waarschijnlijk nodig" markeren dan het missen.
- **Functies apart bekijken, systeem als geheel classificeren.** Doet één systeem meerdere dingen (bijvoorbeeld samenvatten én een score geven), stel T6 tot en met T8 per functie om te zien welke functie het risico bepaalt. De AI Act kijkt naar het beoogde doel van het systeem: valt één doel onder bijlage III, dan is het hele systeem waarschijnlijk hoog risico. Een lichtere uitkomst voor een andere functie geldt alleen als die een apart systeem is of apart wordt ingezet. De jurist stelt dit vast.

## 2. De triagevragen

**T1. Gebruik je gegevens over mensen?**
Waarom: dan geldt de AVG.
Uitleg: alles waarmee je iemand direct of indirect kunt herkennen. Ook een personeelsnummer, IP-adres, kenteken, camerabeeld, stemopname of een combinatie van gegevens (postcode plus geboortedatum plus beroep). Ook als jij de persoon niet kent maar een ander dat wel kan. Denk ook aan de medewerkers die met het systeem werken: hun inloggegevens en logbestanden zijn ook persoonsgegevens.

**T2. Gaat het om gevoelige gegevens?**
Waarom: voor deze gegevens gelden strengere regels.
Drie soorten, elk met eigen regels:
- Bijzondere persoonsgegevens (artikel 9 AVG): gezondheid, ras of etnische afkomst, religie of levensovertuiging, politieke opvattingen, vakbondslidmaatschap, seksueel gedrag of geaardheid, genetische gegevens en biometrie om iemand uniek te identificeren.
- Strafrechtelijke persoonsgegevens (artikel 10 AVG): strafbare feiten, verdenkingen, veroordelingen.
- Het BSN en andere wettelijke identificatienummers (artikel 87 AVG, artikel 46 UAVG): alleen als een wet het gebruik toestaat.
Daarnaast gegevens die in de praktijk gevoelig zijn: financiële situatie, schulden, locatiegegevens, inhoud van communicatie.
Let op: ook afgeleide of voorspelde gegevens tellen mee. Een voorspelling van ziekteverzuim, stress of zwangerschap kan een gezondheidsgegeven zijn. Een bankafschrift kan via betalingen indirect bijzondere gegevens bevatten. Bij bijzondere persoonsgegevens geldt een verwerkingsverbod met beperkte uitzonderingen (artikel 9 AVG); een gewone grondslag zoals gerechtvaardigd belang is dan niet genoeg. Markeer dit als belangrijk aandachtspunt voor de jurist.

**T3. Gaat het om mensen in een kwetsbare positie?**
Waarom: zij kunnen minder makkelijk opkomen voor zichzelf of zijn afhankelijk van de organisatie.
Voorbeelden: kinderen, ouderen, patiënten, mensen met een uitkering of schulden, asielzoekers, mensen met een beperking, medewerkers (afhankelijk van hun werkgever).
Let op de proportionaliteit: bij medewerkers telt dit als EDPB-criterium vooral als ze beoordeeld, gevolgd of geselecteerd worden. Bij gewone, kleinschalige personeelsadministratie (zoals een rooster of contactlijst) niet.

**T4. Om hoeveel mensen gaat het, ongeveer?**
Waarom: grootschalige verwerking verhoogt het risico. Een schatting is genoeg.

**T5. Worden mensen beoordeeld, ingedeeld of wordt er over hen beslist?**
Waarom: beoordelingen en beslissingen kunnen grote gevolgen hebben.
Voorbeelden: een risicoscore, fraudesignaal, selectie voor controle, prioriteit in een wachtrij, advies over een aanvraag, ranking van sollicitanten, kredietscore, automatisch toekennen of weigeren.
Vraag door: beslist een systeem dit (deels) automatisch, of beslist altijd een mens? Wat zijn de gevolgen voor de persoon?

**T6. Gebruik je een algoritme of AI?**
Waarom: dan kunnen de AI Act en extra toetsen gelden.
Maak onderscheid, want de regels verschillen:
- **Algoritme met vaste regels**: een beslisboom, rekenregel of vaste set criteria die mensen hebben bedacht. Valt meestal niet onder de AI Act, maar wel onder de AVG, het Algoritmekader en eventueel de IAMA.
- **AI-systeem**: een systeem dat uit gegevens afleidt hoe het tot een uitkomst komt (een voorspelling, aanbeveling, beslissing, tekst of beeld), bijvoorbeeld een getraind model, ChatGPT, Copilot of een chatbot. Hiervoor geldt de AI Act.
Weet de gebruiker het niet: vraag of het systeem "geleerd" heeft van voorbeelden of zelf teksten of voorspellingen maakt. Blijft het onduidelijk, noteer "mogelijk AI" en een open punt voor de leverancier.

**T7. Als er AI is: waarvoor wordt het ingezet?**
Waarom: in een aantal toepassingsgebieden kan AI "hoog risico" zijn (bijlage III AI Act). Vraag naar het concrete doel en vergelijk met deze lijst (vereenvoudigd, gebruik de exacte criteria in `aanvullende-toetsen.md`):
- biometrie: identificatie op afstand, categorisering op gevoelige kenmerken, emotieherkenning
- veiligheidscomponent van kritieke infrastructuur
- onderwijs: toelating, beoordeling van leerresultaten, niveaubepaling, toezicht bij toetsen
- werk: werving en selectie, besluiten over arbeidsvoorwaarden, promotie of ontslag, taaktoewijzing op basis van gedrag of kenmerken, monitoren en beoordelen van prestaties en gedrag
- essentiële diensten: door of namens de overheid beoordelen of iemand recht heeft op een uitkering of dienst, of die verlenen, beperken, intrekken of terugvorderen; kredietwaardigheid; risico en prijs bij levens- en ziektekostenverzekeringen; noodoproepen en triage
- rechtshandhaving, migratie en grenzen, rechtspraak en verkiezingen
Vraag ook: is het systeem (onderdeel van) een product waarvoor al Europese productregels gelden, zoals een medisch hulpmiddel met CE-markering, een machine of speelgoed? Dan kan het via bijlage I hoog risico zijn (vanaf 2 augustus 2028).
Uitkomst van T7 is nooit een eindoordeel. Gebruik "waarschijnlijk hoog risico" en laat de jurist het vaststellen. Zie de uitzonderingen en de profileringsregel in `aanvullende-toetsen.md`.

**T8. Doet het systeem iets wat in de AI Act verboden is?**
Waarom: verboden toepassingen kun je met maatregelen niet alsnog toegestaan maken.
Vraag alleen door als het systeem in de buurt komt van een verboden toepassing (lijst in `aanvullende-toetsen.md`, onderdeel A2). Het verbod op emotieherkenning geldt alleen op de werkplek en in het onderwijs, en niet bij medische of veiligheidsredenen; het meten van hartslag bij patiënten valt er dus niet onder. Voorbeelden: emotieherkenning op basis van lichaamskenmerken (camera, stem, wearables) op de werkplek of in het onderwijs; social scoring; misdaadvoorspelling alleen op basis van profilering.
Bij een mogelijke "ja": meld dit direct, in een apart bericht, als belangrijkste aandachtspunt voor de jurist, zonder het als vaststaand oordeel te brengen. Zet het op de kaart in de eerste rij als "mogelijk verboden toepassing". Alle andere uitkomsten op de kaart gelden dan "als het systeem niet verboden blijkt".

**T9. Worden mensen gevolgd of in de gaten gehouden?**
Waarom: stelselmatige monitoring is een risicofactor en kan instemming van de ondernemingsraad vereisen.
Voorbeelden: camera's, locatie volgen, registratie van computergebruik of productiviteit, e-mails analyseren, klikgedrag, sensoren.

**T10. Koppel of combineer je gegevens, of gebruik je ze voor een ander doel dan waarvoor ze verzameld zijn?**
Waarom: koppelen en hergebruiken vergroot risico's en kan botsen met het oorspronkelijke doel.

**T11. Is de technologie of werkwijze nieuw voor jullie?**
Waarom: bij nieuwe technologie zijn de risico's minder bekend.

**T12. Werk je met een externe leverancier, clouddienst of SaaS-applicatie?**
Vraag door: welke leverancier, welk product, waar draait het, en is er een verwerkersovereenkomst? Werken medewerkers met het systeem, vraag dan ook of het gebruik per medewerker wordt vastgelegd (logs, prompts, activiteit); dat is van belang voor de OR.

**T13. Waar staan de gegevens, en wie kan erbij?**
Waarom: twee verschillende risico's, die je apart moet beoordelen.
- **Doorgifte**: gaan gegevens naar een land buiten de EER, of kan iemand van buiten de EER ze bekijken (bijvoorbeeld een helpdesk op afstand)? Dan kan een DTIA nodig zijn.
- **Buitenlandse zeggenschap**: valt de leverancier (of zijn moederbedrijf) onder het recht van een land buiten de EU, ook als de gegevens in Europa staan? Dat is geen doorgifte, maar wel een risico voor de DPIA en de soevereiniteitsafweging, omdat een buitenlandse overheid de leverancier kan dwingen gegevens af te geven.
Weet de gebruiker het niet: open punt voor inkoop, de architect of de leverancier.

**T14. Hoe belangrijk en hoe vertrouwelijk is dit proces?**
Vraag: wat gebeurt er als het systeem een dag niet werkt? Wat als de gegevens op straat liggen? Is er een BIV-classificatie? Valt de organisatie onder de Cyberbeveiligingswet?

**T15. Praat het systeem met mensen, of maakt het teksten, beelden of geluid?**
Waarom: dan kunnen transparantieplichten gelden (artikel 50 AI Act, de AVG en het bestuursrecht). De uitwerking staat in `aanvullende-toetsen.md`, onderdeel B.
Voorbeelden: een chatbot, AI-gegenereerde brieven of nieuwsberichten, synthetische stemmen, AI-beelden.

**T16. Bestaat er al een DPIA of ander assessment voor deze of een vergelijkbare toepassing?**
Waarom: hergebruiken of actualiseren scheelt werk. Voor veel standaardsoftware bestaan openbare DPIA's (SLM Rijk, SURF). Een algemene DPIA van een leverancier of koepel vervangt nooit de eigen DPIA, maar is een goed vertrekpunt.

## 3. Beslisregels per assessment

Gebruik voor elke uitkomst één van deze vier labels: **nodig**, **waarschijnlijk nodig**, **niet nodig**, **nog onduidelijk**. Voeg zo nodig een voorwaarde toe tussen haakjes, bijvoorbeeld "waarschijnlijk nodig (als de jurist hoog risico bevestigt)". Licht elke uitkomst toe in één zin.

### DPIA (artikel 35 AVG)

Alleen relevant als T1 ja of onduidelijk is.

**Nodig** als een van deze situaties geldt:
- systematische en uitgebreide beoordeling van mensen op basis van geautomatiseerde verwerking, met besluiten die rechtsgevolgen of vergelijkbaar grote gevolgen hebben (T5)
- grootschalige verwerking van bijzondere of strafrechtelijke gegevens (T2 en T4)
- stelselmatige en grootschalige monitoring van openbaar toegankelijke ruimten (T9)
- de verwerking valt onder de lijst van de Autoriteit Persoonsgegevens. Let op de voorwaarden: de meeste categorieën gelden bij **grootschalige verwerking en/of stelselmatige monitoring**, zoals fraudebestrijding, financiële gegevens, controle van werknemers, locatiegegevens, communicatiegegevens, cameratoezicht, biometrie en het geautomatiseerd observeren of beïnvloeden van gedrag; profilering valt eronder bij een systematische en uitgebreide beoordeling van persoonlijke aspecten; zonder schaaldrempel gelden onder meer heimelijk onderzoek, zwarte lijsten en samenwerkingsverbanden waarin overheden met andere partijen (bijzondere) persoonsgegevens uitwisselen. Twijfel je over de drempel, label dan "waarschijnlijk nodig"
- voor de Rijksoverheid: bij de ontwikkeling van beleid of regelgeving waaruit verwerkingen van persoonsgegevens voortvloeien, bij materieel cloudgebruik met persoonsgegevens (pre-scan DPIA plus DPIA, volgens het cloudbeleid; twijfel je of het gebruik materieel is, label dan "waarschijnlijk nodig" met een open punt voor het CIO-office), of als departementaal beleid een DPIA verplicht stelt

**Waarschijnlijk nodig** als twee of meer EDPB-criteria gelden. Het Model DPIA Rijksdienst noemt dit "waarschijnlijk verplicht"; in de praktijk betekent het dat de DPIA moet, tenzij de organisatie (de verwerkingsverantwoordelijke), na advies van de FG, schriftelijk onderbouwt dat er geen hoog risico is. Ook "waarschijnlijk nodig" bij één criterium in combinatie met onduidelijke antwoorden, en altijd als de verwerking raakt aan grote politiek-bestuurlijke of maatschappelijke vraagstukken.

**Nog onduidelijk** bij één EDPB-criterium zonder verdere aanwijzingen: dan beoordeelt de organisatie, na advies van de FG, of er een hoog risico is. Kan het criterium vervallen door minder gegevens te gebruiken (bijvoorbeeld een opmerkingenveld met gezondheidsinformatie schrappen), noem dat als eenvoudige maatregel.

**Niet nodig** als er geen persoonsgegevens zijn of duidelijk geen hoog risico. Het Model DPIA vraagt dan een schriftelijke, onderbouwde vastlegging van die afweging (bijvoorbeeld via de pre-scan); dat past bij de verantwoordingsplicht uit de AVG (artikel 5 lid 2). Lever die onderbouwing op.

De negen EDPB-criteria (WP248):
1. evalueren of scoren, inclusief profileren en voorspellen (T5)
2. geautomatiseerde besluiten met rechtsgevolg of vergelijkbaar gevolg (T5)
3. stelselmatige monitoring (T9)
4. gevoelige of zeer persoonlijke gegevens (T2)
5. grootschalige verwerking (T4)
6. koppelen of combineren van gegevensbestanden (T10)
7. kwetsbare betrokkenen (T3)
8. innovatief gebruik of nieuwe technologie (T11, vaak bij AI)
9. de verwerking verhindert mensen een recht uit te oefenen of een dienst of contract te krijgen (T5)

### IAMA en FRIA

Zie `iama-fria.md` voor de uitvoering.

**FRIA (artikel 27 AI Act)**: nodig voor de organisatie die het systeem inzet (de gebruiksverantwoordelijke) als beide gelden:
- het is (waarschijnlijk) een hoog-risico-AI-systeem uit bijlage III (T7), behalve kritieke infrastructuur, en
- de organisatie is een publiekrechtelijk orgaan of een private organisatie die openbare diensten verleent (bijvoorbeeld onderwijs, zorg, sociale huisvesting, taken in opdracht van de overheid), óf de toepassing gaat over kredietwaardigheid of over risico en prijs bij levens- en ziektekostenverzekeringen.
Label: "waarschijnlijk nodig (als de jurist hoog risico bevestigt)". Is "openbare dienst" twijfelachtig, label dan "nog onduidelijk". Vermeld op de kaart vanaf wanneer het wettelijk geldt: de FRIA is nodig vóór het eerste gebruik van een hoog-risicosysteem vanaf 2 december 2027; voor overheidsgebruik van een systeem dat al eerder in gebruik is, uiterlijk 2 augustus 2030 (zie de tijdlijn in `aanvullende-toetsen.md` A6). Voor een gewone private organisatie zonder openbare dienst: "niet nodig", met direct erbij welke plichten wel gelden (artikel 26, artikel 86 en de DPIA).

**IAMA**:
- Overheid met een impactvol algoritme of AI (directe rechtsgevolgen voor mensen, of het algoritme beïnvloedt hoe de overheid iemand indeelt): **waarschijnlijk nodig**. De IAMA is geen wettelijke plicht, maar wordt in de overheid sterk aanbevolen en is soms door de organisatie zelf verplicht gesteld. Vraag of er beleid is.
- Als de FRIA nodig is: adviseer de IAMA als manier om de FRIA uit te voeren.
- Overheid met AI of een algoritme zonder directe gevolgen voor mensen (bijvoorbeeld een interne schrijfassistent): **niet nodig**, wel aan te raden als het gebruik later impactvol wordt.
- Private organisatie zonder FRIA-plicht: noem de IAMA als bruikbaar vrijwillig instrument bij impactvolle algoritmes, zonder label.

### AI Act-classificatie en plichten

**Nodig** als T6 een AI-systeem (of "mogelijk AI") oplevert. Vermeld op de kaart:
- de vermoedelijke categorie: mogelijk verboden (T8), waarschijnlijk hoog risico (T7), transparantieplicht (T15) of minimaal risico
- de vermoedelijke rol: gebruiksverantwoordelijke of aanbieder (let op artikel 25, zie `aanvullende-toetsen.md` A4)
- bij waarschijnlijk hoog risico: een aparte rij "AI Act-plichten gebruiksverantwoordelijke" met de datum vanaf wanneer ze gelden
- als de organisatie (waarschijnlijk) ook aanbieder is, bijvoorbeeld omdat ze het model zelf heeft gebouwd: ook een rij "AI Act-plichten aanbieder" (zie A4), met dezelfde datum en de jurist als eigenaar
- altijd bij AI: AI-geletterdheid (artikel 4)

### Transparantie

Bepaal met `aanvullende-toetsen.md` onderdeel B welke plicht geldt:
- **Nodig** bij een chatbot of voicebot, een deepfake, emotieherkenning of biometrische categorisering, of AI-tekst die wordt gepubliceerd om het publiek te informeren over zaken van algemeen belang zonder menselijke redactie.
- **Niet nodig** onder artikel 50 bij interne teksten of brieven aan individuen; noem dan wel de informatieplicht uit de AVG en, bij overheden, de motiveringsplicht.
- **Nog onduidelijk** als het gebruik nog niet vaststaat.

### DTIA

**Waarschijnlijk nodig** als er een doorgifte is (T13, eerste punt) naar een land zonder adequaatheidsbesluit, of naar een Amerikaanse ontvanger die niet onder het EU-US Data Privacy Framework is gecertificeerd. **Nog onduidelijk** als niet bekend is waar subverwerkers en supportteams zitten. **Niet nodig** voor alleen buitenlandse zeggenschap zonder doorgifte; neem dat risico wel op in de DPIA en de cloudafweging.

### Cloud en soevereiniteit

- **Rijksoverheid en zbo's**: **nodig** bij materieel cloudgebruik (zie `aanvullende-toetsen.md` onderdeel D).
- **Andere overheden en private organisaties die een openbare dienst verlenen** (onderwijs, zorg, sociale huisvesting): **waarschijnlijk nodig** bij een nieuwe clouddienst voor een kerntaak of met grootschalige persoonsgegevens; het rijksbrede cloudbeleid is een goede leidraad (voor andere overheden wordt het geadviseerd).
- **Private organisaties**: **waarschijnlijk nodig** bij een nieuwe clouddienst voor een kritiek proces (T14), of als de organisatie onder de Cyberbeveiligingswet valt. Alleen buitenlandse zeggenschap zonder kritiek proces: geen apart assessment, wel meenemen als risico in de DPIA. Meestal geen wettelijke plicht, wel verstandig.
- **Voor iedereen**: gaat het om een bestaand, al beoordeeld platform (bijvoorbeeld een bestand op de bestaande Microsoft 365-omgeving), verwijs dan naar die eerdere afweging: **niet nodig** voor dit project.

### Informatiebeveiliging

- **Nodig** (BIV-classificatie en risicoanalyse) bij een nieuw systeem of een nieuwe leverancier met persoonsgegevens of voor een belangrijk proces (T12, T14), en altijd voor overheden (BIO2) en organisaties onder de Cyberbeveiligingswet.
- Bij een klein project met een gangbare leverancier: **waarschijnlijk nodig** in lichte vorm, namelijk een paar beveiligingsvragen aan de leverancier (certificering, versleuteling, toegang). Zie onderdeel E.

### Algoritmeregister (alleen overheid)

- Rijksoverheid: **nodig** als in de DPIA sprake is van AI of algoritmes (het Model DPIA Rijksdienst schrijft voor die na afronding van de DPIA op te nemen). Zonder DPIA: **waarschijnlijk nodig** bij impactvolle algoritmes.
- Andere overheden: **waarschijnlijk nodig** bij impactvolle algoritmes of hoog-risico-AI.
- Publieke instellingen zoals onderwijsinstellingen of zorginstellingen: **nog onduidelijk**; vraag naar eigen beleid of sectorafspraken.
- Bij hoog-risico-AI geldt voor overheden daarnaast de registratie in de EU-databank (artikel 26 lid 8 en 49 AI Act).

### Ondernemingsraad

Relevant zodra medewerkers betrokken zijn (T3 medewerkers, of medewerkers die met het systeem werken). Zie onderdeel F voor de regels.
- **Nodig** (instemming) als er een OR is en het gaat om een systeem dat geschikt is om aanwezigheid, gedrag of prestaties van personeel te volgen (ook via gebruikslogs per medewerker), of om een nieuwe of gewijzigde regeling over personeelsgegevens, personeelsbeoordeling, werving en selectie, of ziekteverzuim. Een gewoon teamrooster of een contactlijst valt hier meestal niet onder.
- **Waarschijnlijk nodig** (advies) bij een belangrijke nieuwe technologische voorziening.
- **Nog onduidelijk** als niet bekend is of er een OR is, of als nog niet duidelijk is of het systeem gebruik of prestaties per medewerker vastlegt.
- **Medezeggenschapsraad** (onderwijs, met personeel en studenten of ouders): dezelfde labels als de OR.

### Overige punten (alleen signaleren)

Archivering en Woo (overheid), digitale toegankelijkheid, verwerkersovereenkomst en exitafspraken. Zie onderdeel H.

## 4. De assessmentkaart en het tipsblok

Laat de uitkomst zien als tabel:

| Assessment | Uitkomst | Waarom (één zin) | Geldt wettelijk vanaf | Wie betrekken |
|---|---|---|---|---|
| DPIA | Nodig | Je verwerkt gezondheidsgegevens van veel inwoners. | Nu | FG of privacyjurist |
| AI Act-plichten gebruiksverantwoordelijke | Waarschijnlijk nodig (als hoog risico bevestigd) | De score helpt bepalen of iemand een uitkering krijgt. | 2 december 2027, voor de overheid uiterlijk 2 augustus 2030 bij bestaande systemen | AI-verantwoordelijke |

Toon alleen assessments die relevant zijn, of waarvan de gebruiker zou kunnen denken dat ze relevant zijn.

Zet onder de kaart een blok **Belangrijkste aandachtspunten voor de jurist** met hooguit drie punten die geen assessment zijn maar wel zwaar wegen, bijvoorbeeld een mogelijk verwerkingsverbod voor gezondheidsgegevens (artikel 9 AVG), mogelijk geautomatiseerde besluitvorming (artikel 22 AVG) of een twijfelachtige grondslag.

Direct na de kaart volgt het **tipsblok**: hooguit de vier collega's die nu het dringendst betrokken moeten worden, met per persoon één zin waarom (zie `stakeholders.md`). De overige rollen komen in de actielijst bij de oplevering.

Sluit af met: "Dit is een eerste inschatting op basis van jouw antwoorden. Je organisatie stelt, na advies van de jurist, FG of privacy officer, vast welke assessments echt nodig zijn." Lever daarbij de tussenstand mee (zie `SKILL.md`). Vraag daarna of de gebruiker klaar is om met de verdieping te beginnen, of, bij de lichte route, of de korte uitkomst volstaat.
