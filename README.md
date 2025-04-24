# Haavard Bratlie | Portefølje | Kuben VGS

## Innholdsfortegnelse

- Om prosjektet

- Hvordan klone prosjektet

- Hva som trengs for å kjøre prosjektet

- Hvordan kjøre prosjektet

- Hvordan Navigere nettstedet

- Hvordan spille quiz

## OM prosjektet
Dette prosjektet er en portefølje-nettside som presenterer meg og mine interesser. Nettsiden inneholder en forside, en ***Om meg***-side, samt to interaktive ***quizer*** – én som handler om mine faglige ferdigheter og IT-interesser, og én om fritidsaktiviteter som filmer og spill. Brukere kan registrere seg og logge inn for å lagre quizresultater. Nederst på siden finnes kontaktinformasjon og en lenke for å laste ned CV-en min.

**Verktøy og språk**

 - HTML
 - CSS
 - Python / Flask
 - JavaScript
 - MySql
 - MariaDB
 - Photoshop
 - Adobe XD
 - Git / Github



## Hvordan Klone prosjektet

_Denne Brukerveiledningen går ut ifra at du har en github konto_

### Steg 1: Velg hvor du vil ha prosjektet

Naviger til en mappe du ønsker å plasere prosjektet i

Eks:
> C:\Users\Haavard Bratlie\OneDrive - Osloskolen\IM vg2\prosjekt

### Steg 2: Find lenke for repository
Åpne en nettleser og gå til
> https://github.com/HaavardBratlie/aarsoppgave

På denne siden skal det være en grønn knapp hvor det står "**Code**" <br>
Trykk på knappen og deretter på de to firkantene ved siden av url-en for å kopiere lenken

### Steg 3: Last ned git

Åpne nettleser og gå til
> https://git-scm.com/

Last ned git for windows og fullfør alle stegene i installeringen

### Steg 4: Åpne Terminal via mappe

Åpne mappen du ønsker å bruke til proskektet

Trykk på navigasjonsfeltet å skriv inn 
> cmd

Et terminalvindu burde åpne

Sjekk om Git er installert ved å skrive
```console
git --version
```

### Steg 5: Klon prosjektet

Bruk git clone komandoen etterfulgt med lenker du kopierte fra github til å klone prosjektet til din mappe

```console
git clone https://github.com/HaavardBratlie/aarsoppgave.git
```

Nå er Prosjektet klonet

## Hva som trengs for å kjøre 

_Denne brukerveiledningen går ut ifra at du har klonet prosjektet fra github og har Visual Studio Code_

### Steg 1: Åpne prosjektet

Gå til mappen hvor prosjektet ligger

Trykk på navigasjonsfeltet å skriv in 
```console
cmd
```

Dette burde åpne en terminal

I terminalen skriver du
```console
code .
```

Dette burde åpne prosjektet i Visual studio code

### Steg 2: Installer flask

Øverst i VS Code er det en navigasjonsfelt med flere drop down menyer

Trykk på **Terminal** deretter **New Terminal**

Da burde det komme opp en terminal i bunden av VS Code

i terminalen skriver du

```console
pip install flask
```

### Steg 3: Innstaller mySql.connector
I terminalen skriver du

```console
pip install mysql-connector-python
```

### Steg 4: Innstaller bcrypt
I terminalen skriver du
```console
pip install bcrypt
```

Nå er Prosjektet klar for bruk

## Hvordan kjøre prosjektet
_Denne brukerveiledningen går ut ifra at du har fullført alle punktene over_

_Hvis du lurer på hvordan man åpner VS Code kan du se steg 1 av **"Hva som trengs til å kjøre"**._


## Hvordan navigere nettstedet
Når man åpner siden kommer man til hjemmesiden. Der er det en header med linker for **_Innhold_**, **_Logg inn_** og **_Registrer_**.

På innhold siden er det en meny som har 4 knapper, **_Om meg_**, **_Spill Quiz_**, **_Github_** og **_Tabell_**. <br>

- Om meg inneholder litt tekst som handler om meg
- Spill quiz er en link til siden hvor man velger hvilken quiz man vil spille. <sub>_Må logge in for å spille quizen_</sub>
- Github er en link til github kontoen min
- Tabell er oversikten over resultater i quizen.

## Hvordan spille quiz

> _min.ip.adresse_ :2200/quiz_hub

Naviger til denne siden via innhold, så trykk på **_Spill quiz_**.

Deretter velger du den quizen du vil spille

Når quizen starter får du opp spørsmål øverst på siden

Det kommer fire alternativer der et er korrekt

Du velger et av alternativene ved å klikke på det

Svaret ditt lagres automatisk og en oppsumering av quizen kommer når quizen er fullført

Du kan deretter gå til Tabellen via innhold siden for å finne resultatet hvis du kom på top 10