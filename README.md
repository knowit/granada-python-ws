# Granada python workshop

Workshopen er for å lære Python. Vi kikker på de tingene som er generelt nyttig for å kunne
lage enkle scripts og applikasjoner, i all hovedsak syntaks, datastrukturer og fil IO. Vi
har med vilje unngått mye bruk av 'kule' rammeverk for å fokusere mest mulig på selve språket.

## Investering i Bitcoins,  gull og AAPL-aksjer

Vedlagt i data-mappen finnes det noen data-sett som er lastet ned fra http://www.quandl.com/.

Settene er verdien av bitcoins, apple-aksjer og gull over tid. Vi ser på hvor rike vi hadde
vært om vi hadde investert gull i bitcoins eller apple-aksjer helt i starten.

## Avhengigheter
Koden er skrevet for python3.

NB! på OS X måtte jeg installere freetype og libagg før matplotlib ville bygge:

    brew install freetype libagg

Installer avhengigheter:

    pip install -r requirements.txt

## Oppgaver

Oppgavene består i å implementere skjelettene til funksjonene som er oppgitt i *.py-filene.
For hver fil finnes det også en test_$fil som inneholder enhetstester som kan hjelpe å sjekke
om oppgaven er løst. Disse testene kan kjøres med py.test-kommandoen -- enten alle i prosjektet:

$ py.test

Eller en spesifikk test-modul:

$ py.test test_data.py

Eller en spesifikk testcase:

$ py.test -k test_group_data_by_date_should_yield_defaultdict

### data.py - Hente ut strukturert data fra CSV-filer

Oppgavene i data.py skal hjelpe oss å lære litt om IO og en del syntaks og datastrukturer i Python.
Vi skal lese inn csv-filene i data-mappen og legge dataen inn i fornuftige datastrukturer som vi
lett kan jobbe med. I tillegg ser vi litt på noen nyttige moduler fra standardbiblioteket.

I starten av modulen er det dokumentert hva slags strukturer og konsepter man jobber med.

Koden som er gitt er et skjelett som mangler implementasjoner og noen datatype-definisjoner som
gjenbrukes i andre moduler. namedtuples er verdityper som er immutable og har 'dumme' konstruktører,
første del av oppgaven er å skrive smarte konstruktører som ta initialisere datatypene fra
csv-records (en linje plaintext).

Andre hoveddel av denne modulen er å hente ut datapunkter fra datafilene. Dette deles opp i
IO, parsing av CSV og massering av data for å få det på riktig format (verditypene i modulen).
Vi er nødt til å massere dataen fordi settene har forskjellig format, blant annet er ikke alle
datoer gitt i alle filene (det viser seg at gull er eldre enn bitcoin).

### statistics.py - Transformasjon av data til noe som kan plottes

Oppgaven i denne modulen er å transformere datasettet vi har jobbet med til ting som kan
plottes. Output herfra skal benyttes til å visualisere dataen. Formatet på output herfra
er er liste av: (x, y0, y1, yn)

Resultatplottet her vil inneholde n linjer.

### simpleplot.py - plotting med matplotlib (ferdig)

Denne modulen er ferdig implementert. Den implementerer en plot()-funksjon som kan benyttes
for å lage matplotlib-plots av lister av (x, y0, y1, yn)-tuppler og den kan lage PNG-filer
som kan hostes med HTTP.

### webapp.py - minimalist webapp som viser plots

webapp.py er en enkel webapp som hoster plots av dataen. Den benytter webrammeverket flask,
men all web-koden er implementert allerede. Her bindes modulene sammen ved at man serverer
png-plots av dataen man har regnet ut i statistics.py. Ved å kjøre modulen som et python-script
vil man få opp en lokal applikasjon som kan brukes for å se på resultatet:

$ python webapp.py

Du kan gå til http://localhost:5000 i nettleseren for å se på webappen. Dersom noe feiler
vil denne sette deg i en interaktiv debugger for webappen.