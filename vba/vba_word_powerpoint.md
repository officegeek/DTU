---
layout: default
title: VBA - Word og PowerPoint
parent: VBA
nav_order: 30
---

# Brug af VBA i andre programmer
Eksempler på hvordan du kan bruge VBA i andre programmer - Word og PowerPoint

## PowerPoint

```basic
Sub Overfor_til_PowerPoint()
    ' Variabler
    Dim Filepath As String
    Dim Dag As String
    Dim Maaned As String
    Dim Aar As String
    
    Dim pptApp As PowerPoint.Application
    Dim pptPres As PowerPoint.Presentation
    Dim pptSlide As PowerPoint.Slide
    
    Dim pptSlideCount As Integer ' Antal Slides
    
    Dim cht As Excel.ChartObject ' Excel diagram
    
    ' Vælg ark
    SalesDiagram.Select
    
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
        pptSlide.Shapes.PasteSpecial (ppPasteJPG) ' Indsaæt slide i PowerPoint
        
        ' Tilpasning af diagram
        With pptApp.ActiveWindow.Selection.ShapeRange
            .Height = Application.CentimetersToPoints(12)
            .Width = Application.CentimetersToPoints(20)
            .Left = Application.CentimetersToPoints(7)
            .Top = Application.CentimetersToPoints(3)
        End With
    
    Next
    
    SalesDiagram.Select
    
    ' Luk / Gem
    Filepath = Application.ActiveWorkbook.Path
    Dag = Format(Date, "dd")
    Maaned = Format(Date, "mm")
    Aar = Format(Date, "yyyy")
    
    pptPres.SaveAs Filepath & "\" & Dag & "_" & Maaned & "_" & Aar & "_sales.pptx"
    pptPres.Close
    pptApp.Quit
    
End Sub
```

## Word


```basic
Sub Export_Word()
    ' Variabler
    ' Navn på Word dokument
    Const strWordDokument As String = "DataImport.dotx"
    
    ' Word object
    Dim wdApp As Word.Application
    Dim wdDoc As Word.Document
    Dim wdBmkRange As Word.Range
    
    ' Excel object
    Dim wbBook As Workbook
    Dim wbSheet As Worksheet
    Dim ranRapport As Range
    
    Set wbBook = ThisWorkbook ' Den aktive fil
    Set wbSheet = wbBook.Worksheets("Tabeller") ' ref til ark
    Set ranRapport = wbSheet.Range("OmsAfd") ' Ref. til tabellen - OmsAfd
    
    ' Start Word
    Set wdApp = New Word.Application ' Word app
    Set wdDoc = wdApp.Documents.Open(wbBook.Path & "\" & strWordDokument) ' Åben Word doc
    
    ' Indsæt dato
    Set wdBmkRange = wdDoc.Bookmarks("bmkDato").Range ' Bogmærke: bmkDato
    wdBmkRange.InsertAfter Date
    
    ' Indsæt tabellen
    Set wdBmkRange = wdDoc.Bookmarks("bmkDataTabel").Range ' Bogmærke: bmkDataTabel
    
    ' Kopi af tabellen: OmsAfd
    ranRapport.Copy
    
    With wdBmkRange
        .Select ' Vælg boogmærket
        .PasteSpecial Link:=False, _
            DataType:=wdPasteMetafilePicture, _
            Placement:=wdInLine, _
            DisplayAsIcon:=False ' Indsæt Tabellen som et billede, ingen link
    End With
    
    ' Luk
    With wdDoc
        .SaveAs2 wbBook.Path & "\Word_Rapport_" & Format(Date, "dd_mm_yyyy") & ".docx", _
            FileFormat:=wdFormatDocumentDefault
        .Close ' Luk Dokument
    End With

    wdApp.Quit ' Luk word
    
End Sub
```