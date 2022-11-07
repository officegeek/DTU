# Makro Eksempler
Her er nogle eksempler på makroer der kan gøre dit daglige arbejde i Excel lidt nemmere.

## Beskyt Ark
Denne makro beskytter alle ark på en gang, hvilket ikk er muligt uden en makro.

```basic
Sub BeskytAlleArk()
    ' Variable
    Dim ws As Worksheet
    Dim MyPassWord As String
    
    ' Password - Erstat med dit eget
    MyPassWord = "Test123"
    
    ' Gennemløb af alle ark
    For Each ws In Worksheets
        ws.Protect PassWord:=MyPassWord
    Next ws
End Sub
```
Når du har en makro der kan beskytte alle ark, giver det også mening at have en makro der kan fjerne denne beskyttelse.

```basic
Sub FjernBeskytAlleArk()
    ' Variable
    Dim ws As Worksheet
    Dim MyPassWord As String
    
    ' Password - Erstat med dit eget
    MyPassWord = "Test123"
    
    ' Gennemløb af alle ark
    For Each ws In Worksheets
        ws.Unprotect PassWord:=MyPassWord
    Next ws
End Sub
```

## Fjern fletning af alle flettede celler
Det er almindelig praksis at flette celler for f.eks. at oprette en overskrift eller lign. Det giver dog problemer hvis du f.eks. skal sortere dine data.

For at gøre det nemt at fjerne alle flettede celler, fra det aktive ark, på en gang kan du bruge denne makro.

```basic
Sub FjernFlettedeCeller()
    ActiveSheet.Cells.UnMerge
End Sub
```

Denne makro kan nemt udvides til at gøre det sammen fro alle ark.

## Gem Excel fil med Dato og Tid
Når du arbejder med en Excel fil kan det nogle gange være nyttigt at gemme forskellige versioner af din Excel fil.

Brug af tidsstempler giver dig mulighed for at gå tilbage til en bestemt fil for at se, hvilke ændringer der blev foretaget, eller hvilke data der blev brugt.

Denne makro gemmer filen i sammen mappe med navneformatet: **23-11-2022_10-22-45.xlsx**

```basic
Sub GemExcelFilMedDatoTid()
    ' Variable
    Dim timestamp As String
    
    ' Dato og Tid
    timestamp = Format(Date, "dd-mm-yyyy") & "_" & Format(Time, "hh-mm-ss")
    
    ' Gem i samme mappe
    ThisWorkbook.SaveAs timestamp
End Sub
```

**Note**: Du kan evt. ændre navnet så der også inkludere et "*rigtigt*" navn, der f.eks. relater til dit projekt.


## Gem som PDF
Hvis du vil printe de forskellige ark som selvstændige Excel filer, en PDF fil for hvert ark, er det desværre en tidskrævende proces.

Denne marko printer alle ark i Excel filen som en selvstændig PDF fil, med arknavnet som navn på PDF filen.

```basic
Sub PrintArkPDF()
    ' Variable
    Dim ws As Worksheet
    
    ' Loop over alle ark og gem
    For Each ws In Worksheets
        ws.ExportAsFixedFormat xlTypePDF, ws.Name & ".pdf"
    Next ws
End Sub
```

**Note**: Fra print menuen er det muligt at printe alle ark som en samlet PDF file, men ikke en PDF fil for hvert ark.

## Ændre tekst til store bogstaver
Excel har en funktion der kan ændre en celles tekst til store bogstaver, i en anden celle.

Denne makro ændre teksten til store bogstaver i de markerede celler.

```basic
Sub StoreBogstaver()
    ' Variable
    Dim Rng As Range
    
    ' Loop over de celler der er valgt
    For Each Rng In Selection.Cells
        ' Check om det er en formel
        If Rng.HasFormula = False Then
            Rng.Value = UCase(Rng.Value)
        End If
    Next Rng
End Sub
```

Du kan meget nemt ændrer denne makro til små bogstaver - Erstat **UCase** med **LCase**: *LCase(Rng.Value)*

## Marker blanke celler
Du kan bruge betingetformatering til at markere blanke celler i et område, hvis du ikke ønsker at det er dynamisk eller bare vil gøre det nemt for en brugere, kan du bruge denne makro.

```basic
Sub MarkerBlankeCeller()
    ' Variable
    Dim Rng As Range
    ' Marker med Grøn baggrund
    Set Rng = Selection
    Rng.SpecialCells(xlCellTypeBlanks).Interior.Color = vbGreen
End Sub
```

## Sorter ark
Denne makro sortere dine ark alfabetisk

```basic
Sub SorterArkAlfabetisk()
    ' Variable
    Dim AntalArk As Integer
    Dim i As Integer
    Dim j As Integer
    
    ' Antal ark
    AntalArk = Sheets.Count
    
    ' Loop over alle ark
    For i = 1 To AntalArk - 1
        For j = i + 1 To AntalArk
            ' Flyt ark
            If Sheets(j).Name < Sheets(i).Name Then
                Sheets(j).Move before:=Sheets(i)
            End If
        Next j
    Next i
End Sub
```

# Funktioner - User Define Functions
Excel her over 200 indbyggede funktioner men det er også muligt at oprette dine egne funktioner - **User Define Functions**.

Du brugere dine egne funktioner på sammen måde som de indbyggede i Excel.

## Vis kun tal fra en celle
Med denne funktion kan du udtrække alle tal.

```basic
Function FindTal(CellRef As String)
    ' Variable
    Dim TekstLen As Integer
    Dim i As Integer
    Dim Tal As Double
    
    ' Find længden af teksten
    TekstLen = Len(CellRef)
    
    ' Gennemløb af teksten
    For i = 1 To TekstLen
        If IsNumeric(Mid(CellRef, i, 1)) Then
            Tal = Tal & Mid(CellRef, i, 1)
        End If
    Next i
    
    ' Retuner
    FindTal = Tal
End Function
```