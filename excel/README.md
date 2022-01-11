---
layout: default
title: Excel
nav_order: 2
has_children: true
---
[HOME](../README.md)
# Excel

## Excel funktioner
Excel har over 300 indbyggede funktioner, nogle af dem kender du sikkert, f.eks. **SUM**

Microsoft har oprette en oversigt, sorteret efter kategorien, over funktionerne.
[Excel funktioner efter kategori](https://support.office.com/da-dk/article/excel-funktioner-efter-kategori-5f91f4e9-7b42-46d2-9bd1-63f26a86c0eb)

Du har også mulighed for at finde funktionerne alfabetisk
[Excel funktioner alfabetisk](https://support.office.com/da-dk/article/excel-funktioner-alfabetisk-b3944572-255d-4efb-bb96-c6d90033e188)

## Absolutte og relative cellereferencer
Det centrale i et regneark er begrebet cellereferencer. Disse kan være relative eller absolutte. Forskellen har kun betydning, når du kopierer formler. 

Ved relative cellereferencer er der så at sige altid samme forhold mellem formel og cellernes referencer.

Ved absolutte referencer fastholdes en cellereference – dvs. den bliver ved med at pege på en bestemt celle, hvorfra vi skal hente indholdet, uanset hvor mange gange vi tager kopier af formlen. Det bruges typisk til f.eks. moms og valutakurser. 

Du opretter en absolut reference ved at stille markøren i formlen på den celle reference du vil oprette som absolut, derefter trykker du på funktionstasten [F4]. Der vil så fremkomme et $-tegn foran kolonnenavn og rækkenavn.

[Switch between relative, absolute, and mixed references](https://support.office.com/en-us/article/switch-between-relative-absolute-and-mixed-references-dfec08cd-ae65-4f56-839e-5f0d8d0baca9)

## Navngiv celler
Ved at navngive celler kan du gøre det nemmere at læse og forstå dine formler. Desuden er en navngiven celle altid **absolut** hvilket gør at du ikke skal bruge $ hvis du vil oprette en absolut reference til cellen.

[Define and use names in formulas](https://support.office.com/en-us/article/define-and-use-names-in-formulas-4d0f13ac-53b7-422e-afd2-abd7ff379c64?ui=en-US&rs=en-US&ad=US)

## Hvis
*HVIS* funktionen, *IF* på engelsk, er en meget brugt funktion. Den giver dig mulighed for at fortage logiske sammenligninger mellem værdier.

En *HVIS*-sætning har to resultater:

1. Hvis din sammenligning er **SAND**
2. Hvis din sammenligning er **FALSK**

For eksempel **=HVIS(A1>100, 1, 2)**
Hvis værdien af cellen **A1** er større end 100 returner *HVIS* funktionen **1**. Ellers returner den **2**

[HVIS](https://support.office.com/da-dk/article/hvis-funktionen-69aed7c9-4e8a-4755-a9bc-aa8bbff73be2?ui=da-DK&rs=da-DK&ad=DK)

### Nested functions
Tit vil du have behov for at kombinere **HVIS** med andre funktioner også kaldet **Nestede** eller **Indlejrede** funktioner. Det kan også være at du vil kombinere flere **HVIS** funktioner.

[Use nested functions in a formula](https://support.office.com/en-us/article/use-nested-functions-in-a-formula-9d7c966d-6030-4cd6-a052-478d7d844166?ui=en-US&rs=en-US&ad=US)

[HVIS nestede med HVIS](https://support.office.com/en-us/article/video-nested-if-functions-bdb0ebe2-caff-4914-835b-36796040e303)


### OG - ELLER
**HVIS** kan kombineres med **OG** - **ELLER**.

[IF with AND and OR](https://support.office.com/en-us/article/video-if-with-and-and-or-2a47066d-85d8-4751-a59d-3c69d2931c3e?ui=en-US&rs=en-US&ad=US)

### HVIS - specielle versioner
Der findes nogle versioner af **HVIS**, der typisk kombinere **HVIS** med yderligere funktionalitet

- **TÆL.HVIS**  tælle antal celler som opfylder et kriterium, f.eks. hvis du vil tælle det antal gange, en bestemt by vises i en kundeliste - [TÆL.HVIS](https://support.office.com/da-dk/article/t%C3%86l-hvis-funktionen-e0de10c6-f885-4e71-abb4-1f464816df34)

- **TÆLV** tæller det antal celler, der ikke er tomme, i et celleområde - [TÆLV](https://support.office.com/da-dk/article/funktionen-t%C3%A6lv-7dc98875-d5c1-46f1-9a82-53f3219e2509)

- **SUM.HVIS** summere værdierne i et område, der opfylder kriterier, som du angiver - [SUM.HVIS](https://support.office.com/da-dk/article/sum-hvis-c44b60c3-c9f4-4789-80fe-28a07f9b75b1?ui=da-DK&rs=da-DK&ad=DK)

- **HVISER** kontrollere, om en eller flere betingelser er opfyldt og for at returnere en værdi, der svarer til den første betingelse, der er SAND.
- =HVISER(noget er SAND1; Værdi, hvis SAND1;noget er SAND2; værdi, hvis SAND2;Noget er SAND3, værdi, hvis SAND3)

[HVISER 1](https://support.office.com/da-dk/article/hviser-23c84e31-fc11-425d-ab03-5630f247b566?ui=da-DK&rs=da-DK&ad=DK)
[HVISER 2](https://support.office.com/da-dk/article/hviser-funktionen-36329a26-37b2-467c-972b-4a39bd951d45)

- **SUM.HVISER** bruges hvis du har flere betingelser der skal være opfyldt - [SUM.HVISER](https://support.office.com/da-dk/article/sum-hviser-9bdc9d30-4277-4888-b606-ae9927a650bb?ui=da-DK&rs=da-DK&ad=DK)

- **MIDDEL.HVISER** returnerer gennemsnittet af alle de celler, der opfylder flere kriterier. **HVIS.FEJL** returnerer den angivne værdi, hvis MIDDEL.HVISER evalueres til en fejl - [MIDDEL.HVISER og HVIS.FEJL](https://support.office.com/da-dk/article/video-middel-hviser-og-hvis-fejl-e1b2c34b-098b-4d4e-962b-a1ae9e15d015?ui=da-DK&rs=da-DK&ad=DK)

## Datoer
Når du arbejder med data vil det tit være nøvendigt at arbejde med datoer. Excel har en del funktioner der gør dette lettere:

- **DATO** - Returnerer serienummeret for en bestemt dato
- **DATO.FORSKEL** - Beregner antallet af dage, måneder eller år mellem to datoer. Denne funktion er nyttig i formler, hvor du skal beregne en alder.
- **DATOVÆRDI** - Konverterer en dato i form af tekst til et serienummer
- **DAG** - Konverterer et serienummer til en dag i måneden
- **DAGE** - Returnerer antallet af dage mellem to datoer
- **DAGE360** - Beregner antallet af dage mellem to datoer på grundlag af et år med 360 dage
- **UGEDAG** - Konverterer et serienummer til en dag i ugen
- **UGE.NR** - Konverterer et serienummer til et tal, der angiver ugenummeret i året
- **ARBEJDSDAG** - Returnerer serienummeret for dagen før eller efter det angivne antal arbejdsdage
- **ARBEJDSDAG.INTL** - Returnerer serienummeret for datoen før eller efter et angivet antal arbejdsdage ved hjælp af parametre for at angive, hvilke og hvor mange dage der er weekenddage
- **** - Returnerer serienummeret for dags dato

Microsoft vejledninger:

- [Formatere en dato på den ønskede måde](https://support.office.com/da-dk/article/formatere-en-dato-p%C3%A5-den-%C3%B8nskede-m%C3%A5de-8e10019e-d5d8-47a1-ba95-db95123d273e)
- [DATO(år, måned, dag)](https://support.office.com/da-dk/article/dato-funktionen-e36c0c8c-4104-49da-ab83-82328b832349)
- [Beregne forskellen mellem to datoer](https://support.office.com/da-dk/article/beregne-forskellen-mellem-to-datoer-8235e7c9-b430-44ca-9425-46100a162f38)

## Procenter
Nogle gange kan procentdele være frustrerende, fordi det ikke altid er let at huske, hvad vi lærte om dem i skolen? 
Lad Excel gøre arbejdet for dig! Simple formler kan gøre det lettere at finde f.eks. procentdelen af en total eller den procentvise forskel mellem to tal.

[Calculate percentages](https://support.office.com/da-dk/article/calculate-percentages-6b5506e9-125a-4aba-a638-d6b40e603981)

[Formatere tal som procentdele](https://support.office.com/da-dk/article/formatere-tal-som-procentdele-de49167b-d603-4450-bcaa-31fba6c7b6b4)

## Diagrammer
Diagrammer hjælper dig med at visualisere data på en måde, som gør størst indtryk på dit "læseren".

[Oprette et diagram fra start til slut](https://support.office.com/da-dk/article/oprette-et-diagram-fra-start-til-slut-0baf399e-dd61-4e18-8a73-b3fd5d5680c2)

### Sekundær akse
Når tallene i et diagram varierer meget fra dataserie til dataserie, eller når du har blandede typer data (f.eks. pris og volumen), skal du afbilde en eller flere dataserier på en sekundær lodret (værdi) akse. 

[Sekundær akse i et diagram](https://support.office.com/da-dk/article/tilf%C3%B8j-eller-fjern-en-sekund%C3%A6r-akse-i-et-diagram-i-excel-91da1e2f-5db1-41e9-8908-e1a2e14dd5a9?ui=da-DK&rs=da-DK&ad=DK)

### Tendenslinjer
Find ud af, hvordan du opretter og tilføjer en tendenslinje.

[Indstillinger for tendenslinje i Office](https://support.office.com/da-dk/article/indstillinger-for-tendenslinje-i-office-92157920-fee4-4905-bc89-6a0f48152c52)

[Føje en tendens- eller bevægelig gennemsnitslinje til et diagram](https://support.office.com/da-dk/article/f%C3%B8je-en-tendens-eller-bev%C3%A6gelig-gennemsnitslinje-til-et-diagram-fa59f86c-5852-4b68-a6d4-901a745842ad)

## Minidiagrammer
Et minidiagram er et lille diagram i en regnearkscelle, som giver en visuel præsentation af data. Brug minidiagrammer til at vise tendenser indenfor en række værdier såsom sæsonbestemte stigninger eller fald, økonomiske cyklusser eller for at fremhæve maksimum-og minimumsværdier. Indsæt et minidiagram tæt på pågældende data for at have størst påvirkning.

[Bruge minidiagrammer til at få vist datatendenser](https://support.office.com/da-dk/article/bruge-minidiagrammer-til-at-f%C3%A5-vist-datatendenser-1474e169-008c-4783-926b-5c60e620f5ca?ui=da-DK&rs=da-DK&ad=DK)

# Opslagsfunktioner
Excel har flere funktioner som du kan bruge til at finde værdier i et datasæt. De mest brugte er:

- **LOPSLAG** - Søger i øverste række af en matrix og flytter på tværs af rækken for at returnere en celleværdi
- **VOPSLAG** - Søger i den øverste række af en matrix og returnerer værdien af den angivne celle
- **INDEKS** - Anvender et indeks til at vælge en værdi fra en reference eller en matrix
- **SAMMENLIGN** - Slår værdier op i en reference eller en matrix
- **XOPSLAG** - Er en ny opslagsfunktion, den kom i 2020 og vil klart på sigt komme til at erstatte flere af de andre.

### LOPSLAG
Brug **LOPSLAG** når du vil finde data i en tabel eller et område efter række værdier.

Hvis det er syntaksen for LOPSLAG er:

**VLOOKUP(lookup_value,table_array,col_index_num,[range_lookup])**

[LOPSLAG](https://support.office.com/da-dk/article/lopslag-funktionen-0bbc8083-26fe-4963-8ab8-93a18ad188a1?wt.mc_id=otc_tips)

Microsoft har oprettet en pdf der giver en oversigt over **LOPSLAG**
[LOPSLAG Reference PDF](https://download.microsoft.com/download/9/b/4/9b49c8c5-d7a9-45b1-b8b6-52067e9970a8/AF101984660_en-us_xl_qrc_vlookup%20refresher.pdf)

Microsoft har også oprettet en fejlfindings oversigt

[Fejlfindings PDF LOPSLAG](https://download.microsoft.com/download/3/4/0/340f95a5-33cd-45a5-8701-7efa0cf82daf/AF102038056_en-us_xl_qrc_vlookup_troubleshooter.pdf)

Video omkring [Lookup Functions in Excel](https://vimeo.com/87812779)

### XOPSLAG
Brug funktionen XOPSLAG til at finde ting i en tabel eller et område efter række. Slå prisen for en del af bildelen af varenummeret til, eller Find et medarbejdernavn baseret på deres medarbejder-ID. Med XOPSLAG kan du se en kolonne i en kolonne for et søgeord og returnere et resultat fra den samme række i en anden kolonne, uanset hvilken side kolonnen retur er slået til.

[Funktionen XOPSLAG](https://support.microsoft.com/da-dk/office/funktionen-xlookup-b7fd680e-6d10-43e6-84f9-88eae8bf5929)

## Tabeller
Hvis du arbejder med data i Excel, og det kommer du til, så er tabeller et rigtigt stærkt og meget anvendiligt værktøj.

Microsoft vejledninger:

[Microsoft kursus tabeller](https://support.office.com/da-dk/article/video-opret-en-tabel-bf0ce08b-d012-42ec-8ecf-a2259c9faf3f?ui=da-DK&rs=da-DK&ad=DK)
[Oversigt over Excel-tabeller](https://support.office.com/da-dk/article/oversigt-over-excel-tabeller-7ab0bb7d-3a9e-4b56-a3c9-6c94334e492c)
[Oprette relationer mellem tabeller i Excel](https://support.office.com/da-dk/article/oprette-relationer-mellem-tabeller-i-excel-fe1b6be7-1d85-4add-a629-8a3848820be3)
[Kompatibilitetsproblemer med Excel-tabeller](https://support.office.com/da-dk/article/kompatibilitetsproblemer-med-excel-tabeller-1e9c9c83-bf17-41c7-b243-c48625a7a6ff)

## Udsnitsværktøjer
Udsnitsværktøjer giver dig knapper, som du kan klikke på for at filtrere **Tabeldata** eller **Pivottabeldata**. 
Ud over hurtig filtrering angiver udsnitsværktøjer også den aktuelle filtreringstilstand, hvilket gør det nemt at forstå, hvad der præcis vises i en filtreret pivottabel.

[Udsnitsværktøjer](https://support.office.com/da-dk/article/brug-udsnitsv%C3%A6rkt%C3%B8jer-til-at-filtrere-data-249f966b-a9d5-4b0f-b31a-12651785d29d)
