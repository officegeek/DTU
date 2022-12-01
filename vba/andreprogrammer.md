---
layout: default
title: Brug VBA i forhold andre Office programmer 
parent: VBA
nav_order: 30
---

# Makro eksempler andre Office programmer
Eksempler på hvordan du kan bruge VBA fra Excel i andre Office programmer


## Kopier tabeller til Word
Denne kode kopier tabeller til eksisterende Word dokument.

Der er brugt Early Binding, så husk reference til Word Objects.

![](./image/wordref.jpg.jpg)

```basic
Sub Export_Table_Word()
    ' Navn på eksisterende Word dokument
    Const strWordDokument As String = "Omsætnings Rapport.docx"
    
    ' Word objects
    Dim wdApp As Word.Application
    Dim wdDoc As Word.Document
    Dim wdbmRange As Word.Range
    
    ' Excel objects
    Dim wbBook As Workbook
    Dim wsSheet As Worksheet
    Dim ranReport As Range
    
    ' Initialize Excel objects
    Set wbBook = ThisWorkbook
    Set wsSheet = wbBook.Worksheets("Tabeller")
    Set ranReport = wsSheet.Range("OmsAfd")
    
    ' Initialize Word objets
    Set wdApp = New Word.Application
    Set wdDoc = wdApp.Documents.Open(wbBook.Path & "\" & strWordDokument)
    Set wdbmRange = wdDoc.Bookmarks("OmsRapport").Range
    
    ' Hvis der er indsat en tabel skal denne fjernes
    ' Bemærk brugen af Error Handling

    On Error Resume Next
    With wdDoc.InlineShapes(1)
        .Select
        .Delete
    End With
    On Error GoTo 0
    
    ' Kopier tabellen
    ranReport.Copy
    
    ' Indsæt tabellen ved Bogmærket - OmsRapport
    With wdbmRange
        .Select
        .PasteSpecial Link:=False, _
                      DataType:=wdPasteMetafilePicture, _
                      Placement:=wdInLine, _
                      DisplayAsIcon:=False
    End With

    ' Gem og luk Word dokumentet
    With wdDoc
        .Save
        .Close
    End With
    
    wdApp.Quit
    
    ' Ryd op - Nulstil variabler
    Application.CutCopyMode = False
    Set wdbmRange = Nothing
    Set wdDoc = Nothing
    Set wdApp = Nothing
    
    ' Besked til bruger
    MsgBox "Tabellen er blevet kopieret" & vbNewLine & _
           "til " & strWordDokument, vbInformation

End Sub
```

## Kopier Diagrammer til PowerPint
Kopier alle diagrammer fra det aktive sheet til en ny PowerPoint præsentation.

Der er brugt Early Binding, så husk reference til PowerPoint Objects.

![](./image/powerpointref.jpg)

```basic
Sub Overfor_til_PowerPoint()
    ' Variabler
    Dim pptApp As PowerPoint.Application
    Dim pptPres As PowerPoint.Presentation
    Dim pptSlide As PowerPoint.Slide
    
    Dim pptSlideCount As Integer ' Antal Slides
    
    Dim cht As Excel.ChartObject ' Excel diagram
    
    ' Vælg ark
    PowerPointArk.Select
    
    ' Åben PowerPoint
    Set pptApp = New PowerPoint.Application ' Åben applikationen PowerPoint
    Set pptPres = pptApp.Presentations.Add  ' Tilføj en præsentation
    
    
    ' Find alle Diagrammer i det aktive sheet
    For Each cht In ActiveSheet.ChartObjects
    
        ' Slide
        pptSlideCount = pptPres.Slides.Count ' Antal slide i præsentationen
        Set pptSlide = pptPres.Slides.Add(pptSlideCount + 1, ppLayoutBlank) ' Blankt slide
    
        ' Diagram
        cht.Select ' Vælg diagram
        ActiveChart.ChartArea.Copy ' Kopi af slide
        pptSlide.Shapes.PasteSpecial (ppPasteJPG) ' Indsæt slide i PowerPoint
        
        ' Tilpasning af diagram
        With pptApp.ActiveWindow.Selection.ShapeRange
            .Height = Application.CentimetersToPoints(12)
            .Width = Application.CentimetersToPoints(20)
            .Left = Application.CentimetersToPoints(7)
            .Top = Application.CentimetersToPoints(3)
        End With
    
    Next
    
    ' Luk / Gem
    pptPres.SaveAs "C:\Users\Tue Hellstern\Dropbox\DTU\2020_2\VBA\test.pptx"
    
    pptPres.Close
    pptApp.Quit
    
End Sub
```

