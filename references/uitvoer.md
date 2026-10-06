# Uitvoer

Laatst inhoudelijk gecontroleerd: 6 oktober 2026, tegen artikel 35 lid 7 en artikel 36 AVG en de indeling van het Model DPIA Rijksdienst (augustus 2026).

In fase 5 lever je vijf onderdelen op. Schrijf in gewone taal, behalve waar een juridische term nodig is. Zet **één keer**, bovenaan de hele oplevering:

> Concept, opgesteld met hulp van een AI-assistent op [datum]. Dit is geen juridisch oordeel. Laat het beoordelen door [de beoordelaar uit fase 0, bijvoorbeeld de FG of privacyjurist].

Lever je in delen, herhaal de disclaimer dan kort bovenaan elk deel.

## 1. Assessmentkaart

De tabel uit `triage.md`, bijgewerkt met wat in de verdieping duidelijk is geworden, inclusief de kolom "Geldt wettelijk vanaf" en, bij AI, de rij "AI Act-plichten gebruiksverantwoordelijke".

## 2. Concept per assessment

### Welk format?

1. **Eigen format van de organisatie.** Heeft de gebruiker een leeg format geupload of de hoofdstukken genoemd, of is `organisatie/eigen-format.md` ingevuld: gebruik die structuur. Zet elk antwoord onder het best passende hoofdstuk. Wat nergens past, komt onder "Overige informatie". Hoofdstukken zonder antwoorden laat je staan met "Nog in te vullen" en een verwijzing naar het open punt.
   Let daarbij op:
   - **Ontbrekende verplichte onderdelen.** Een DPIA moet volgens artikel 35 lid 7 AVG ten minste bevatten: een beschrijving van de verwerking en de doeleinden, een beoordeling van noodzaak en evenredigheid, een beoordeling van de risico's voor betrokkenen, en de maatregelen. Ontbreekt er een, voeg een extra hoofdstuk toe en meld dit als aandachtspunt.
   - **Andere risicoschaal.** Gebruikt het format een andere schaal of matrix (bijvoorbeeld kans keer impact van 1 tot 5, met kleurdrempels), scoor dan in fase 4 meteen op die schaal. Was het format toen nog niet bekend, gebruik dan deze vaste omzetting voor zowel het risico als het restrisico: laag = 2, gemiddeld = 3, hoog = 4. Reken het eindniveau uit volgens de drempels van het format en vermeld de omzetting. De hoogste kleur of categorie van het format geldt als "hoog" voor de vraag of de Autoriteit Persoonsgegevens vooraf geraadpleegd moet worden (artikel 36 AVG); laat de jurist dat bevestigen.
   - **Risico's voor de organisatie.** Vraagt het format ook naar risico's voor de organisatie (reputatie, boetes, kosten), houd die gescheiden van de risico's voor betrokkenen. Een DPIA gaat in de kern over de mensen van wie de gegevens zijn.
2. **Geen eigen format.** Gebruik de indelingen hieronder. De DPIA-indeling volgt het Model DPIA Rijksdienst en is ook bruikbaar voor niet-overheden.

### DPIA (Model DPIA Rijksdienst)

```
DPIA [naam project], concept [datum]

Deel A. Beschrijving
 1. Voorstel
 2. Persoonsgegevens (tabel: categorie betrokkenen | gegevens | soort | bron)
 3. Gegevensverwerkingen (inclusief tekstversie van het stroomschema)
 4. Technieken en methoden
 5. Doeleinden
 6. Betrokken partijen (tabel: partij | rol | toegang tot welke gegevens)
 7. Belangen
 8. Verwerkingslocaties
 9. Juridisch en beleidsmatig kader
10. Bewaartermijnen (tabel: gegevens | termijn | onderbouwing)

Deel B. Rechtmatigheid
11. Rechtsgrond
12. Bijzondere persoonsgegevens
13. Doelbinding
14. Noodzaak en evenredigheid
15. Rechten van betrokkenen

Deel C. Risico's
16. Risico's (tabel: nr | risico voor betrokkene | oorzaak | geraakt grondrecht (bij AI of algoritmes) | kans | ernst | niveau)
    Niveau bij de standaardschaal (kans x ernst): hoog als beide hoog zijn, of als de ernst hoog is en de kans gemiddeld; laag als beide laag zijn, of als één laag en de ander gemiddeld is; in alle andere gevallen gemiddeld. Hetzelfde geldt voor het restrisico.

Deel D. Maatregelen
17. Maatregelen (tabel: risico nr | maatregel | type | eigenaar | restrisico)
```

Markeer in deel B elke juridische inschatting als "Aandachtspunt voor de jurist", niet als conclusie.

### IAMA (voorbereiding voor de teamsessie)

```
IAMA [naam project], voorbereiding [datum]

Deel 1. Waarom?      1.1 Aanleiding en doel | 1.2 Publieke waarden | 1.3 Grondslag | 1.4 Verantwoordelijkheden
Deel 2. Wat?         2.1 Type | 2.2 Totstandkoming | 2.3 Inzet | 2.4 Kwaliteit | 2.5 Datagovernance
Deel 3. Hoe?         3.1 Gebruikscontext | 3.2 Rol medewerker | 3.3 Communicatie | 3.4 Monitoring | 3.5 Impact
Deel 4. Grondrechten Agenda: mogelijk geraakte grondrechten per cluster, uitzoekvragen voor de jurist
Deel 5. Afsluiting   Agenda: argumenten voor en tegen, openstaande keuzes, mogelijke restrisico's
```

Verwijs met "zie DPIA onderdeel x" waar de koppeltabel overlap toont, in plaats van tekst te herhalen. Zet bij deel 4 en 5 duidelijk: "Voorbereiding voor de teamsessie, geen conclusie." Sluit af met een blok **Teamsessie**: voorgestelde deelnemers (projectleider, data scientist, jurist en anderen), aantal sessies, en de [team]-vragen als agenda per deel.

### FRIA (artikel 27 lid 1)

Een tabel met de zes onderdelen (a) tot en met (f), met per onderdeel het antwoord of een verwijzing naar de plek in de DPIA of IAMA, en een kolom "informatie of gebruiksaanwijzing van de aanbieder ontvangen: ja / nee / gedeeltelijk". Voeg toe: de geplande datum van eerste gebruik, en de stap "resultaten melden aan de markttoezichthouder".

### Aanvullende toetsen

Per toets op de kaart een korte notitie: de verzamelde feiten, de aandachtspunten, de open vragen en wie het oppakt. Bijvoorbeeld voor cloud: locatie, jurisdictie, sleutelbeheer, exitmogelijkheden en de vereiste stappen (voor de Rijksoverheid: risicoanalyse, exitplan, melding CISO Rijk).

## 3. Open punten

| Nr | Open punt | Waarom nodig | Wie weet het | Hoort bij |
|---|---|---|---|---|

## 4. Actielijst

Alle tips en acties uit het gesprek, gebundeld. Zet eventuele meldingen bovenaan, zoals een geuploade file met persoonsgegevens die aan de FG gemeld moet worden.

| Wie | Wat vragen of doen | Wanneer |
|---|---|---|

## 5. Samenvatting voor de beslisser

Maximaal één pagina:
- wat we gaan doen en waarom (twee of drie zinnen)
- welke assessments nodig zijn, hoe ver ze zijn, en vanaf wanneer welke plichten gelden
- de belangrijkste risico's, met het restrisico na maatregelen
- wat er nog moet gebeuren voordat besloten kan worden
- de grootste onzekerheid, eerlijk benoemd

## Vorm

Lever gestructureerde tekst met kopjes en tabellen (Markdown), zodat de gebruiker het makkelijk naar Word of een ander systeem kan kopiëren. Lever standaard per onderdeel, in deze volgorde, zodat niets wordt afgekapt: eerst de kaart, de samenvatting voor de beslisser, de open punten en de actielijst (samen kort), daarna de concepten per assessment. Zo heeft de gebruiker het belangrijkste direct.
