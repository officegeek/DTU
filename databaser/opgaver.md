---
layout: default
title: Opgaver til 06-10-2022 - Database
nav_order: 1
has_children: false
---
<span class="fs-1">
[HOME](./online-06102022.md){: .btn .btn-blue }
</span>

# Opgaver til den 06-10-2022

# SQL Opgaver
Du skal bruge databasen Northwind til alle opgaverne. Det er SQL sætningerne du skal skrive i Workbench.

Du finder løsningen i SQL filen **opgaver06102022.sql**. Denne fil kan du åbne i Workbench - **Men prøv nu lige selv først!**

## Opgave 1
Vælg følgende felter fra tabellen: Customers
- CustomerId
- CompanyName
- ContactName
- Country
*Resultat: 93 Rows*     

## Opgave 1
Find alle lande der er sendt en ordre til, vis dem kun én gang, ud fra tabellen: Orders
*Resultat: 21 Rows*

## Opgave 2
List alle Produkter fra tabellen Products.
Sorter faldende efter feltet UnitPrice
*Res

## Opgave 3
Find alle Customeres fra UK og Spain.
Brug tabellen Customers
*Resultat: 12 Rows*

## Opgave 4
Find alle Products hvor vi har mere end 100 på lager (UnitsInStock) og prisen (UnitPrice) er større end eller lig med 25.
Brug tabellen Products
*Resultat: 2 Rows*

## Opgave 5
Find alle Products hvor prisen (UnitPrice) er større end eller lig med 25.
Brug tabellen Products
*Resultat: 29*

## Opgave 6
Find alle Ordres der er har en Ordre Date i 10 måned af 1996.
Brug tabellen Orders
*Resultat: 26 Rows*

## Opgave 7
Find alle Orders hvor ShipRegion er blank, ShipCountry=Germany, Freight er større end eller lig med 100, EmployeeID = 1 og OrdreDate er fra 1996.
Brug tabellen Orders
*Resultat: 2 Rows*