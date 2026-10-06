# Wie moet meekijken?

Laatst inhoudelijk gecontroleerd: 6 oktober 2026, tegen de AVG, de AI Act zoals gewijzigd door de Digitale omnibus, de WOR en de Herziening rijksbreed cloudbeleid 2026.

Veel risico's kan de gebruiker niet alleen beoordelen. Een goede tip op het juiste moment voorkomt dat het project later vastloopt. Geef een tip zodra een antwoord een van de signalen hieronder bevat. Wacht dus niet tot het eind.

## Hoe je een tip geeft

Er zijn drie vaste momenten (zie `SKILL.md` regel 8): het tipsblok direct na de assessmentkaart, de samenvatting na elk verdiepingsblok, en de actielijst in de oplevering. Daarbuiten alleen een tip als iets dringend is, hooguit één per bericht. In het tipsblok mag je meerdere collega's noemen, elk met één zin.

Rijen gemarkeerd met "(overheid)" gelden alleen voor overheidsorganisaties.

Houd het kort en praktisch, in deze vorm:

> **Tip: betrek [rol].** [Eén zin waarom.] Je kunt bijvoorbeeld vragen: "[concrete vraag]". Dit is het handigst [moment].

Voeg de tip ook toe aan de actielijst voor fase 5. Geef dezelfde tip niet twee keer. Gebruik de namen of afdelingen uit `organisatie/organisatieprofiel.md` als die zijn ingevuld.

Rollen heten per organisatie anders. Als de gebruiker een rol niet herkent, beschrijf wat die persoon doet en vraag wie dat in de eigen organisatie is.

## Signalen en rollen

| Signaal | Rol | Waarom | Voorbeeldvraag aan die persoon | Moment |
|---|---|---|---|---|
| Persoonsgegevens met een mogelijk hoog risico | FG of privacyjurist | Adviseert over de DPIA en beoordeelt de grondslag. | "Moeten we hiervoor een volledige DPIA doen, en welk format gebruiken we?" | Zo vroeg mogelijk, na de triage |
| Clouddienst of SaaS | CIO-office, enterprise-architect | Beoordeelt of de dienst past in het cloudbeleid en de architectuur, en wat de afhankelijkheid is. | "Past deze dienst in ons cloudbeleid, en is er een exitplan nodig?" | Voor de keuze van leverancier |
| Leverancier met moederbedrijf of toegang buiten Europa | FG of jurist, architect | Mogelijk DTIA nodig; risico op toegang door buitenlandse overheden. | "Is er een doorgiftetoets nodig, en welke maatregelen verlagen het risico?" | Voor contractering |
| Kritiek proces of gevoelige gegevens | CISO of security officer | BIV-classificatie, risicoanalyse en beveiligingseisen (BIO2, Cyberbeveiligingswet). | "Welke BIV-classificatie hoort hierbij, en welke beveiligingseisen stellen we aan de leverancier?" | Voor het opstellen van de eisen |
| Afhankelijkheid van één leverancier, lange contractduur, kernproces | CIO, architect, inkoop | Soevereiniteit en vendor lock-in; het rijksbrede cloudbeleid (2026) vraagt bij materieel cloudgebruik een door de organisatie zelf getoetst exitplan. | "Kunnen we overstappen of terugvallen als deze dienst stopt of de voorwaarden veranderen?" | Bij de business case |
| AI of algoritme dat mensen beoordeelt | Algoritmeverantwoordelijke of AI-officer, data scientist | Risicoclassificatie onder de AI Act en biastoetsing; voor overheden ook IAMA en registratie in het algoritmeregister. | "Valt dit onder hoog risico in de AI Act, en hoe toetsen we op bias?" | Voor de ontwikkeling of aanschaf |
| Gegevens van medewerkers, monitoring van personeel | Ondernemingsraad, HR | Instemmingsrecht bij systemen die aanwezigheid, gedrag of prestaties kunnen volgen en bij regelingen over personeelsgegevens; adviesrecht bij belangrijke nieuwe technologie. Bij hoog-risico-AI op de werkplek ook een informatieplicht uit de AI Act. | "Wanneer leggen we dit ter instemming of advies voor, en hoe informeren we de medewerkers?" | Voor de invoering, ruim op tijd |
| Gezondheid, verzuim, werkdruk | Bedrijfsarts of arbodienst, preventiemedewerker | Gezondheidsgegevens van medewerkers horen in principe alleen bij de bedrijfsarts; monitoring kan de werkdruk verhogen. | "Mogen wij deze gegevens als werkgever zien, en wat doet dit met de werkdruk?" | Bij het ontwerp |
| Uitzendkrachten of ingehuurd personeel | HR, inkoop, uitzendbureau | Wie is verantwoordelijk voor hun gegevens, en weten zij ervan? | "Welke afspraken maken we met het uitzendbureau over deze gegevens?" | Voor de invoering |
| Uitkeringen, zorg, jeugd of andere kwetsbare cliënten | Cliëntenraad of adviesraad sociaal domein | Betrokkenen of hun vertegenwoordigers laten meedenken verbetert het ontwerp en het draagvlak. | "Herkennen jullie de risico's, en wat zou het voor cliënten makkelijker maken?" | Bij het ontwerp |
| Medisch hulpmiddel of zorgtoepassing | Medische technologie, regulatory affairs, klinisch verantwoordelijke | Productregels voor medische hulpmiddelen en klinische veiligheid. | "Is dit een medisch hulpmiddel met CE-markering, en wie is daarvoor verantwoordelijk?" | Voor de aanschaf |
| Financiële sector | Compliance, risk management | Sectorregels zoals DORA en toezicht van DNB en AFM. | "Welke sectorregels en toezichtseisen gelden hiervoor?" | Bij de business case |
| Onderwijsinstelling | Medezeggenschapsraad (personeel en studenten of ouders) | Heeft in het onderwijs vergelijkbare rechten als een OR. | "Wanneer leggen we dit voor aan de medezeggenschapsraad?" | Voor de invoering |
| Nieuwe werkwijze voor medewerkers | Proceseigenaar of teamleider van de eindgebruikers | Zij weten hoe het in de praktijk gaat en of menselijk toezicht echt haalbaar is. | "Hebben medewerkers tijd en ruimte om van het advies van het systeem af te wijken?" | Bij het ontwerp |
| Gevolgen voor burgers of klanten | Communicatie, klantcontact, eventueel een burger- of cliëntenpanel | Uitleg aan betrokkenen, transparantie, bezwaarmogelijkheden, draagvlak. | "Hoe leggen we dit begrijpelijk uit, en waar kunnen mensen terecht met vragen?" | Bij het ontwerp |
| Contract, verwerkersovereenkomst, subverwerkers | Inkoop of contractmanager | Afspraken over gegevens, locatie, beveiliging en exit moeten in het contract. | "Staan locatie, subverwerkers, bewaartermijnen en exitbepalingen in het contract?" | Tijdens de aanbesteding |
| Bewaren, vernietigen, archiveren (overheid) | DIV, informatiebeheerder of archivaris | Archiefplicht en selectielijsten bepalen bewaartermijnen. | "Welke bewaartermijn hoort bij deze gegevens volgens de selectielijst?" | Bij het ontwerp |
| Openbaarheid (overheid) | Woo-coördinator | Documenten en algoritmes kunnen openbaar gemaakt moeten worden. | "Wat moeten we hierover actief openbaar maken?" | Voor de invoering |
| Chatbot of AI-gegenereerde content naar buiten | Communicatie, jurist | Transparantieplichten uit artikel 50 AI Act. | "Hoe maken we duidelijk dat dit door AI gemaakt is of dat men met AI praat?" | Bij het ontwerp |
| Digitale dienst voor burgers of klanten | Toegankelijkheidsexpert | Digitale toegankelijkheid (voor overheden verplicht, voor veel bedrijven sinds 28 juni 2025 door de European Accessibility Act). | "Is de dienst toegankelijk voor mensen met een beperking?" | Bij het ontwerp |
| Grote investering of structurele kosten | Controller, budgethouder | Maatregelen zoals exit, beveiliging en training kosten geld. | "Is er budget voor de benodigde maatregelen?" | Bij de business case |

## Toon

Breng tips als hulp, niet als extra drempel. Bijvoorbeeld: "Goed om te weten: als je de CISO nu al betrekt, voorkom je dat de beveiligingseisen later het contract ophouden."
