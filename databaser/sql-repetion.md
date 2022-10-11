---
layout: default
title: SQL Opgaver til 13-10-2022 - SQL
nav_order: 1
parent: Database
has_children: false
---
<span class="fs-1">
[HOME](../README.md){: .btn .btn-blue }
</span>

# SQL Repetition
For lige at opfriske din SQL viden er der her 5 SQL opgaver som jeg vil anbefale dig at løse.

Du skal bruge den "*nye*" MySQL Server:

- Server name: **dtudatabase.mysql.database.azure.com**
- Login name: **dtuhellstern**
- Password: *Kommer på e-mail* - Password er kun gyldigt i en kort periode!

## Opgave 1
- Find de ordre der ikke er leveret til tiden, **ShippedeDate** er større end **RequiredDate**
- Brug tabellen: **orders**
- *Resultat: 37 rows*

## Opgave 2
- Find alle Ordre (*OrderDate*) fra **1997** i månederne **januar**, **februar**, **marts** og **april** fra **Canada** (*ShipCountry*). 
- Brug tabellen: **orderdetails**
- *Resultat: 8 rows*

## Opgave 3
- Find de 3 produkter vi har flest på lager af ud fra **products.UnitsInStock**
- *Resultat: ProductID = 75, 40, 6*

## Opgave 4
- Find de 3 produkter hvor vi har mest på lager i forhold til værdien af lageret
- *Resultat: ProductID = 38, 59, 12*

## Opgave 5
- Find de *Ordre* hvor **EmployeeID** er lig med **2**, **5** eller **8**. **ShipRegion** **ikke** er **NULL** og **ShipVia** enten er **1** eller **3**. 
- Skal sorteres først efter *EmployeeID* derefter *ShipVia*
- *Resultat: 57 rows*

# Vejledende løsning
Du kan hente en vejledende løsning her: [SQL_Repetition_Opgaver.sql](./filer/SQL_Repetition_Opgaver.sql)

Du kan åbne min løsnings-fil i MySQL Workbench

**Prøv først selv!**

