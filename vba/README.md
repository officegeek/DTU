---
layout: default
title: VBA
nav_order: 5
---
[HOME](../README.md)
# VBA
VBA bruges rigtig meget i Excel og det er også i Excel du primært kommer til at bruge VBA.

Microsoft har en *Getting started with VBA in Office* guide, den er på engelsk, men giver et rigtigt godt overblik.

[Getting started with VBA in Office](https://docs.microsoft.com/en-us/office/vba/library-reference/concepts/getting-started-with-vba-in-office?irgwc=1&OCID=AID681541_aff_7806_1246483&tduid=(ir__snukbsnj6wv13yycus23kguo3u2xm9ybeexehznx00)(7806)(1246483)(%28f5d2667ddccb4999bcba81444ccf4381%29%2881561%29%28686431%29%28at106140_a107739_m12_p12460_cDK%29%28%29)(f5d2667ddccb4999bcba81444ccf4381)&irclickid=_snukbsnj6wv13yycus23kguo3u2xm9ybeexehznx00)

## Udvikler fanen
Der er en ekstra fane du vil have glæde af når du arbejder med VBA i Excel - **Udvikler** (Developer).

Du aktivere den på følgende måde:

1. Filer
2. Indstillinger
3. Tilpas båndet
4. Sæt hak ud for *Udvikler*
5. Klik Ok


## Makrooptageren
Det er muligt at optage dine makroer, det er dog ikke alt der kan optages. Det at optage en makro kan også bruges til at lære hvordan du programmere i VBA, f.eks. hvis du ikke ved hvordan man via VBA gør en celle's tekst fed - så kan du optage det og genbruge det i din egen kode.

Microsoft har en rigtig god guide til dette, den dækker både Windows og MacOS.

[Makro optager guide - DK version](https://support.office.com/da-dk/article/automatiser-opgaver-med-makrooptageren-974ef220-f716-4e01-b015-3ea70e64937b)

## Basis elementer
VBA består af 5 basis elementer:

1. Objects
2. Collections
3. Properties
4. Methods
5. Parameters

### Objects og Collections
Du brugere *Objects* til at henvis til noget, f.eks.:

- Workbook, henviser til Workbook object
- Worksheet, henviser til Worksheet object

I nogle tilfælde er det muligt at henvise til flere *Objects* på sammen tid. Dette gøres via en *Collection*, f.eks.:

- All Open Workbooks
- All Worksheets i en Workbook

Med andre ord er *Objects* normalt grupperet i samlinger af beslægtede objekter, f.eks.:

- Collection af ​​alle åbne workbooks i Workbooks collection
- Collection af ​​alle worksheets i en projektmappe i Worksheets collection

Du kan normalt (der er undtagelser) skelne et enkelt *Object* fra en *Collection* af objekter, fordi *Collection* indeholder "s" i slutningen, f.eks.:

- Workbook object vs. Workbook**s** collection
- Worksheet object vs. Worksheet**s** collection


### Properties
*Properties* er de egenskaber eller attributter, der beskriver et objekt. De fleste *Object* har et sæt egenskaber. Disse egenskaber bestemmer blandt andet; Udseende og Funktion

*Properties* beskriver egenskaberne eller attributterne på et *Object*, f.eks.:

- Address of a cell - **Range.Address**
- Worksheet formula within a cell - **Range.Formula**
- Height of a row of cells - **Range.Height**
- Interior color of a cell - **Interior.Color**
- Name of a worksheet - **Worksheet.Name**

### Methods
Metoder *udtrykker* en handling, du udfører med eller på et *Object*, F.eks.:

- Copy, Cut and Paste methods
- Delete method
- Sort method
- Find method

### Parameters
Parametre giver dig mulighed for yderligere at angive, hvordan:

- A method is carried out
- A property behaves or is modified

Overvej f.eks., Når du brugere indsæt special (Range.PasteSpecial). I Excel indeholder dialogboksen *Indsæt specielle* flere muligheder, som giver dig mulighed for at angive, hvordan Excel skal udfører indsætningen.

### Connect objects with properties or methods
I VBA bruger du et punktum (.) Til at forbinde:

- Object med properties - Object.Property
- Object med methods - Object.Method

### Basic structure - VBA statement
Grundlæggende kan du opdele VBA-sætninger ved at kombinere 3 elementer:

- Objects
- Punktum (.)
- Property eller Methode

Det giver dig 2 grundlæggende sætningsstrukturer:

- Object.Property - Range("A1").Font.Bold = True
- Object.Method - Range("A1").Select

## Excel Object Model
VBA er organisert i et logisk hieraki - **Excel Object Model**.
Denne en **meget** stor model med mange niveauer og forgreninger. Hver *Object* indeholder typisk andre/nye objekter.

Øverst er **Application** som repræsentere hele Excel applikationen. Den indeholder flere objekter, f.eks. *Workbook object* som indeholder *Worksheet object*, som indeholder flere andre objekter, f.eks. *Range object* og *PivotTable object*.

Dette mønster fortsætter med at udfolde sig på en lignende måde, 
indtil du støder på objekter, der ikke indeholder andre objekter.

[Object model - Excel](https://docs.microsoft.com/en-us/office/vba/api/overview/excel/object-model)


## IF
[Microsoft If...Then...Else statement](https://docs.microsoft.com/en-us/office/vba/language/reference/user-interface-help/ifthenelse-statement)

## Variabler

## Loop
LOOP eller løkker er meget brugt i programmering. Det kan f.eks. være gennemløb af data i et Excel ark.

VBA har flere forskellige typer af løkker som kan opdeles i to grupper:
- For - Next
- Do - Loop

Ved et For-Next loop kender du antallet af gennemløb, det kan f.eks. være alle Ark i en Excel fil. Der er to typer af For-Next loop

```vbnet
    For variabel = a TO b
        VBA Kode
    Next
    
    For Each Egenskab IN Objekt
        VBA Kode
    Next
``` 

Ved et Do-Loop udføres Loopet indtil en betingelse er opfyldt
Der er 2 hoved typer af Do-Loop. Udfør en Betingelse indtil denne er Opfyldt, eller udfør loopet så længe betingelsen er sand. Du kan starte med at skrive Betingelsen eller du kan skrive Betingelsen til sidst i loopet.

```vbnet
    Do Until Betingelse
      VBA Kode
    Loop
    
    Do While Betingelse 
      VBA Kode 
    Loop
    
    Do
      VBA Kode
    Loop Until Betingelse

    Do
      VBA Kode
    Loop While Betingelse
``` 

Hvis du har behov for at Stoppe/komme ud af et Loop før det er helt færdigt, kan du gøre det med denne kommando

```vbnet
    Exit do
    
' F.eks.
    Do Until Betingelse
      If Betingelse then
          Exit Do
      End If
    Loop
``` 
## Fejlhåndtering
Der er forskellige typer af fejl i et program. Nogle fejl opstår fordi der er en fejl i programmeringen af programmet og nogle fejl opstår via brugeren, f.eks. ved en forkert indtastning.

Error handling består af 3 "kommandoer"

1. On Error GoTO *Line / ErrorHandler:*
2. On Error Resume Next
3. On Error GoTo 0

```vbnet
    Sub InitializeMatrix(Var1, Var2, Var3, Var4) 
        On Error GoTo ErrorHandler 
             . . . 
         Exit Sub xx
        ErrorHandler: 
             . . . 
        Resume Next
    End Sub
``` 
[Microsoft On Error Statement oversigt](https://docs.microsoft.com/en-us/office/vba/language/reference/user-interface-help/on-error-statement)

## Andre Programmer
Alt efter hvilket Microsoft Office program du arbejder i vil det være muligt at åbne et andet Office program, f.eks. du har nogle diagrammer i Excel som du opdateret og derefter gerne vil overføre til PowerPoint - *Automatisk*.

### Word
Det kan tit være en fordel at bruge Word til oprettelse af rapporter og lign.  
Denne VBA kode vil virke uanset hvilken Word version du brugere og uden yderligere referencer, hvilket er en stor fordel når du opgradere til en ny Office version.

```vbnet
Sub AabenWord()
    ' Variable
    Dim appWord As Object
    
    ' Åben Word
    Set appWord = CreateObject(Class:="Word.Application")

    ' Handlinger i Word
    With appWord
        .Visible = True ' Vis Word
        .Documents.Add  ' Nyt dokument
    End With

    ' Oprydning
    Set appWord = Nothing

End Sub
```

#### Åben eksisterende dokument
Brug denne VBA kode til at åbne et eksisterende Word dokument.  
Bemærk at du skal angive stien og filnavnet i variablen *WordFilePath*

```vbnet
Sub AabenWordDokument()
    ' Variable
    Dim appWord As Object
    Dim WordFilePath As String
    
    ' Åben Word
    Set appWord = CreateObject(Class:="Word.Application")
    
    ' Sti og filnavn på det dokument der skal åbnes
    WordFilePath = "C:\Users\Tue Hellstern\Documents\SalgsBudget.docx"

    ' Handlinger i Word
    With appWord
        .Visible = True
        .Documents.Open Filename:=WordFilePath
    End With
    
    ' Oprydning
    Set appWord = Nothing
    
End Sub
```
Du kan læse mere om de muligheder der er i *Documents.Open* metoden her:  
[Documents.Open method (Word)](https://docs.microsoft.com/en-us/office/vba/api/word.documents.open)

#### Kopier Excel tabel til Word
Eksempel på hvordan du kopiere en Excel tabel til Word. Tabellen har navnet: *SalgsData*.

```vbnet
Sub TabelWordDokument()
    ' Variable
    Dim appWord As Object
    Dim tbl As Excel.Range
    Dim WordTable As Object
    Dim WordFilePath As String
    
    ' Åben Word
    Set appWord = CreateObject(Class:="Word.Application")
    
    ' Sti og filnavn på det dokument der skal åbnes
    WordFilePath = "C:\Users\Tue Hellstern\Documents\SalgsBudget.docx"
    
    ' Tabellen der skal kopieres
    Set tbl = ThisWorkbook.Worksheets(1).ListObjects("SalgsData").Range
    tbl.Copy

    ' Handlinger i Word
    With appWord
        .Visible = True
        .Documents.Open Filename:=WordFilePath
        .Selection.PasteExcelTable _
            LinkedToExcel:=False, WordFormatting:=False, RTF:=False ' Indsæt Excel tabel
        .ActiveDocument.Tables(1).AutoFitBehavior 1 ' wdAutoFitWindow = 1
    End With

    ' Oprydning
    Set appWord = Nothing
    Application.CutCopyMode = False
    
End Sub
```

* [Selection.PasteExcelTable method (Word)](https://docs.microsoft.com/en-us/office/vba/api/word.selection.pasteexceltable)
* [WdAutoFitBehavior Enum](https://docs.microsoft.com/en-us/dotnet/api/microsoft.office.interop.word.wdautofitbehavior?view=word-pia)

### PowerPoint
Det er jo oplagt at oprette PowerPoint præsentationer baseret på data fra et Excel ark.

#### Åben PowerPoint

```vbnet
Sub AabenPowerPoint()
    ' Variable
    Dim appPowerPoint As Object

    ' Åben PowerPoint
    Set appPowerPoint = CreateObject("PowerPoint.Application")
    
    ' Handlinger i PowerPoint
    With appPowerPoint
        .Visible = True
        .Presentations.Add
        .ActivePresentation.Slides.Add 1, 1
    End With

End Sub
```

* [Slide.Layout property (PowerPoint)](https://docs.microsoft.com/en-us/office/vba/api/powerpoint.slide.layout)

#### Åben eksisterende præsentation
Hvis du har en PowerPoint præsentation du vil åbne, kan du gøre det på denne måde.  
Bemærk at du skal angive stien og filnavnet i variablen *PowerPointPress*

```vbnet
Sub AabenPowerPointPresentation()
    ' Variable
    Dim appPowerPoint As Object
    Dim PowerPointPress As String

    ' Eksisterende PowerPoint præsentation
    PowerPointPress = "C:\Users\Tue Hellstern\Documents\Salgsdata.pptx"
    
    ' Åben PowerPoint
    Set appPowerPoint = CreateObject("PowerPoint.Application")
    
    ' Handlinger i PowerPoint
    With appPowerPoint
        .Visible = True
        .Presentations.Open (PowerPointPress)
    End With

End Sub
```

#### Indsæt slide hvis der allerede er slides i dokumentet
#### Indsæt slide i tomt dokument
#### Indsæt shape på slide
#### Vælg slide

## Sikkerhed
Du kan ændre indstillingerne for makrosikkerhed i Excel til at styre, hvilke makroer der køres, og under hvad omstændigheder, når du åbner en projektmappe.

[Ændre indstillinger for makrosikkerhed](https://support.office.com/da-dk/article/%C3%86ndre-indstillinger-for-makrosikkerhed-a97c09d2-c082-46b8-b19f-e8621e8fe373)

## Eksempler
Her kommer nogle kode eksempler

```vbnet
Sub DeleteBlankRows()
    Dim Rw As Range
    
    If WorksheetFunction.CountA(Selection) = 0 Then
        MsgBox "Der er ikke nogle blanke celler!", vbOKOnly
        Exit Sub
    End If
    
    With Application
        .Calculation = xlCalculationManual
        .ScreenUpdating = False
    End With
    
    Selection.SpecialCells(xlCellTypeBlanks).Select
    For Each Rw In Selection.Rows
        If WorksheetFunction.CountA(Selection.EntireRow) = 0 Then
            Selection.EntireRow.Delete
        End If
    Next Rw

    With Application
        .Calculation = xlCalculationAutomatic
        .ScreenUpdating = True
    End With
    
    MsgBox "Blanke rækker fjernet"
End Sub
```

