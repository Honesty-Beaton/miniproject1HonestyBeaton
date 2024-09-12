### INF601 - Advanced Programming in Python
### Honesty Beaton
### Mini Project 1
### Using API's and NumPy
import numpy as np
import matplotlib.pyplot as plt #used to do graphs in python
from datetime import datetime, timedelta
import yfinance as yf
import os

from pandas import period_range
today = datetime.now()
ten_days_ago = today - timedelta(days=15) # accounts for any weekends
myTickers = ["MSFT", "AAPL", "NVDA", "SPOT", "AMZN"] # List of my five selected tickers to track their closing prices
#myTickers.sort()
aapl = yf.Ticker("AAPL")
# print(aapl.info['dayHigh'])

myData = {}
os.makedirs("charts/", exist_ok=True)
for ticker in myTickers:
    result = yf.Ticker(ticker)
    #hist = result.history(period="5d")
    hist = result.history(start = ten_days_ago, end = today)

    lastTenDays = []
    for date in hist['Close'][:11]:
        lastTenDays.append(date)
        if len(lastTenDays) == 10:
            myArray = np.array(lastTenDays)

            #maxPrice = myArray.max() + 10
            maxPrice = myArray.max() + (myArray.max() * .05)
            minPrice = myArray.min() - (myArray.min() * .05)

            plt.plot(myArray)
            plt.xlabel("Days Ago")
            plt.ylabel("Closing Price")
            plt.axis((10, 1, minPrice, maxPrice))
            plt.title(f'{ticker} Last 10 Closing Prices')

            plt.savefig(f'charts/{ticker}.png')
            # plt.show()
        else:
            print(f"Do not have 10 days of data. Only have {len(lastTenDays)}")

    #pprint.pprint(myArray)
    #print(hist['Close'])
 #   myData[ticker] = {'ticker': ticker, 'dayHigh': result.info['dayHigh']} #dictionary to store ticker information
  #  print(f"Ticker:  {ticker} \tDaily High: {result.info['dayHigh']}")


#msft = yf.Ticker("MSFT") #finance ticker for microsoft

# get all stock info
# pprint.pprint(msft.info) # returns dictionary

# get historical market data for last 1mo
# hist = msft.history(period="1mo") # returns PANDAS frame
# trim to last 10

# pprint.pprint(hist)

