# Aanvullende toetsen

Laatst inhoudelijk gecontroleerd: 6 oktober 2026, tegen de brontekst van de AI Act (Verordening (EU) 2024/1689) zoals gewijzigd door de Digitale omnibus inzake AI (Verordening (EU) 2026/1744, in werking sinds 27 juli 2026) de Herziening rijksbreed cloudbeleid 2026 (3 juli 2026) en de BIO2 versie 1.3 (Staatscourant 2026, 7416). Overige punten (Cyberbeveiligingswet, WOR) op basis van openbare bronnen; laat die bij twijfel controleren.

Gebruik deze module in fase 3 voor de onderdelen die op de assessmentkaart staan. Stel ook hier één vraag tegelijk, in gewone taal. Je verzamelt feiten; de juridische conclusie is aan de jurist.

De vragen onder "Vragen" bij elk onderdeel zijn de [kern]-vragen: stel ze alleen als het antwoord nog niet bekend is uit eerdere blokken (zie `crosswalk.md`). Richtlijn: hooguit zes vragen per onderdeel, en samen niet meer dan het budget in `SKILL.md` regel 10. De achtergrondtekst gebruik je om uit te leggen en om de kaart te vullen, niet als vragenlijst.

## Inhoud

- A. AI Act: classificatie, rol, plichten en tijdlijn
- B. Transparantie bij AI
- C. DTIA (doorgifte buiten de EER)
- D. Cloud en soevereiniteit
- E. Informatiebeveiliging
- F. Ondernemingsraad
- G. Algoritmeregister en EU-databank
- H. Overige punten

## A. AI Act

### A1. Is het een AI-systeem?

Een AI-systeem is een op een machine gebaseerd systeem dat met enige autonomie werkt en uit de input die het krijgt afleidt hoe het output maakt, zoals voorspellingen, inhoud, aanbevelingen of beslissingen (artikel 3 punt 1). Een getraind model, een taalmodel of een chatbot valt daar meestal onder. Een vaste beslisboom of rekenregel die mensen volledig hebben uitgeschreven meestal niet; die valt wel onder de AVG en, bij de overheid, onder het Algoritmekader en eventueel de IAMA.

Vragen:
- Heeft het systeem geleerd van voorbeelden of gegevens, of volgt het alleen regels die jullie zelf hebben bedacht?
- Maakt het zelf teksten, samenvattingen, voorspellingen of aanbevelingen?

### A2. Verboden toepassingen (artikel 5)

Sinds 2 februari 2025 verboden:
- schadelijke manipulatie of misbruik van kwetsbaarheden (leeftijd, beperking, sociale of economische situatie)
- social scoring: mensen beoordelen op gedrag of persoonlijkheid, met nadelige gevolgen in een andere context of buiten verhouding
- voorspellen of iemand een strafbaar feit zal plegen, uitsluitend op basis van profilering of persoonlijkheidskenmerken
- gezichtsdatabanken opbouwen door ongericht beelden van internet of camerabeelden te verzamelen
- emotieherkenning op de werkplek of in het onderwijs, behalve om medische of veiligheidsredenen. Let op: het gaat om het afleiden van emoties of intenties **op basis van biometrische gegevens** (gezicht, stem, lichaamssignalen). Stress afleiden uit productiecijfers valt hier niet onder, een camera of wearable die gezichtsuitdrukking of hartslag analyseert wel
- biometrische categorisering om ras, politieke opvattingen, vakbondslidmaatschap, religie of seksuele geaardheid af te leiden
- realtime biometrische identificatie op afstand in openbare ruimten voor rechtshandhaving (met beperkte uitzonderingen)

Vanaf 2 december 2026 ook verboden (toegevoegd door de Digitale omnibus):
- realistische beelden, video's of audio maken of manipuleren van de intieme delen van een herkenbaar persoon, of van een herkenbaar persoon in seksuele handelingen, zonder diens uitdrukkelijke toestemming
- materiaal van seksueel kindermisbruik genereren of manipuleren

Let op de uitzonderingen: het verbod op emotieherkenning geldt niet bij medische of veiligheidsredenen, en niet buiten de werkplek en het onderwijs. Het meten van lichaamssignalen bij patiënten in de zorg valt er dus niet onder.

Vragen (alleen als het systeem in die buurt komt):
- Meet of analyseert het systeem lichaamskenmerken, zoals gezicht, stem, hartslag of bewegingen?
- Worden mensen beoordeeld op hun algemene gedrag, met gevolgen buiten de context waarin dat gedrag is waargenomen?

### A3. Hoog risico (artikel 6 en bijlage III)

Een AI-systeem is hoog risico als het bedoeld is voor een van deze gebruiksgevallen (bijlage III, samengevat; de jurist toetst aan de exacte tekst):

1. **Biometrie**: identificatie op afstand (niet: alleen verificatie dat iemand is wie hij zegt), categorisering op gevoelige kenmerken, emotieherkenning (voor zover niet verboden).
2. **Kritieke infrastructuur**: veiligheidscomponent bij digitale infrastructuur, wegverkeer, water, gas, warmte of elektriciteit.
3. **Onderwijs en beroepsopleiding**: toelating of toewijzing, beoordelen van leerresultaten, bepalen van het passende onderwijsniveau, toezicht op fraude bij toetsen.
4. **Werk en personeelsbeheer**: werven en selecteren (vacatures gericht plaatsen, sollicitaties filteren, kandidaten beoordelen); besluiten over arbeidsvoorwaarden, promotie of ontslag; taken toewijzen op basis van individueel gedrag of persoonlijke kenmerken; prestaties en gedrag monitoren en evalueren.
5. **Essentiële diensten**:
   - (a) systemen die door of namens overheidsinstanties worden gebruikt om te beoordelen of mensen in aanmerking komen voor essentiële overheidsuitkeringen en -diensten (inclusief zorg), of om die te verlenen, te beperken, in te trekken of terug te vorderen
   - (b) kredietwaardigheid of kredietscore van personen (niet: opsporen van financiële fraude)
   - (c) risicobeoordeling en prijsstelling bij levens- en ziektekostenverzekeringen
   - (d) noodoproepen beoordelen, hulpdiensten prioriteren, triage van patiënten die dringend zorg nodig hebben
6. **Rechtshandhaving** (door of namens rechtshandhavingsinstanties), 7. **migratie, asiel en grenstoezicht**, 8. **rechtspraak en verkiezingen**.

**Uitzonderingen (artikel 6 lid 3).** Een systeem uit bijlage III is toch geen hoog risico als het geen significant risico vormt en het de uitkomst van de besluitvorming niet wezenlijk beïnvloedt, en het alleen: (a) een beperkte procedurele taak uitvoert, (b) het resultaat van eerder voltooid menselijk werk verbetert, (c) afwijkingen van eerdere besluitpatronen opspoort zonder de menselijke beoordeling te vervangen, of (d) een voorbereidende taak uitvoert.

Let op: deze uitzondering beoordeelt de **aanbieder**. Hij moet die beoordeling vastleggen vóór het systeem op de markt komt, en het systeem registreren in de EU-databank (artikel 6 lid 4 en artikel 49 lid 2). Een gebruiksverantwoordelijke kan zich er niet zelf op beroepen. Vraag de leverancier om die documentatie; ontbreekt die, dan is het een open punt voor de jurist.

**Profileringsregel.** Valt het systeem onder een gebruiksgeval van bijlage III en profileert het personen (het beoordeelt of voorspelt persoonlijke aspecten, zoals gedrag, betrouwbaarheid, prestaties of situatie), dan gelden de uitzonderingen niet: het blijft hoog risico. Eerst moet dus vaststaan dat het systeem onder een gebruiksgeval valt.

Voorbeeld: een systeem dat bijstandsaanvragen alleen samenvat, kan een voorbereidende taak zijn. Een systeem dat per aanvrager een score geeft die bepaalt wie extra onderzoek krijgt, kan onder punt 5(a) vallen en profileert dan. Of de score "beoordeelt of iemand in aanmerking komt" is een juridische vraag. Formuleer het daarom als "waarschijnlijk hoog risico" en vraag de jurist het vast te stellen.

Vragen:
- Wat doet het systeem precies met de output? Wie gebruikt die en waarvoor?
- Heeft de output invloed op wie iets krijgt, wie gecontroleerd wordt of wat er met iemand gebeurt?
- Geeft het systeem een score, rangorde of voorspelling per persoon?

### A4. Welke rol heeft de organisatie? (artikel 25)

- **Gebruiksverantwoordelijke**: de organisatie gebruikt een AI-systeem onder eigen verantwoordelijkheid. De meeste organisaties die AI inkopen, zijn dat.
- **Aanbieder**: de organisatie ontwikkelt het systeem of brengt het onder eigen naam op de markt.

Een gebruiksverantwoordelijke wordt zelf aanbieder van een hoog-risicosysteem, met veel zwaardere plichten, als zij:
- (a) haar eigen naam of merk zet op een hoog-risicosysteem
- (b) een hoog-risicosysteem ingrijpend wijzigt
- (c) het beoogde doel van een AI-systeem (ook een algemeen systeem zoals een chatbot of taalmodel) zo wijzigt dat het een hoog-risicosysteem wordt

Wordt de organisatie (ook) aanbieder van een hoog-risicosysteem, dan gelden onder meer: een systeem voor risicobeheer en kwaliteitsbeheer, eisen aan data en datagovernance, technische documentatie en logging, transparantie en een gebruiksaanwijzing, menselijk toezicht in het ontwerp, nauwkeurigheid en cyberbeveiliging, een conformiteitsbeoordeling met CE-markering, registratie in de EU-databank en monitoring na het in gebruik nemen (artikel 16 en verder). Dat is werk voor de jurist en de ontwikkelaars; noteer het als belangrijk aandachtspunt.

Vragen:
- Gebruik je het systeem voor het doel dat de leverancier opgeeft, of voor iets anders?
- Laat je het systeem aanpassen of bijtrainen op eigen gegevens?
- Komt het systeem onder jullie eigen naam naar buiten?

Bij een "ja": belangrijk aandachtspunt voor de jurist.

### A5. Plichten van de gebruiksverantwoordelijke bij hoog risico

Deze plichten gelden ook als er geen FRIA nodig is (artikel 26 en 86):
- passende maatregelen om het systeem te gebruiken volgens de gebruiksaanwijzing van de aanbieder (lid 1)
- menselijk toezicht door mensen met de nodige bekwaamheid, opleiding, autoriteit en ondersteuning (lid 2)
- voor zover de organisatie de invoergegevens beheert: zorgen dat die relevant en voldoende representatief zijn (lid 4)
- de werking monitoren; bij een risico het gebruik onderbreken en de aanbieder en de markttoezichthouder informeren; ernstige incidenten direct melden (lid 5)
- automatisch gegenereerde logs bewaren, voor zover de organisatie die beheert, gedurende een passende periode en minimaal zes maanden, tenzij ander recht (zoals de AVG) iets anders bepaalt (lid 6)
- als werkgever: vóór de ingebruikname werknemersvertegenwoordigers en de betrokken werknemers informeren (lid 7)
- overheidsinstanties: registratie van het gebruik in de EU-databank (artikel 49 lid 3); staat het systeem daar niet in, dan het systeem niet gebruiken en de aanbieder of distributeur informeren (lid 8)
- de informatie van de aanbieder gebruiken voor de DPIA (lid 9)
- mensen over wie het systeem beslissingen neemt of helpt nemen, informeren dat het systeem op hen wordt toegepast (lid 11)
- recht op uitleg (artikel 86): wie getroffen wordt door een besluit op basis van de output van een hoog-risicosysteem uit bijlage III (behalve kritieke infrastructuur), met rechtsgevolgen of vergelijkbaar aanzienlijke nadelige gevolgen, heeft recht op een duidelijke uitleg over de rol van het systeem en de belangrijkste elementen van het besluit

### A6. Tijdlijn

- Verboden (artikel 5): sinds 2 februari 2025; de twee nieuwe verboden vanaf 2 december 2026.
- AI-geletterdheid (artikel 4): sinds 2 februari 2025; sinds 27 juli 2026 in de lichtere vorm zoals gewijzigd door de Digitale omnibus.
- Transparantie (artikel 50): sinds 2 augustus 2026; markering van synthetische content (lid 2) voor systemen die al vóór 2 augustus 2026 op de markt waren: uiterlijk 2 december 2026.
- Hoog risico uit bijlage III: vanaf **2 december 2027**. Hoog risico in producten uit bijlage I: vanaf 2 augustus 2028.
- **Overgangsrecht (artikel 111 lid 2)**: voor hoog-risicosystemen die vóór die datum in de handel of in gebruik zijn, gelden de regels pas als het ontwerp daarna aanzienlijk wijzigt. Volgens de toelichting bij de Digitale omnibus (overweging 39) kijk je daarbij naar het **type en model**: is één exemplaar van dat type en model vóór de datum rechtmatig op de markt gebracht, dan geldt het overgangsrecht ook voor latere exemplaren van hetzelfde type en model, zolang het ontwerp niet aanzienlijk wijzigt. Dit raakt vooral SaaS-diensten die al op de markt zijn.
- **Uitzondering voor de overheid**: aanbieders en gebruiksverantwoordelijken van hoog-risicosystemen die bedoeld zijn voor gebruik door overheidsinstanties, moeten in ieder geval uiterlijk **2 augustus 2030** voldoen.

Hoe je dit uitlegt aan de gebruiker:
- Overheid: "Vanaf 2 december 2027 voor nieuwe systemen, en uiterlijk 2 augustus 2030 ook voor systemen die je nu al gebruikt."
- Private organisatie: "Vanaf 2 december 2027 voor nieuwe systemen. Voor een systeem dat al vóór die datum op de markt is, kan overgangsrecht gelden. Of dat hier zo is, beoordeelt de jurist."
- Altijd: "Wacht niet. Als er een DPIA nodig is, geldt die plicht nu al, en een goede voorbereiding voorkomt dat je in 2027 moet ombouwen."

### A7. AI-geletterdheid (artikel 4)

Aanbieders en gebruiksverantwoordelijken nemen maatregelen om de ontwikkeling van AI-geletterdheid te ondersteunen bij hun personeel en anderen die namens hen AI gebruiken, rekening houdend met kennis, ervaring en de context. Er hoeft geen bepaald niveau gegarandeerd te worden, maar de maatregelen moeten er aantoonbaar zijn. Geldt bij elk AI-gebruik, ook bij minimaal risico.

Vraag: hoe zorg je dat de medewerkers die met dit systeem werken weten wat het kan, wat het niet kan en wanneer ze het moeten negeren?

### A8. Bias toetsen met gevoelige gegevens (artikel 4 bis)

Wie wil controleren of een systeem bepaalde groepen benadeelt, heeft daarvoor soms gevoelige gegevens nodig, zoals afkomst. De Digitale omnibus staat dat bij uitzondering toe, als het strikt noodzakelijk is en met strenge waarborgen (onder meer: het kan niet met andere of synthetische gegevens, pseudonimisering, strikte toegang, niet delen, verwijderen zodra het klaar is, en vastlegging van de reden in het register van verwerkingen):
- voor aanbieders van hoog-risicosystemen (lid 1)
- voor gebruiksverantwoordelijken van hoog-risicosystemen, en voor aanbieders en gebruiksverantwoordelijken van andere AI-systemen, als de mogelijke bias waarschijnlijk gevolgen heeft voor gezondheid, veiligheid of grondrechten, of tot verboden discriminatie leidt (lid 2)
Het is een mogelijkheid, geen plicht, en de AVG blijft daarnaast gelden. Signaleer dit als aandachtspunt voor de jurist zodra de gebruiker groepen wil vergelijken.

## B. Transparantie bij AI

Bepaal eerst wie welke plicht heeft. Artikel 50 maakt onderscheid tussen aanbieder en gebruiksverantwoordelijke.

| Situatie | Wie | Plicht |
|---|---|---|
| Een systeem dat direct met mensen praat (chatbot, voicebot) | Aanbieder | Het systeem zo ontwerpen dat mensen weten dat ze met AI praten, tenzij dat duidelijk is (lid 1). Als gebruiksverantwoordelijke: controleer dat het zo is ingesteld. |
| Systeem dat synthetische tekst, beeld, audio of video maakt | Aanbieder | Output machineleesbaar markeren als kunstmatig (lid 2). |
| Emotieherkenning of biometrische categorisering (voor zover toegestaan) | Gebruiksverantwoordelijke | De mensen die eraan worden blootgesteld informeren (lid 3). |
| Deepfake: beeld, audio of video die echt lijkt | Gebruiksverantwoordelijke | Bekendmaken dat het kunstmatig is (lid 4). |
| AI-tekst die wordt **gepubliceerd** om het publiek te informeren over zaken van algemeen belang | Gebruiksverantwoordelijke | Bekendmaken dat de tekst door AI is gemaakt, tenzij een mens de tekst heeft gecontroleerd en iemand redactionele verantwoordelijkheid draagt (lid 4). |

De informatie moet uiterlijk bij het eerste contact duidelijk worden gegeven en toegankelijk zijn (lid 5).

Let op: **brieven of e-mails aan individuele burgers of klanten** vallen niet onder lid 4. Daar gelden wel andere regels: de informatieplicht uit de AVG (artikel 13 en 14, inclusief informatie over geautomatiseerde besluitvorming), bij hoog-risico-AI artikel 26 lid 11, en voor overheden de beginselen van behoorlijk bestuur, zoals een deugdelijke motivering. Signaleer dat een mens de inhoud van zo'n brief moet controleren.

## C. DTIA (doorgifte buiten de EER)

Een DTIA is nodig bij een doorgifte van persoonsgegevens naar een land buiten de EER waarvoor geen adequaatheidsbesluit geldt, als de doorgifte gebeurt op basis van bijvoorbeeld standaardcontractbepalingen.

Wat telt als doorgifte:
- de gegevens worden opgeslagen of verwerkt buiten de EER
- iemand buiten de EER kan de gegevens inzien of bewerken, bijvoorbeeld een helpdesk of ontwikkelteam op afstand
- een subverwerker buiten de EER krijgt toegang

Wat geen doorgifte is, maar wel een risico:
- de leverancier valt onder buitenlands recht (bijvoorbeeld een Amerikaans moederbedrijf) terwijl de gegevens in de EU staan. Neem dit op in de DPIA en de cloudafweging (onderdeel D).

Voor Amerikaanse ontvangers: is de ontvanger gecertificeerd onder het EU-US Data Privacy Framework, dan is er een adequaatheidsbesluit en is een DTIA voor die doorgifte niet nodig. Laat de jurist de actuele status van het kader en de certificering van de ontvanger controleren.

Vragen:
- In welke landen worden de gegevens opgeslagen, verwerkt of bekeken, ook door subverwerkers en supportteams?
- Op welke basis gebeurt de doorgifte? (Adequaatheidsbesluit, Data Privacy Framework, standaardcontractbepalingen.)
- Welke aanvullende maatregelen zijn er, zoals versleuteling waarbij de sleutel in Europa blijft?

De DTIA zelf volgt meestal de stappen van de EDPB-aanbevelingen over aanvullende maatregelen: doorgiften in kaart brengen, de basis bepalen, het recht en de praktijk in het ontvangende land beoordelen, aanvullende maatregelen kiezen, de formele stappen zetten en periodiek opnieuw beoordelen. Dat is werk voor de jurist; jij verzamelt de feiten.

## D. Cloud en soevereiniteit

### D1. Rijksoverheid (en zbo's)

Bron: Herziening rijksbreed cloudbeleid, 3 juli 2026. Het beleid geldt voor de hele rijksdienst behalve de Hoge Colleges van Staat en Defensie; zbo's worden geacht het te volgen; andere overheden wordt het geadviseerd.

Het geldt voor publieke, hybride, community en private cloud van een externe leverancier, en voor SaaS die op een publieke of gedeelde infrastructuur van een niet-overheidspartij draait.

**Materieel cloudgebruik** is gebruik voor de primaire of kerntaak, voor belangrijke ondersteunende processen, of voor grootschalige verwerking van persoonsgegevens. Dan is nodig:
- een integrale risicoanalyse op basis van de classificatie (BIV of TBB), die naast beveiliging, continuïteit en privacy ook ingaat op: de leverancier en onderaannemers, het type cloud, de regio van opslag en verwerking, de rol van de leverancier in beveiliging en continuïteit, controle- en auditmogelijkheden, inmenging door een buitenlandse overheid, en misbruik van leveranciersafhankelijkheid
- een pre-scan DPIA en DPIA bij persoonsgegevens; een DTIA bij doorgifte naar een land zonder adequaatheidsbesluit
- een gedocumenteerd en zelf getoetst exitplan met twee scenario's (geplande exit en plotselinge uitval), inclusief vernietiging van data bij de leverancier; jaarlijks te herzien
- een melding aan CISO Rijk vóór de implementatie, bij voorkeur met risicoanalyse en exitplan
- formele acceptatie van het restrisico door de verantwoordelijke bestuurder; maatregelen die van de leverancier afhangen, in het contract

Harde punten:
- opslag en verwerking binnen de EER en Zwitserland
- versleuteling bij opslag en verzending (behalve openbare data); bij vertrouwelijke gegevens sleutelbeheer bij voorkeur in eigen beheer of bij een gecertificeerde derde
- e-mail en documenten niet in de publieke cloud, tenzij onafhankelijk is vastgesteld dat de continuïteit anders in gevaar komt, risicoanalyse en exitplan getoetst zijn en de minister in overeenstemming met de bewindspersoon voor digitalisering heeft ingestemd
- brondata van basisregistraties niet in de publieke cloud
- staatsgeheime informatie en TBB-niveau 1, 2 en 3: nooit in de publieke cloud
- bijzondere persoonsgegevens bij voorkeur niet in de publieke cloud; anders met extra maatregelen zoals privacybevorderende technieken
- leveranciers uit landen met een actief cyberprogramma gericht tegen Nederlandse belangen zijn uitgesloten (C2000-criteria); bij dreiging van statelijke actoren advies inwinnen bij AIVD of MIVD
- voor vitale aanbieders, organisaties onder de Wet weerbaarheid kritieke entiteiten en essentiële entiteiten onder de Cyberbeveiligingswet wordt afgeraden voor het primaire proces een leverancier te gebruiken die (deels) onder niet-Europese jurisdictie valt
Overgangstermijn voor bestaand gebruik: vier jaar (of de langere looptijd van een bestaand contract); voor het exitplan twaalf maanden.

### D2. Andere organisaties

Het rijksbrede beleid is geen plicht, maar wel een goede leidraad. Het EU Cloud Sovereignty Framework helpt bij het beoordelen van het risico op buitenlandse inmenging bij leverancierskeuze. De Data Act geeft sinds 12 september 2025 rechten om over te stappen naar een andere clouddienst; laat de jurist nagaan wat dit betekent voor lopende contracten. Het rijksbrede cloudbeleid vraagt de overstapafspraken bij bestaande contracten expliciet op te nemen.

### D3. Vragen

- Hoe belangrijk is de dienst voor je kerntaak? Wat gebeurt er als hij een week uitvalt?
- In welke landen staan en worden de gegevens verwerkt? Onder welk recht valt de leverancier?
- Wie beheert de versleutelingssleutels?
- Hoe kom je eraf als het moet? Kun je je gegevens in een bruikbaar formaat terugkrijgen, en hoe lang duurt dat?
- Wat doe je als de dienst morgen plotseling stopt?
- Hoe afhankelijk ben je al van deze leverancier voor andere diensten?

## E. Informatiebeveiliging

- **BIV-classificatie**: hoe belangrijk zijn beschikbaarheid, integriteit en vertrouwelijkheid? Dit bepaalt de maatregelen.
- **Overheid**: de BIO2 is het normenkader, gebaseerd op ISO 27001 en 27002. Geldend is versie 1.3 van 9 januari 2026, voor het Rijk vastgesteld met de circulaire in de Staatscourant van 5 maart 2026 (nr. 7416). De BIO2 werkt risicogestuurd: de drie basisbeveiligingsniveaus (BBN's) van de oude BIO zijn vervallen. Volgens de circulaire verwijst de ministeriële regeling bij de Cyberbeveiligingswet voor de zorgplicht rechtstreeks naar deze versie. Vraag de CISO welke eisen voor deze toepassing gelden.
- **Cyberbeveiligingswet** (van kracht sinds 15 augustus 2026): essentiële en belangrijke entiteiten moeten zich registreren, passende maatregelen nemen voor risicobeheer, significante incidenten melden en hun bestuur verantwoordelijk maken. Vraag of de organisatie hieronder valt; zo ja, dan is de leverancier onderdeel van de toeleveringsketen die beoordeeld moet worden.

Vragen:
- Is er een BIV-classificatie of risicoanalyse voor dit systeem?
- Welke beveiligingseisen stel je aan de leverancier, en hoe controleer je die (bijvoorbeeld certificering of auditrapporten)?
- Wie wordt gewaarschuwd bij een incident, en hoe snel?

## F. Ondernemingsraad

- Een OR is verplicht in ondernemingen met 50 of meer medewerkers. Vraag of er een OR of personeelsvertegenwoordiging is.
- **Instemmingsrecht** (artikel 27 lid 1 WOR) bij een voorgenomen besluit over onder meer:
  - sub d: regelingen over arbeidsomstandigheden, ziekteverzuim of re-integratie
  - sub e: aanstellings-, ontslag- of bevorderingsbeleid (relevant bij AI in werving en selectie)
  - sub g: personeelsbeoordeling
  - sub k: het verwerken en beschermen van persoonsgegevens van medewerkers
  - sub l: voorzieningen die geschikt zijn om aanwezigheid, gedrag of prestaties van medewerkers waar te nemen of te controleren
- De instemming moet vóór het besluit worden gevraagd. Neemt de bestuurder het besluit zonder instemming, dan kan de OR binnen een maand de nietigheid inroepen.
- Regelt een cao het onderwerp al inhoudelijk, dan vervalt het instemmingsrecht voor dat deel. Vraag of de cao het echt inhoudelijk regelt.
- Weigert de OR instemming, dan kan de bestuurder de kantonrechter om vervangende toestemming vragen (artikel 27 lid 4 WOR).
- **Adviesrecht** (artikel 25 lid 1 sub k WOR) bij de invoering of wijziging van een belangrijke technologische voorziening.
- Ook een pilot of proef kan onder het instemmingsrecht vallen, en heeft ook een DPIA nodig.
- Instemming van de OR is geen grondslag onder de AVG. De grondslag moet apart worden bepaald.
- Bij hoog-risico-AI op de werkplek: werknemers en hun vertegenwoordigers vooraf informeren (artikel 26 lid 7 AI Act).
- Vergeet uitzendkrachten en ingehuurd personeel niet.
- In het onderwijs heeft de medezeggenschapsraad (met personeel en studenten of ouders) vergelijkbare rechten; vraag ernaar.

Vragen:
- Wanneer dien je het instemmingsverzoek in? Vóór een eventuele pilot?
- Werken er uitzendkrachten of ingehuurde mensen mee, en hoe worden zij geïnformeerd?
- Deel je de DPIA met de OR?
- Regelt de cao iets over monitoring of personeelsgegevens? (Alleen als dat nog niet bekend is uit DPIA onderdeel 9.)

## G. Algoritmeregister en EU-databank

- **Algoritmeregister** (algoritmes.overheid.nl): openbaar overzicht van algoritmes van de overheid. Voor de Rijksoverheid hoort een algoritme of AI uit een DPIA er na de DPIA in. Vraag welke gegevens de organisatie daarvoor moet aanleveren, bijvoorbeeld: naam en doel van het algoritme, het proces waarin het wordt gebruikt, de rol van de mens, de gebruikte gegevens, de risico's en maatregelen, en een contactpunt.
- **EU-databank** (artikel 49 en 71 AI Act): aanbieders registreren hoog-risicosystemen; overheden registreren als gebruiksverantwoordelijke hun gebruik (artikel 49 lid 3). Vraag of de leverancier het systeem al heeft geregistreerd.

Vragen:
- Staat dit algoritme of een vergelijkbaar algoritme al in het register?
- Wie in de organisatie beheert de registratie?

## H. Overige punten

Signaleer deze kort en verwijs naar de juiste collega (`stakeholders.md`):
- **Sectorregels**: in sommige sectoren gelden extra regels die de jurist moet meenemen, zoals in de financiële sector (onder meer DORA voor digitale weerbaarheid en het toezicht van DNB en AFM) en in de zorg (onder meer de regels voor medische hulpmiddelen). Vraag of er sectorregels gelden.
- **Verwerkersovereenkomst** (artikel 28 AVG): afspraken over doel, beveiliging, subverwerkers, locatie, bijstand bij rechten van betrokkenen, en wat er met de gegevens gebeurt aan het eind.
- **Archivering** (overheid): de selectielijst bepaalt bewaren en vernietigen.
- **Woo** (overheid): actieve openbaarmaking; het cloudbeleid gaat uit van openbaarmaking van relevante besluitvorming.
- **Digitale toegankelijkheid**: verplicht voor overheden; voor veel producten en diensten van bedrijven sinds 28 juni 2025 door de European Accessibility Act.
