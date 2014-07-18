from matplotlib.finance import quotes_historical_yahoo
from datetime import date
import numpy
from binomial_proportion import pos_confidence

#1. Get close prices.
today = date.today()
start = (today.year - 1, today.month, today.day)

quotes = quotes_historical_yahoo('AAPL', start, today)
close =  numpy.array([q[4] for q in quotes])
print pos_confidence(close)
