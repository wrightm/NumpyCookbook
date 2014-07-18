'''
Created on 17 Jul 2014

@author: wrightm
'''
import unittest
from matplotlib.pyplot import show
import pandas
import numpy
from matplotlib import finance
import datetime


class ResampleTest(unittest.TestCase):


    def test(self):
        # Download AAPL data for 2011 to 2012
        start = datetime.datetime(2011, 01, 01)
        end = datetime.datetime(2012, 01, 01)

        symbol = "AAPL"
        quotes = finance.quotes_historical_yahoo(symbol, start, end, asobject=True)

        # Create date time index
        dt_idx = pandas.DatetimeIndex(quotes.date)

        #Create data frame
        df = pandas.DataFrame(quotes.close, index=dt_idx, columns=[symbol])

        # Resample with monthly frequency
        resampled = df.resample('M', how=numpy.mean)
        print resampled 
 
        # Plot
        df.plot()
        resampled.plot()
        show()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()