'''
Created on 16 Jul 2014

@author: wrightm
'''
import unittest
import datetime
from matplotlib import finance
import numpy
from statsmodels.stats.adnorm import normal_ad


class NormalityTest(unittest.TestCase):


    def test(self):
        #1. Download price data

        # 2011 to 2012
        start = datetime.datetime(2011, 01, 01)
        end = datetime.datetime(2012, 01, 01)

        quotes = finance.quotes_historical_yahoo('AAPL', start, end, asobject=True)

        close = numpy.array(quotes.close).astype(numpy.float)
        self.assertAlmostEqual(normal_ad(numpy.diff(numpy.log(close)))[0], 0.57, 2)
        self.assertAlmostEqual(normal_ad(numpy.diff(numpy.log(close)))[1], 0.13, 2)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()