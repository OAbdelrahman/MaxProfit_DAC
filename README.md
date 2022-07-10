# MaxProfit_DAC

### Programming Language:
Python

### Purpose:
This program calculates the maximum profit of a given stock, <br>
and the buy and sell dates to get that profit.<br>

### Requirements:
* pandas

### How it works:
This program reads in two files: <br>
prices-split-adjusted.csv <br>
securities.csv <br>

Those two files have the stock data necessary to run the analysis.

In main(), you can hard code which function to run:<br>
getCompanyProfit(), which calculates the best of all stocks to buy. <br>
stockDetails(), which gets the best dates for a specific stock. Currently it's hard coded for "AAPL" (Apple). <br>

The program uses a Divide-and-Conquer algorithm to calculate maximum profit.
