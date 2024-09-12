### INF601 - Advanced Programming in Python
### Honesty Beaton
### Mini Project 1
"""
 Using API's, NumPy and MatPlotLib to track and display the closing price off
 5 stock tickers as a graph for the last 10 trading days
"""

import numpy as np
import matplotlib.pyplot as plt #used to do graphs in python
from datetime import datetime, timedelta
import yfinance as yf
import os

# Variables to hold today's date and ten days ago's date
today = datetime.now()
ten_days_ago = today - timedelta(days=15) # accounts for any weekends

# List of strings of my five selected stock tickers to track their closing prices
myTickers = ["MSFT", "AAPL", "NVDA", "SPOT", "AMZN"]

# empty dictionary to
myData = {}
os.makedirs("charts/", exist_ok=True)

'''
This for loop loops through all of the tickers in myTickers, grabs the 'Close" key containing the closing price
for each, and adds it to the list lastTenDays. 
Then, lastTenDays is turned into a NumPy array, and graph's are plotted using Matplotlib
to show the closing price of each stock over the last 10 trading days.
'''
for ticker in myTickers:
    # returns Ticker information from yFinance API
    result = yf.Ticker(ticker)

    hist = result.history(start = ten_days_ago, end = today)

    lastTenDays = [] #empty list

    # loops through the current ticker's history by date to grab the closing price
    for date in hist['Close'][:11]:
        lastTenDays.append(date) # appends this information to a list

        if len(lastTenDays) == 10:
            #list is turned into numpy array
            myArray = np.array(lastTenDays)

            # maxPrice and minPrice y-values are allowed a buffer of 5%
            maxPrice = myArray.max() + (myArray.max() * .05)
            minPrice = myArray.min() - (myArray.min() * .05)

            # Each Ticker chart is labeled and plotted
            plt.plot(myArray)
            plt.xlabel("Days Ago")
            plt.ylabel("Closing Price")
            plt.axis((10, 1, minPrice, maxPrice))
            plt.title(f'{ticker} Last 10 Closing Prices')

            # Each Ticker chart is saved as the ticker name as a .png file in charts/
            plt.savefig(f'charts/{ticker}.png')

            print(f"New chart created for ticker {ticker} has been saved in charts/{ticker}.png")

print("Thank you, goodbye!")


