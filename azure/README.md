---
layout: default
title: Azure
nav_order: 130
---
<span class="fs-1">
[HOME](../README.md){: .btn .btn-blue }
</span>

# Azure
Microsoft Azure er en cloud computingplatform og infrastruktur, der er skabt af Microsoft.

![](https://www.logo.wine/a/logo/Microsoft_Azure/Microsoft_Azure-Logo.wine.svg)

Hvis du har en MAC computer skal du oprette en virtuel machine der har Windows som styresystem. Årsagen er at du skal installere to programmer der kun fås til Windows platformen:

- Microsoft Project
- Microsoft Power BI Desktop

Som MAC brugere kan du også have fordele af at brugere den virtuelle machine til Excel, grundet forskellen i import funktionaliteterne.

Som studerende på DTU har du 200 USD som du kan bruge på Azure. Det betyder at det er vigtigt at du lukker den virtuelle machine ned når den ikke bruges.

Hvis der er nogle windows brugere der har lyst til at prøve "*kræfter*" med en virtuel machine kan de også følge denne vejledning¨.

Mere info omkring Azure Dev Tools for Teaching kan læses via nedenstående link.
[https://azureforeducation.microsoft.com/en-us/Support/FAQ](https://azureforeducation.microsoft.com/en-us/Support/FAQ)

## Licenser
Gennem DTU har du en studenter licens til Microsoft Project, Microsoft Power BI Desktop kræver ingen licens.

## Oprettelse af virtuel machine
- For at logge på Azure Education Hub skal du tilgå [https://aka.ms/devtoolsforteaching](https://aka.ms/devtoolsforteaching)
- Ved Microsoft’s login siden skriver du **INITIALER/S-NUMMER@win.dtu.dk**
- Siden vil derefter viderestille dig til DTU’s login side, hvor du logger på med dine DTU legitimationsoplysninger

DTU har oprette en vejledning til hvordan du opretter dig på Azure og får adgang til de 200 USD. Det er vigtigt at du bruger dit DTU login/e-mail.

[DTU Vejledning](https://www.inside.dtu.dk/-/media/dtu-inside/medarbejder/it-og-telefoni/vejledninger/software/software-til-studerende-azure-microsoft-dk-1-.pdf)

### Video
Jeg har oprette en video der vier hvordan du opretter den virtuelle machine.

<div style="position: relative; padding-bottom: 56.25%; height: 0;"><iframe src="https://www.loom.com/embed/69508c07a13348988b950b935e139ed0" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>


## Adgang til den virtuelle machine - RDP
For at komme din på den virtuelle machine, bruge den, skal du brugere Remote Desktop Protocol (**RPD**). Microsoft har lavet en meget fin vejledning til hvordan du brugere RDP på både MAC og Windows:

- [Install Microsoft Remote Desktop on a Mac](https://docs.microsoft.com/en-us/azure/lab-services/connect-virtual-machine-mac-remote-desktop)
- [Connect to a VM using Remote Desktop Protocol on Windows](https://docs.microsoft.com/en-us/azure/lab-services/connect-virtual-machine-windows-rdp)

### Video - Login - Fra Windows :-)

<div style="position: relative; padding-bottom: 56.25%; height: 0;"><iframe src="https://www.loom.com/embed/09c3488e57b3413b9a2b62c144b59293" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

### Luk ned - Vigtigt
Da i har en limit på 200 USD er det vigtigt at i **lukker den virtuelle machine når i ikke bruger den**!

<div style="position: relative; padding-bottom: 56.25%; height: 0;"><iframe src="https://www.loom.com/embed/a1677e7e70e24c278bb6f529da566998" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>


## Installation af programmer
Du skal installere de to programmer på den virtuelle machine

- Microsoft Project
- Microsoft Power BI Desktop

### Microsoft Project
Dette gælder primært MAC brugere, men nogle gange er der en konflikt mellem specielt gamle Office installationer på en Windows computer. Hvis det er tilfældet er det nemmest at bruge en virtuel machine.

Først skal du hente installationsfilen til Microsoft Project på [https://aka.ms/devtoolsforteaching](https://aka.ms/devtoolsforteaching).

På den virtuelle machine skal du gøre følgende:
- Login med DTU username på [https://aka.ms/devtoolsforteaching](https://aka.ms/devtoolsforteaching)
- Vælg **software** i menuen til venstre
- Søg efter - **Project**
- Klik på **Project Professional 2021 - DVD**
- Klik på View Key
- Klik på kopier Product key
- Klik på **download** knappen - Husk hvor du gemmer den - *Downloads*

Det næste du skal gøre er at installere Microsoft Project.

- Find den **ISO fil** du har downloadet
- Klik på og vælg **Mount**
- Følg installations vejledningen

### Video - Microsoft Project

<div style="position: relative; padding-bottom: 56.25%; height: 0;"><iframe src="https://www.loom.com/embed/af731f9b0531473689f0c091643f4821" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

### Power BI Desktop
Det er ikke muligt at installere Microsoft Power BI Desktop på en Mac, så det skal du gøre på den virtuelle machine - [https://powerbi.microsoft.com/en-us](https://powerbi.microsoft.com/en-us/)

- Login på den virtuelle machine - RDP
- Klik på **Microsoft Store**
- Søg efter **Power BI**
- Install - *PS. Kan godt gøres uden Microsoft konto*

### Video - Microsoft Power BI Desktop

<div style="position: relative; padding-bottom: 56.25%; height: 0;"><iframe src="https://www.loom.com/embed/7ddf725e26434998b16a13656596c729" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>