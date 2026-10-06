# DPIA: vragen per onderdeel

Laatst inhoudelijk gecontroleerd: 6 oktober 2026, tegen de brontekst van het Model DPIA Rijksdienst (augustus 2026).

Deze module volgt de 17 onderdelen van het **Model DPIA Rijksdienst** (versie op kcbr.nl, augustus 2026). Die indeling is ook bruikbaar voor gemeenten, andere overheden en private organisaties, omdat ze de eisen van artikel 35 lid 7 AVG volgt. Gebruikt de organisatie een eigen format, dan stel je dezelfde vragen en zet je de antwoorden in fase 5 in hun structuur (zie `uitvoer.md`).

## Inhoud

- Werkwijze
- Deel A. Beschrijving (onderdelen 1 tot en met 10)
- Deel B. Rechtmatigheid (onderdelen 11 tot en met 15)
- Deel C. Risico's (onderdeel 16)
- Deel D. Maatregelen (onderdeel 17)
- Voorbeelden uit openbare bronnen

## Werkwijze

- De onderdelen 1 tot en met 10 overlappen met de gedeelde basis uit fase 3. Vraag niets opnieuw wat al beantwoord is; bevestig het alleen.
- Per onderdeel staan hieronder: wat het model vraagt, de vragen in gewone taal, waar je op doorvraagt, en een voorbeeld van een goed antwoord.
- Deel B is juridisch. Hier vraag je de gebruiker vooral naar feiten (welke wet, welke taak, welke afspraken). De juridische afweging laat je over aan de jurist. Formuleer je bevindingen als "aandachtspunt voor de jurist".
- Na elk deel: samenvatten en laten bevestigen.

## Deel A. Beschrijving van de verwerking

### 1. Voorstel

Wat het model vraagt: een beschrijving van het voorstel, de aanleiding, wie erbij betrokken zijn, hoe privacy vanaf het ontwerp is meegenomen, en wat er verandert ten opzichte van de huidige situatie.

Vragen:
- Wat ga je doen, in twee of drie zinnen?
- Wat is de aanleiding? Welk probleem los je op?
- Wat verandert er ten opzichte van hoe het nu gaat?
- Heb je bij het ontwerp al nagedacht over het beschermen van gegevens? Bijvoorbeeld: minder gegevens gebruiken, standaardinstellingen zo privacyvriendelijk mogelijk.

Doorvragen bij: een beschrijving die alleen over techniek gaat ("we implementeren tool X"). Vraag dan naar het doel en de mensen die erdoor geraakt worden.

Voorbeeld goed antwoord: "We willen inkomende brieven van inwoners automatisch laten samenvatten door een AI-dienst, zodat medewerkers sneller kunnen reageren. Nu leest een medewerker elke brief volledig. De samenvatting is een hulpmiddel; de medewerker leest de brief zelf als de samenvatting onduidelijk is."

### 2. Persoonsgegevens

Wat het model vraagt: alle soorten persoonsgegevens per categorie (gewoon, gevoelig, bijzonder, strafrechtelijk, BSN), de bron, en of het gaat om kwetsbare groepen.

Vragen:
- Over welke groepen mensen gaat het? (Bijvoorbeeld inwoners, klanten, medewerkers, sollicitanten.)
- Welke gegevens gebruik je per groep? Noem soorten gegevens, geen echte gegevens.
- Waar komen de gegevens vandaan? Van de persoon zelf, uit een eigen systeem, van een andere organisatie, of maakt het systeem ze zelf (zoals een score of samenvatting)?

Doorvragen bij: "klantgegevens", "basisgegevens", "alleen wat nodig is", "geen gevoelige gegevens" (vraag of er vrije tekstvelden zijn; daarin staat vaak onverwacht gevoelige informatie). Vergeet afgeleide gegevens niet: een risicoscore of AI-samenvatting is ook een persoonsgegeven.

Voorbeeld goed antwoord: "Inwoners: naam, adres, e-mailadres, de inhoud van hun brief. In brieven staat soms informatie over gezondheid of financiële problemen. Medewerkers: naam en gebruikersaccount, en logbestanden van wie welke samenvatting heeft opgevraagd."

### 3. Gegevensverwerkingen

Wat het model vraagt: welke handelingen er met de gegevens gebeuren, welke gegevens per handeling, liefst met een stroomschema.

Vragen:
- Loop het proces eens met mij door, van begin tot eind. Wat gebeurt er eerst, en dan?
- Welke gegevens worden bij elke stap gebruikt?
- Waar worden ze opgeslagen, gedeeld of verwijderd?

Tip voor de gebruiker: een simpel stroomschema met vakjes (invoer, verwerking, uitvoer) is genoeg. Bied aan om op basis van de antwoorden een tekstversie van zo'n schema te maken.

### 4. Technieken en methoden

Wat het model vraagt: of er sprake is van (deels) geautomatiseerde besluitvorming, profilering, cloud, big data, AI of algoritmes, en nieuwe technologie. Ook aandacht voor vooringenomenheid in trainingsdata en diagnostische gegevens (telemetrie) bij cloudleveranciers.

Vragen:
- Gebruik je een clouddienst, AI of een algoritme? Welk product precies?
- Beslist het systeem zelf iets, of geeft het een advies aan een mens?
- Verzamelt de leverancier zelf ook gegevens over het gebruik, zoals logbestanden of diagnostische gegevens? (Weet de gebruiker het niet: open punt voor de leverancier of de architect.)

Doorvragen bij AI: waarop is het systeem getraind, kan het fouten maken over personen, en controleert een mens de uitkomst?

### 5. Doeleinden

Wat het model vraagt: de doelen van elke verwerking.

Vragen:
- Waarvoor heb je deze gegevens precies nodig?
- Zijn er nog andere doelen, ook later? (Bijvoorbeeld statistiek, verbetering van het systeem, training van AI.)

Doorvragen bij: vage doelen zoals "efficiëntie", "dienstverlening verbeteren" of "voor de zekerheid". Vraag wat er concreet beter wordt en voor wie. Vraag expliciet of de leverancier de gegevens voor eigen doelen gebruikt, zoals het trainen van modellen.

### 6. Betrokken partijen

Wat het model vraagt: alle partijen en hun rol (verwerkingsverantwoordelijke, gezamenlijk verwerkingsverantwoordelijke, verwerker, subverwerker, ontvanger), en welke medewerkers toegang hebben tot welke gegevens.

Vragen:
- Welke organisaties zijn betrokken? Denk aan leveranciers, hostingpartijen en partners.
- Wie bepaalt het doel en de middelen? (Meestal je eigen organisatie.)
- Is er een verwerkersovereenkomst met de leverancier?
- Welke medewerkers of teams kunnen bij de gegevens?

Leg de rollen uit met `uitleg-begrippen.md` als de gebruiker ze niet kent. Doorvragen bij "iedereen in het team kan erbij": is dat nodig?

### 7. Belangen

Wat het model vraagt: de belangen van alle partijen, inclusief de betrokkenen zelf. Liefst is ook de mening van betrokkenen of hun vertegenwoordigers gevraagd.

Vragen:
- Wat levert dit op voor je organisatie?
- Wat levert het op voor de mensen van wie de gegevens zijn?
- Heb je hen of hun vertegenwoordigers gevraagd wat zij ervan vinden? (Bijvoorbeeld een cliëntenraad, burgerpanel of de ondernemingsraad.) Zo nee: is dat mogelijk?

### 8. Verwerkingslocaties

Wat het model vraagt: in welke landen de gegevens worden verwerkt, en bij doorgifte buiten de EER op welke basis en met welke aanvullende maatregelen.

Vragen:
- In welk land of welke landen staan de gegevens?
- Kan iemand van buiten Europa erbij, bijvoorbeeld een helpdesk of ontwikkelteam van de leverancier?
- Waar is het moederbedrijf van de leverancier gevestigd?

Houd twee dingen uit elkaar (zie `aanvullende-toetsen.md` C en D): een **doorgifte** (gegevens gaan naar buiten de EER of worden van daaruit bekeken) kan een DTIA vereisen; **buitenlandse zeggenschap** (een leverancier onder niet-Europees recht, ook met opslag in Europa) is geen doorgifte maar wel een risico voor onderdeel 16 en de cloudafweging. Bij twijfel: open punt voor de jurist en de architect.

### 9. Juridisch en beleidsmatig kader

Wat het model vraagt: relevante wet- en regelgeving en beleid, naast de AVG.

Vragen:
- Is er een wet of regeling die deze taak of dit proces beschrijft? (Bijvoorbeeld de Participatiewet, Wet maatschappelijke ondersteuning, een cao of een sectorspecifieke wet.)
- Zijn er interne beleidsregels die gelden, zoals een AI-beleid, cloudbeleid of informatiebeveiligingsbeleid?

Als de gebruiker het niet weet: open punt voor de jurist. Raad niet.

### 10. Bewaartermijnen

Wat het model vraagt: de bewaartermijn per doel, de onderbouwing, en hoe vernietiging of archivering geregeld is.

Vragen:
- Hoe lang bewaar je de gegevens, en waarom zo lang?
- Hoe lang bewaart de leverancier de gegevens, inclusief logbestanden en back-ups?
- Wie zorgt dat gegevens op tijd verwijderd worden?

Doorvragen bij: "zo lang als nodig", "dat regelt het systeem". Vraag naar een concrete termijn. Voor overheden: wijs op de selectielijst en de archivaris.

## Deel B. Rechtmatigheid

Laat de gebruiker weten dat dit deel juridischer is, en dat jij vooral feiten verzamelt die de jurist nodig heeft.

Kernvragen voor dit deel (stel de rest alleen als het ertoe doet): de taak, wet of overeenkomst waarop de verwerking steunt (11); bij gevoelige gegevens welke wet of uitzondering wordt gebruikt (12); welke minder ingrijpende alternatieven zijn bekeken (14); en hoe mensen hun rechten kunnen uitoefenen en bezwaar kunnen maken (15). Dat zijn samen ongeveer vijf vragen.

### 11. Rechtsgrond

Wat het model vraagt: de grondslag uit artikel 6 AVG per verwerking, en hoe aan de voorwaarden wordt voldaan.

Vragen in gewone taal:
- Doe je dit omdat een wet het verplicht of omdat het een publieke taak is? Welke wet of taak?
- Of is het nodig voor een overeenkomst met de persoon (bijvoorbeeld een klantcontract of arbeidsovereenkomst)?
- Of vraag je toestemming? (Zie doorvragen.)
- Of gaat het om een eigen belang van de organisatie (alleen voor private organisaties)?

Doorvragen bij "toestemming": een overheid of werkgever kan meestal niet op toestemming steunen, omdat mensen niet echt vrij zijn om nee te zeggen. Markeer dit als aandachtspunt voor de jurist en help de gebruiker vervolgens de juiste route te vinden (zie de rij "Met toestemming" in `doorvragen.md`). Bij "gerechtvaardigd belang" door een overheidsorganisatie voor haar publieke taak: aandachtspunt, want die grondslag is daarvoor niet beschikbaar.

Voor private organisaties die zich op gerechtvaardigd belang beroepen, vraag je de drie stappen uit: welk belang precies, waarom de verwerking daarvoor echt nodig is, en waarom dat belang zwaarder weegt dan de privacy van de betrokkenen. Vraag ook hoe betrokkenen bezwaar kunnen maken.

### 12. Bijzondere persoonsgegevens

Alleen als T2 ja is. Vraag welke uitzondering op het verbod geldt en of het BSN gebruikt mag worden op grond van een wet. De gebruiker weet dit vaak niet; verzamel wat bekend is en markeer het voor de jurist.

### 13. Doelbinding

Alleen als gegevens hergebruikt worden voor een ander doel (T10). Vraag waarvoor de gegevens oorspronkelijk verzameld zijn, en hoe het nieuwe doel daarmee samenhangt. Markeer voor de jurist.

### 14. Noodzaak en evenredigheid

Wat het model vraagt: is de verwerking evenredig met het doel (proportionaliteit), en kan het doel ook met minder ingrijpende middelen bereikt worden (subsidiariteit)?

Vragen:
- Kun je hetzelfde doel bereiken met minder gegevens, of zonder gegevens over personen?
- Is er een minder ingrijpende manier? (Bijvoorbeeld pseudonimiseren, alleen een steekproef, een andere tool.)
- Waarom is deze aanpak de beste?

Doorvragen bij: "dit is de enige manier". Vraag welke alternatieven bekeken zijn en waarom ze afvielen. Dit is vaak het zwakste deel van een DPIA, en juist hier vragen toezichthouders naar.

### 15. Rechten van betrokkenen

Vragen:
- Hoe kunnen mensen hun gegevens inzien, laten corrigeren of laten verwijderen?
- Hoe informeer je mensen over deze verwerking? (Bijvoorbeeld een privacyverklaring.)
- Kan iemand bezwaar maken tegen een beslissing en om menselijke tussenkomst vragen?

## Deel C. Risico's (onderdeel 16)

Volg fase 4 uit `SKILL.md`. Beschrijf elk risico als gevolg voor een mens, met de oorzaak, de kans en de ernst (laag, gemiddeld, hoog).

Voorbeelden van risico's om op te letten:
- Onjuiste gegevens of uitkomsten over een persoon (bijvoorbeeld een AI die verkeerde informatie over iemand genereert)
- Discriminatie of ongelijke behandeling van groepen, ook via indirecte kenmerken
- Te veel mensen hebben toegang, of gegevens lekken
- Gegevens worden langer bewaard dan nodig, of door de leverancier voor eigen doelen gebruikt
- Toegang door buitenlandse overheden via de leverancier
- Mensen weten niet dat hun gegevens zo gebruikt worden en kunnen zich niet verweren
- Afhankelijkheid van één leverancier, waardoor je niet meer kunt overstappen
- Function creep: de toepassing wordt later voor andere doelen gebruikt
- Een "chilling effect": mensen gedragen zich anders omdat ze zich bekeken voelen

## Deel D. Maatregelen (onderdeel 17)

Per risico: welke technische, organisatorische of juridische maatregel helpt, wie is verantwoordelijk, en welk restrisico blijft over (laag, gemiddeld, hoog).

Voorbeelden van maatregelen:
- Technisch: versleuteling, pseudonimisering, toegangsbeheer op basis van rollen, logging, gegevens automatisch verwijderen, privacyvriendelijke standaardinstellingen, diagnostische gegevens uitzetten
- Organisatorisch: werkinstructies, training en AI-geletterdheid, menselijke controle op uitkomsten, periodieke evaluatie, een gebruiksbeleid voor AI
- Juridisch: verwerkersovereenkomst, afspraken over locatie en subverwerkers, exitafspraken, informatie aan betrokkenen

Restrisico hoog na maatregelen? Dan moet de organisatie de Autoriteit Persoonsgegevens vooraf raadplegen (artikel 36 AVG). Signaleer dit duidelijk voor de FG.

## Voorbeelden uit openbare bronnen

Gebruik deze voorbeelden om de gebruiker te laten zien waarom bepaalde vragen ertoe doen. Vat ze kort samen en noem de bron. Gebruik ze niet als bewijs dat een vergelijkbaar project wel of niet mag.

**Microsoft 365 Copilot (DPIA van SLM Rijk en SURF).** In december 2024 vonden de onderzoekers vier hoge privacyrisico's. Na verbeteringen door Microsoft bleven er in september 2025 nog twee middelgrote risico's over: Copilot kan onjuiste of onvolledige persoonsgegevens genereren, en door een bewaartermijn van 18 maanden voor bepaalde gegevens is heridentificatie niet helemaal uit te sluiten. Organisaties moeten zelf nog maatregelen nemen, zoals een AI-gebruiksbeleid, kwaliteitscontrole en een eigen aanvullende DPIA. Les: ook bij een bekende leverancier met een algemene DPIA blijft een eigen DPIA nodig, en "onjuiste output over personen" is een echt privacyrisico.

**Controle uitwonendenbeurs DUO.** DUO selecteerde studenten voor controle met een risicoprofiel op basis van kenmerken zoals opleidingstype, afstand tot het ouderlijk huis en leeftijd. Studenten met een migratieachtergrond werden daardoor onevenredig vaak gecontroleerd. De Autoriteit Persoonsgegevens oordeelde dat de werkwijze discriminerend en onrechtmatig was. Les: ook als je geen afkomst gebruikt, kunnen andere kenmerken indirect tot discriminatie leiden. Vraag daarom altijd door op selectiecriteria en toets de uitkomsten per groep.

**Slimme Check bijstand, gemeente Amsterdam.** Amsterdam ontwikkelde een model om bijstandsaanvragen te selecteren voor extra onderzoek en besteedde veel aandacht aan eerlijkheid. In de praktijk bleef het model toch bepaalde groepen ongelijk behandelen, en de gemeente stopte de pilot. Les: goede bedoelingen en technische maatregelen zijn niet genoeg; test in de praktijk, meet per groep, en houd een exitstrategie achter de hand.

**Monitoring van magazijnmedewerkers bij Amazon France Logistique (Frankrijk).** De Franse toezichthouder CNIL legde in december 2023 een boete van 32 miljoen euro op, onder meer omdat via handscanners zeer gedetailleerd werd bijgehouden hoe snel en hoe lang medewerkers werkten en stilstonden. In december 2025 verlaagde de Raad van State (Conseil d'État) de boete in hoger beroep naar 15 miljoen euro, maar bleef het oordeel dat de monitoring te ver ging grotendeels in stand. Les: ook als metingen een bedrijfsdoel hebben, moet de mate van detail in verhouding staan tot dat doel. Vraag bij productiviteitsmetingen altijd door op het detailniveau, wie de gegevens ziet en hoe lang ze bewaard worden.

Bronnen: Model DPIA Rijksdienst (kcbr.nl); berichtgeving over de CNIL-boete en de uitspraak van de Conseil d'État (23 december 2025); berichtgeving over de Copilot-DPIA door Binnenlands Bestuur (2025); Kamerbrieven over de controle uitwonendenbeurs (2023) en het oordeel van de AP; MIT Technology Review (juni 2025) over de Slimme Check.
