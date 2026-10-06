# Wijzigingen

## 1.0.1 (oktober 2026)

- Afbeelding "zo werkt het" in de README: gebruik, technische werking, aanpassen per organisatie en privacy.
- Privacysectie in de README: de assistent draait in de eigen AI-omgeving; niets gaat naar de maker of andere organisaties.
- Kant-en-klare zip bij elke release, en een installatie in één regel voor Claude Code.
- Alle referentiebestanden vermelden nu wanneer en waartegen ze zijn gecontroleerd.
- Promptversie ingekort tot ruim onder de 8.000 tekens, zodat er ruimte is voor correcties.
- Automatische controle (`scripts/controleer.py`) bij elke pull request.
- Issueformulieren voor inhoudelijke fouten en verbeteringen.
- Exitplan: "getoetst" in plaats van "getest", zoals in het rijksbrede cloudbeleid.
- Pseudonimisering genuanceerd na het arrest EDPS/SRB (C-413/23 P, 4 september 2025).
- Directe link naar het Model DPIA Rijksdienst van augustus 2026.

## 1.0.0 (oktober 2026)

Eerste publieke versie.

**Modules**
- Triage met 16 vragen, beslisregels, assessmentkaart met datum vanaf wanneer plichten gelden, en een vast tipsblok.
- DPIA volgens de 17 onderdelen van het Model DPIA Rijksdienst (augustus 2026).
- IAMA en FRIA volgens de IAMA versie 2 (februari 2026) en artikel 27 AI Act, met de zes FRIA-onderdelen.
- Aanvullende toetsen: AI Act (definitie, verboden, hoog risico, profileringsregel, rol, plichten, tijdlijn, AI-geletterdheid, biastoetsing), transparantie, DTIA, cloud en soevereiniteit (rijksbreed cloudbeleid 2026), informatiebeveiliging, ondernemingsraad en overige punten.
- Koppeltabel tussen DPIA, IAMA en FRIA, zodat niets dubbel gevraagd wordt.
- Doorvraagregels, begrippenlijst, stakeholdertips, uploadregels en uitvoerformats, ook voor een eigen format en een eigen risicomatrix.
- Promptversie voor platforms zonder skills.
- Tien testcasussen met verwachte uitkomst.

**Gecontroleerd tegen de brontekst** van de AI Act, de Digitale omnibus inzake AI (Verordening (EU) 2026/1744), het Model DPIA Rijksdienst, de IAMA en de Herziening rijksbreed cloudbeleid 2026.

**Verbeterd na meerdere testrondes** met gesimuleerde gesprekken (onder meer een gemeente met een AI-score voor bijstand en een werkgever met productiviteitsmonitoring), onder meer:
- AI Act: hoog risico pas vaststellen na toetsing aan het gebruiksgeval; profileringsregel juist toegepast; onderscheid tussen algoritme met vaste regels en AI-systeem; functies van één systeem apart beoordeeld; emotieherkenning alleen verboden op basis van biometrische gegevens; rol als aanbieder (artikel 25 a, b en c); plichten van de gebruiksverantwoordelijke (artikel 26 en 86) met de juiste voorwaarden; overgangsrecht per type en model.
- Transparantie: artikel 50 per rol uitgewerkt; brieven aan individuen vallen er niet onder.
- Doorgifte (DTIA) en buitenlandse zeggenschap uit elkaar gehaald.
- Grondslag bij werkgevers: arbeidsovereenkomst alleen waar echt nodig, gerechtvaardigd belang voor monitoring; OR-instemming is geen AVG-grondslag.
- Route voor organisaties zonder FG.
- Eenduidige regels voor doorvragen, "weet ik niet", berichtopbouw en het moment van stakeholdertips.
- Uploads met persoonsgegevens: melding in een apart bericht, vandaag nog naar de FG.

## Gepland

- Feedback van juristen en FG's verwerken via GitHub-issues.
- Bijwerken zodra het AI Office het model voor de FRIA publiceert.
