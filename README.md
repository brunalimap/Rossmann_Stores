<h1 align="center"> Predict Sales Rossmann Stores </h1> 

<img align="center"  height="450" width="1000" src="https://github.com/brunalimap/DataScience_em_Producao/blob/main/img/img01.jpg" >

## 1.0 Context

<p> Rossmann operates over 3,000 drug stores in 7 European countries. Currently, Rossmann store managers are tasked with predicting their daily sales for up to six weeks in advance. Store sales are influenced by many factors, including promotions, competition, school and state holidays, seasonality, and locality. With thousands of individual managers predicting sales based on their unique circumstances, the accuracy of results can be quite varied. </p>

## 2.0 Business Challenge

<p> In a monthly meeting with managers, Store CFO Rossmann made the proposal to renovate all its stores. To carry out the renovations, the CFO needs to predict how much each store each store will sell in the next 6 weeks. </p>

## 3.0 Data fields


- <b>Id</b> - an Id that represents a (Store, Date) duple within the test set
- <b>Store</b> - a unique Id for each store
- <b>Sales</b> - the turnover for any given day (this is what you are predicting)
- <b>Customers</b> - the number of customers on a given day
- <b>Open</b> - an indicator for whether the store was open: 0 = closed, 1 = open
- <b>StateHoliday</b> - indicates a state holiday. Normally all stores, with few exceptions, are closed on state holidays. Note that all schools are closed on public holidays and weekends. a = public holiday, b = Easter holiday, c = Christmas, 0 = None
- <b>SchoolHoliday</b> - indicates if the (Store, Date) was affected by the closure of public schools
- <b>StoreType</b> - differentiates between 4 different store models: a, b, c, d
- <b>Assortment</b> - describes an assortment level: a = basic, b = extra, c = extended
- <b>CompetitionDistance</b> - distance in meters to the nearest competitor store
- <b>CompetitionOpenSince[Month/Year]</b> - gives the approximate year and month of the time the nearest competitor was opened
- <b>Promo</b> - indicates whether a store is running a promo on that day
- <b>Promo2</b> - Promo2 is a continuing and consecutive promotion for some stores: 0 = store is not participating, 1 = store is participating
- <b>Promo2Since[Year/Week]</b> - describes the year and calendar week when the store started participating in Promo2
- <b>PromoInterval</b> - describes the consecutive intervals Promo2 is started, naming the months the promotion is started anew. E.g. "Feb,May,Aug,Nov" means each round starts in February, May, August, November of any given year for that store




## 4.0 Solution - Telegram Bot

<img align="center" height="550" width="300" src="https://github.com/brunalimap/DataScience_em_Producao/blob/main/img/rossmann_video.gif">

## 5.0  References
Course Data Science em Produção - By Meigarom

## 6.0 Next steps:

- [ ] Translate of Notebook
- [ ] Preparation of README.md
- [ ] Project presentation
