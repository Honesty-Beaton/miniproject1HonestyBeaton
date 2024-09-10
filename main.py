### INF601 - Advanced Programming in Python
### Honesty Beaton
### Mini Project 1
### Using API's and NumPy
import yfinance as yf
import pprint #for formatting dictionary

myTickers = ["MSFT", "AAPL", "NVDA", "SPOT", "AMZN"]
myTickers.sort()
aapl = yf.Ticker("AAPL")
# print(aapl.info['dayHigh'])

myData = {}
for ticker in myTickers:
    result = yf.Ticker(ticker)
    myData[ticker] = {'ticker': ticker, 'dailyHigh': result.info['dayHigh']} #dictionary to store ticker information
    print(f"Ticker:  {ticker} \tDaily High: {result.info['dayHigh']}")

pprint.pprint(myData)

#msft = yf.Ticker("MSFT") #finance ticker for microsoft

# get all stock info
# pprint.pprint(msft.info) # returns dictionary

# get historical market data for last 1mo
# hist = msft.history(period="1mo") # returns PANDAS frame
# trim to last 10

# pprint.pprint(hist)

