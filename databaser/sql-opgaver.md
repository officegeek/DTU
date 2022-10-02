---
layout: default
title: Opgaver til 06-10-2022 - SQL
nav_order: 1
parent: Online-06-10-2022
has_children: false
---
<span class="fs-1">
[HOME](./online-06102022.md){: .btn .btn-blue }
</span>

# SQL Opgaver til den 06-10-2022
Du skal bruge databasen Northwind til alle opgaverne. Det er SQL sætningerne du skal skrive i Workbench.

Du finder løsningen i SQL filen [sql-opgaver.sql](./filer/sql-opgaver.sql). Denne fil kan du åbne i Workbench - **Men prøv nu lige selv først!**

## Opgave 1
- Vælg følgende felter fra tabellen: Customers
    - CustomerId
    - CompanyName
    - ContactName
    - Country
-  *Resultat: 93 Rows*     

## Opgave 2
- Find alle lande der er sendt en ordre til, vis dem kun én gang.
- Brug tabellen Orders
- *Resultat: 21 Rows*

## Opgave 3
- List alle Produkter fra tabellen Products.
- Sorter faldende efter feltet UnitPrice
- *Resultat: 77 Rows*

## Opgave 4
- Find alle Customeres fra UK og Spain.
- Brug tabellen Customers
- *Resultat: 12 Rows*

## Opgave 5
- Find alle Products hvor vi har mere end 100 på lager (UnitsInStock) og prisen (UnitPrice) er større end eller lig med 25.
- Brug tabellen Products
- *Resultat: 2 Rows*

## Opgave 6
- Find alle Products hvor prisen (UnitPrice) er større end eller lig med 25.
- Brug tabellen Products
- *Resultat: 29*

## Opgave 7
- Find alle Ordres der er har en Ordre Date i 10 måned af 1996.
- Brug tabellen Orders
- *Resultat: 26 Rows*

## Opgave 8
- Find alle Orders hvor ShipRegion er blank, ShipCountry=Germany, Freight er større end eller lig med 100, EmployeeID = 1 og OrdreDate er fra 1996.
- Brug tabellen Orders
- *Resultat: 2 Rows*

## Opgave 9
- Find de ordre der ikke er leveret til tiden, ShippedeDate er større end RequiredDate
- Brug tabellen orders
- *Resultat: 37 Rows*

## Opgave 10
- Find de Ordre hvor EmployeeID er lig med 2, 5 eller 8.
- ShipRegion ikke er "tom/blank"
- ShipVia enten er 1 eller 3. 
- Skal sorteres først efter, EmployeeID derefter ShipVia begge acending
- Brug tabellen orders
- *Resultat: 57 Rows*