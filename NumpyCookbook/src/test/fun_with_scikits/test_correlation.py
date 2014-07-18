'''
Created on 17 Jul 2014

@author: wrightm
'''
import unittest
import datetime
from matplotlib import finance
import numpy
import pandas
from matplotlib.pyplot import legend, show


class CorrelationTest(unittest.TestCase):


    def test(self):
        # 2011 to 2012
        start = datetime.datetime(2011, 01, 01)
        end = datetime.datetime(2012, 01, 01)

        symbols = ["AA", "AXP", "BA", "BAC", "CAT"]

        quotes = [finance.quotes_historical_yahoo(symbol, start, end, asobject=True)
                  for symbol in symbols]

        close = numpy.array([q.close for q in quotes]).astype(numpy.float)
        dates = numpy.array([q.date for q in quotes])

        data = {}

        for i in xrange(len(symbols)):
            data[symbols[i]] = numpy.diff(numpy.log(close[i]))

        df = pandas.DataFrame(data, index=dates[0][:-1], columns=symbols)
 
        print df
        print df.corr()
        df.plot()
        legend(symbols)
        show()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test']
    unittest.main()