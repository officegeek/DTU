---
layout: default
title: Opgaver til 06-10-2022 - JOIN
nav_order: 1
parent: Online-06-10-2022-Database
has_children: false
---
<span class="fs-1">
[HOME](./online-06102022.md){: .btn .btn-blue }
</span>

# JOIN opgaver
Du skal bruge databasen Northwind til alle opgaverne. Det er SQL sætningerne du skal skrive i Workbench.

Du skal bruge **INNER JOIN** for at løse alle opgaverne

Du finder løsningen i SQL filen [join-opgave.sql](./filer/join-opgave.sql). Denne fil kan du åbne i Workbench - **Men prøv nu lige selv først!**

## Opgave 1
- Opret en SELECT sætning der viser følgende felter:
    - Products.ProductID
    - Products.ProductName
    - Categories.CategoryName
- *Resultat: 77 Rows*

## Opgave 2
- Opret en SELECT sætning der viser følgende felter:
    - Products.ProductID
    - Products.ProductName
    - Suppliers.CompanyName
- *Resultat: 77 Rows*

## Opgave 3
Opret en SELECT sætning der viser følgende felter:
    - Orders.OrderID
    - Customers.CompanyName
    - Name som består af Employees.FirstName og Employees.LastName (*sat sammen*)
- *Resultat: 830 Rows*

## Opgave 4
- Opret en SELECT sætning der indeholder følgende felter:
    - OrderId
    - CompanyName
    - ProductName
- *Resultat: 2.155 Rows*

## Opgave 5
- Find alle Products (*ProductName og ProductID*)
- Der er solgt i maj måned 1997
- *Resultat: 96 Rows*