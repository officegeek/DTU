---
layout: default
title: Time Intelligence Formulas
parent: Power-BI
has_children: false
nav_order: 50
---

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

# Power BI Time Intelligence Formulas Using Today
The user does want to have a date slicer or filter. Also, the user does not want to control the measures based on the last date of the calendar. Formulas should use today's date and provide **Today, yesterday, WTD, MTD, QTD, YTD sales**

These formulas do not use all to remove filters on the date table; for example filters (all('Date'), <filter code>), because the assumption is no date is selected. Otherwise, you have to use all on date

## Day Level Formulas using Today

```dax
Today = CALCULATE([Net], FILTER('Date','Date'[Date] = Today() ) )

Yesterday = CALCULATE([Net], FILTER('Date','Date'[Date] = Today()-1 ) )

Same day Last week Today= CALCULATE([Net], FILTER('Date','Date'[Date] = Today()-7 ) ) 

Month Start Date Today = CALCULATE([Net], FILTER('Date','Date'[Date] = Eomonth(Today(),-1)+1 ) )

Month End Date Today = CALCULATE([Net], FILTER('Date','Date'[Date] = Eomonth(Today(),0) ) )

Last Month End Date Today = CALCULATE([Net], FILTER('Date','Date'[Date] = Eomonth(Today(),-1) ) )

Last Month End Date Today = CALCULATE([Net], FILTER('Date','Date'[Date] = Eomonth(Today(),-1) ) )

Last year same WeekDay = CALCULATE([Net], FILTER('Date','Date'[Date] = Today()-364 ) )

Last year same date = CALCULATE([Net], FILTER('Date','Date'[Date] = date(Year(Today())-1, month(Today()), day(Today()) )))
```

## Month Level Formulas using Today
 
```dax
MTD Today = 
var _min = eomonth(today(),-1)+1
var _max =  today() 
return 
CALCULATE([Net], FILTER('Date','Date'[Date] >=_min && 'Date'[Date] <= _max))

LMTD Today= 
var _min = eomonth(today(),-2)+1
var _max1 = today()
var _max = date(year(_max1),month(_max1)-1, day(_max1))
return 
CALCULATE([Net], FILTER('Date','Date'[Date] >=_min && 'Date'[Date] <= _max))

LYMTD Today = 
var _min = eomonth(today(),-13)+1
var _max1 = today()
var _max = date(year(_max1)-1,month(_max1), day(_max1))
return CALCULATE([Net], FILTER('Date','Date'[Date] >=_min && 'Date'[Date] <= _max))

MTD Yesterday = 
var _max =  today() -1
var _min = eomonth(_max,-1)+1
return CALCULATE([Net], FILTER('Date','Date'[Date] >=_min && 'Date'[Date] <= _max))

This Month Today = 
var _min = eomonth(today(),-1)+1
var _max =  eomonth(today(),0) 
return CALCULATE([Net], FILTER('Date','Date'[Date] >=_min && 'Date'[Date] <= _max))

Last Month Today = 
var _min = eomonth(today(),-2)+1
var _max =  eomonth(today(),-1) 
return CALCULATE([Net], FILTER('Date','Date'[Date] >=_min && 'Date'[Date] <= _max))

Same Month Last Year Today = 
var _min = eomonth(today(),-13)+1
var _max =  eomonth(today(),-12) 
return CALCULATE([Net], FILTER('Date','Date'[Date] >=_min && 'Date'[Date] <= _max))


First Month This year Today = 
var _min = eomonth(today(),-1*month(Today()))+1
var _max =  eomonth(today(),-1*month(Today())+1) 
return CALCULATE([Net], FILTER('Date','Date'[Date] >=_min && 'Date'[Date] <= _max))

Last Month Last year Today = 
var _min = eomonth(today(),-1*month(Today())-1)+1
var _max =  eomonth(today(),-1*month(Today())) 
return CALCULATE([Net], FILTER('Date','Date'[Date] >=_min && 'Date'[Date] <= _max))
```

## Quarter Level Formulas using Today
 
```dax
QTD Today = 
var _max = today()
var _min = eomonth(_max,-1* if( mod(Month(_max),3) =0,3,mod(Month(_max),3)))+1
return 
CALCULATE([Net], FILTER('Date','Date'[Date] >=_min && 'Date'[Date] <= _max))

QTD Yesterday = 
var _max = today()-1
var _min = eomonth(_max,-1* if( mod(Month(_max),3) =0,3,mod(Month(_max),3)))+1
return 
CALCULATE([Net], FILTER('Date','Date'[Date] >=_min && 'Date'[Date] <= _max))

LQTD Today = 
var _max = Date(year(today()), Month(Today())-3, day(today()))
var _min = eomonth(_max,-1* if( mod(Month(_max),3) =0,3,mod(Month(_max),3)))+1
return 
CALCULATE([Net], FILTER('Date','Date'[Date] >=_min && 'Date'[Date] <= _max))

LYQTD Today = 
var _max = Date(year(today())-1, Month(Today()), day(today()))
var _min = eomonth(_max,-1* if( mod(Month(_max),3) =0,3,mod(Month(_max),3)))+1
return 
CALCULATE([Net], FILTER('Date','Date'[Date] >=_min && 'Date'[Date] <= _max))

This Qtr Today = 
var _today = today()
var _max = eomonth(_today, if( mod(Month(_today),3) =0,0,3-mod(Month(_today),3)))
var _min = eomonth(_max,-3)+1
return 
CALCULATE([Net], FILTER('Date','Date'[Date] >=_min && 'Date'[Date] <= _max))

Last Qtr Today = 
var _today = today()
var _max = eomonth(_today, -1*if( mod(Month(_today),3) =0,3,mod(Month(_today),3)))
var _min = eomonth(_max,-3)+1
return 
CALCULATE([Net], FILTER('Date','Date'[Date] >=_min && 'Date'[Date] <= _max))

Same Qtr Last Year Today = 
var _today = today()
var _max = eomonth(eomonth(_today, if( mod(Month(_today),3) =0,0,3-mod(Month(_today),3))),-12)
var _min = eomonth(_max,-3)+1
return 
CALCULATE([Net], FILTER('Date','Date'[Date] >=_min && 'Date'[Date] <= _max))

First Qtr This year Today = 
var _min = eomonth(today(),-1*month(Today()))+1
var _max =  eomonth(_min,2) 
return CALCULATE([Net], FILTER('Date','Date'[Date] >=_min && 'Date'[Date] <= _max))

Last Qtr Last year Today = 
var _max = eomonth(today(),-1*month(Today()))
var _min =  eomonth(_max,-3)+1 
return CALCULATE([Net], FILTER('Date','Date'[Date] >=_min && 'Date'[Date] <= _max))
```

## Year Level Formulas using Today
 
```dax
YTD Today = 
var _min = eomonth(today(),-1*month(today()))+1
var _max =  today() 
return 
CALCULATE([Net], FILTER('Date','Date'[Date] >=_min && 'Date'[Date] <= _max))

YTD Yesterday = 
var _min = eomonth(today(),-1*month(today()))+1
var _max =  today() -1
return 
CALCULATE([Net], FILTER('Date','Date'[Date] >=_min && 'Date'[Date] <= _max))

LYTD Today = 
var _today = TODAY()
var _max =  date(year(_today)-1, month(_today), day(_today))
var _min = eomonth(_max,-1*month(_max))+1
return 
CALCULATE([Net], FILTER('Date','Date'[Date] >=_min && 'Date'[Date] <= _max))

LYTD Yesterday = 
var _today = TODAY()-1
var _max =  date(year(_today)-1, month(_today), day(_today))
var _min = eomonth(_max,-1*month(_max))+1
return 
CALCULATE([Net], FILTER('Date','Date'[Date] >=_min && 'Date'[Date] <= _max))

This year Today = 
var _min = eomonth(today(),-1*month(today()))+1
var _max =  eomonth(_min,11) 
return 
CALCULATE([Net], FILTER('Date','Date'[Date] >=_min && 'Date'[Date] <= _max))

Last year Today = 
var _max = eomonth(today(),-1*month(today()))
var _min =  eomonth(_max,-12)+1 
return 
CALCULATE([Net], FILTER('Date','Date'[Date] >=_min && 'Date'[Date] <= _max))

2nd Last year Today = 
var _max = eomonth(today(),(-1*month(today()))-12)
var _min =  eomonth(_max,-12)+1 
return 
CALCULATE([Net], FILTER('Date','Date'[Date] >=_min && 'Date'[Date] <= _max))
```

 

## Week Level Formulas using Today
 
```dax
WTD Today = 
var _min = TODAY() -WEEKDAY(TODAY(),2) +1 //Monday week start
var _max =  today() 
return CALCULATE([Net], FILTER('Date','Date'[Date] >=_min && 'Date'[Date] <= _max))

LWTD Today = 
var _min = TODAY() -WEEKDAY(TODAY(),2) -6 //Monday week start
var _max =  today() -7
return CALCULATE([Net], FILTER('Date','Date'[Date] >=_min && 'Date'[Date] <= _max))

LYWTD Today = 
var _max =  today() -364
var _min = _max -WEEKDAY(_max,2) +1//Monday week start
return CALCULATE([Net], FILTER('Date','Date'[Date] >=_min && 'Date'[Date] <= _max))

WTD Yesterday = 
var _max =  today() -1
var _min = _max -WEEKDAY(_max,2) +1 //Monday week start
return CALCULATE([Net], FILTER('Date','Date'[Date] >=_min && 'Date'[Date] <= _max))

LWTD Yesterday = 
var _max =  today() -8
var _min = _max -WEEKDAY(_max,2) +1 //Monday week start
return CALCULATE([Net], FILTER('Date','Date'[Date] >=_min && 'Date'[Date] <= _max))

LYWTD Yesterday = 
var _max =  today() -364
var _min = _max -WEEKDAY(_max,2) +1//Monday week start
return CALCULATE([Net], FILTER('Date','Date'[Date] >=_min && 'Date'[Date] <= _max))

This Week Today = 
var _min = today() -WEEKDAY(today() ,2) +1 //Monday week start
var _max =  _min +6
return CALCULATE([Net], FILTER('Date','Date'[Date] >=_min && 'Date'[Date] <= _max))

Last Week Today = 
var _min = today() -WEEKDAY(today() ,2) -6 //Monday week start
var _max =  _min +6
return CALCULATE([Net], FILTER('Date','Date'[Date] >=_min && 'Date'[Date] <= _max))

Last year same week Today = 
var _today =  today() -364
var _min = _today -WEEKDAY(_today,2) +1//Monday week start
var _max = _min+6
return CALCULATE([Net], FILTER('Date','Date'[Date] >=_min && 'Date'[Date] <= _max))
```