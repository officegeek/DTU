---
layout: default
title: Excel
nav_order: 1
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

## PivotTabel
En **PivotTabel** er et effektivt værktøj til at beregne, opsummere og analysere data, der gør det muligt at se sammenligninger, mønstre og tendenser i dataene.

[PivotTabel](https://support.office.com/da-dk/article/oprette-en-pivottabel-for-at-analysere-regnearksdata-a9a84538-bfe9-40a9-a8e9-f99134456576?ui=da-DK&rs=da-DK&ad=DK)

### PivotTabel Feltlisten
Når du har oprettet en pivottabel, får du vist feltlisten. Du kan ændre pivottabellens design ved at tilføje og arrangere dens felter. Hvis du vil sortere eller filtrere de kolonner med data, som vises i pivottabel, skal du se Sortere data i en pivottabel og Filtrere data i en pivottabel.

[Feltlisten](https://support.office.com/da-dk/article/brug-af-feltlisten-til-at-arrangere-felter-i-en-pivottabel-43980e05-a585-4fcd-bd91-80160adfebec)

### Gruppér data
Når du grupperer data i en pivottabel, kan det vise dig et undersæt af data, der skal analyseres.

[Gruppér eller opdel en gruppe af data i en pivottabel](https://support.office.com/da-dk/article/grupp%C3%A9r-eller-opdel-en-gruppe-af-data-i-en-pivottabel-c9d1ddd0-6580-47d1-82bc-c84a5a340725?ui=da-DK&rs=da-DK&ad=DK)

### Beregn værdier i en PivotTabel
I en pivottabel kan du bruge summeringsfunktioner i værdifelter til at kombinere værdier fra den underliggende datakilde. Hvis summeringsfunktioner og brugerdefinerede beregninger ikke giver de resultater, du ønsker, kan du oprette dine egne formler i beregnede felter eller beregnede elementer. Du kan f.eks. tilføje et beregnet element med formlen for salgsprovisioner, som kunne være forskellige fra område til område. Pivottabellen medtager derefter provisionen i subtotaler og hovedtotaler.

[Beregn værdier i en pivottabel](https://support.office.com/da-dk/article/beregn-v%C3%A6rdier-i-en-pivottabel-11f41417-da80-435c-a5c6-b0185e59da77)

### PivotDiagram
Nogle gange er det svært at se det store billede, når dine ubehandlede data ikke er blevet opsummeret. Din første Instinct kan være at oprette en pivottabel, men ikke alle kan se tal i en tabel og hurtigt se, hvad der foregår. Pivotdiagrammer er en god måde at føje datavisualiseringer til dine data.

[PivotDiagram](https://support.office.com/da-dk/article/opret-et-pivotdiagram-c1b1e057-6990-4c38-b52b-8255538e7b1c)

### Slette en PivotTabel
Når du ikke længere har brug for en pivottabel, skal du markere hele pivottabellen og trykke på Delete for at fjerne den.

[Slet PivotTabel](https://support.office.com/da-dk/article/slette-en-pivottabel-1de9b894-9178-43b3-b436-92e3ddb9175b)

## Udsnitsværktøjer
Udsnitsværktøjer giver dig knapper, som du kan klikke på for at filtrere **Tabeldata** eller **Pivottabeldata**. 
Ud over hurtig filtrering angiver udsnitsværktøjer også den aktuelle filtreringstilstand, hvilket gør det nemt at forstå, hvad der præcis vises i en filtreret pivottabel.

[Udsnitsværktøjer](https://support.office.com/da-dk/article/brug-udsnitsv%C3%A6rkt%C3%B8jer-til-at-filtrere-data-249f966b-a9d5-4b0f-b31a-12651785d29d)

## PivotTabel Tidslinje
I stedet for at justere filtre for at få vist datoer kan du bruge en tidslinje i en pivottabel – en dynamisk filtreringsindstilling, hvor du kan nemt kan filtrere efter dato/klokkeslæt og zoome ind på det ønskede tidsrum ved hjælp af et skyderkontrolelement. Klik på Analysér > Indsæt en Tidslinje for at indsætte en på regnearket.

[PivotTabel Tidslinje](https://support.office.com/da-dk/article/opret-en-pivottabel-tidslinje-til-at-filtrere-datoer-d3956083-01be-408c-906d-6fc99d9fadfa)

## Dataanalyseværktøjer
Excel har tre meget powerfulde dataanalyseværktøjer:

- Power Pivot
- Hent og transformer (Power Query)
- Power View

[Hente og transformere og Power Pivot i Excel](https://support.office.com/da-dk/article/hente-og-transformere-og-power-pivot-i-excel-42d895c2-d1d7-41d0-88da-d1ed7ecc102d)

### Power Pivot
Power Pivot er en datamodellerings teknologi, der giver dig mulighed for at oprette datamodeller, etablere relationer og oprette beregninger. Med Power Pivot kan du arbejde med store datasæt, opbygge omfattende relationer og oprette komplekse (eller enkle) beregninger, alt sammen i et højtydende miljø med den vante brugeroplevelse i Excel.

[Aktiver tilføjelsesprogrammet Power Pivot](https://support.office.com/da-dk/article/start-tilf%C3%B8jelsesprogrammet-power-pivot-til-excel-a891a66d-36e3-43fc-81e8-fc4798f39ea8)

[Power Pivot – Oversigt og læring](https://support.office.com/da-dk/article/Power-Pivot-%E2%80%93-Oversigt-og-l%C3%A6ring-f9001958-7901-4caa-ad80-028a6d2432ed)

### Hent og transformér
**Hent og transformér** er en dataforbindelses teknologi, der gør det muligt for dig at finde, forbinde, kombinere og justere datakilder for at opfylde dine analysebehov. Funktioner i **Hent og transformér** er tilgængelige i Excel og Power BI desktop.

[Power Query – Oversigt og læring](https://support.office.com/da-dk/article/power-foresp%C3%B8rgsel-%E2%80%93-oversigt-og-l%C3%A6ring-ed614c81-4b00-4291-bd3a-55d80767f81d)

[Introduktion til Power Query](https://support.office.com/da-dk/article/introduktion-til-power-foresp%C3%B8rgsel-7104fbee-9e62-4cb9-a02e-5bfb1a6c536a)

### Power View
Power View er en datavisualiserings teknologi, der giver dig mulighed for at oprette interaktive diagrammer, grafer, kort og andre visuelle elementer, der gør dine data levende. Power View er tilgængelig i Excel, SharePoint, SQL Server og Power BI.

Der er nogle [systemkrav til Power-visning](https://support.office.com/da-dk/article/systemkrav-til-power-view-11d2c4b3-0633-4c60-b0e2-88f0f62b7697), afhængigt af hvilken version af Excel, SharePoint eller SQL Server du bruger. Visualiseringerne i Power-visning er også tilgængelige i [Power BI](https://powerbi.com/) og [Power BI Designer](https://powerbi.microsoft.com/designer).

Power View er et tilføjelsesprogram til Excel. Du skal muligvis aktivere det for at bruge Power View.

[Power-visning – Oversigt og læring](https://support.office.com/da-dk/article/power-visning-%E2%80%93-oversigt-og-l%C3%A6ring-5380e429-3ee0-4be2-97b7-64d7930020b6)

[Power View: Undersøge, visualisere og præsentere dine data](https://support.office.com/da-dk/article/power-view-unders%C3%B8ge-visualisere-og-pr%C3%A6sentere-dine-data-98268d31-97e2-42aa-a52b-a68cf460472e)

### Generel forordning om databeskyttelse (GDPR)
I maj 2018 er en europæiske beskyttelse af personlige oplysninger lovgivning [Generelle Data beskyttelse bestemmelser (GDPR)](https://ec.europa.eu/info/law/law-topic/data-protection_en) på grund af træde i kraft. GDPR er sat, nye regler på firmaer, offentlige institutioner, ikke overskud og andre organisationer, tilbud varer og tjenesteydelser til personer i EU (EU), eller at indsamle og analysere data, der er bundet til EU-bosiddende. GDPR gælder uanset hvor du befinder dig.

Du kan få flere oplysninger om indstillingerne for beskyttelse af personlige oplysninger om opdatering, sletning eller eksportere personlige data fra Power-forespørgsel projektmapper,: [Få vist og opdatere en delt forespørgsel (Power-forespørgsel).](https://support.office.com/da-dk/article/f%C3%A5-vist-og-opdatere-en-delt-foresp%C3%B8rgsel-power-foresp%C3%B8rgsel-ece958c5-baf2-4789-9312-bb113e679e91)

Du kan også kopiere forespørgselsindstillinger Power-forespørgsel **Redigere definitionen for forespørgsel** i dialogboksen. Mikset kan hentes ved at dobbeltklikke på it i ruden **Mine Datakatalogforespørgsler** opgaver i Excel. Alle forespørgslerne, derefter indlæses til Excel-projektmappen. Hvis du vil se individuelle forespørgsler, åbne **Query Editor** og gå igennem hvert trin enkeltvis, eller gå til fanen **Vis** og åbne **Avanceret Editor**.
