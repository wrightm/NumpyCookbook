'''
Created on 9 Jul 2014

@author: wrightm
'''
import unittest
import numpy
from matplotlib.finance import quotes_historical_yahoo
import datetime
import matplotlib.pyplot

def get_indices(high, size):
    #2. Generate random indices
    return numpy.random.randint(0, high, size)

class Test(unittest.TestCase):


    def test(self):
        #1. Get close prices.
        today = datetime.date.today()
        start = (today.year - 1, today.month, today.day)

        quotes = quotes_historical_yahoo('AAPL', start, today)
        close =  numpy.array([q[4] for q in quotes])

        nbuys = int(5)
        N = int(10000)
        profits = numpy.zeros(N)

        for i in xrange(N):
            #3. Simulate trades
            buys = numpy.take(close, get_indices(len(close), nbuys))
            sells = numpy.take(close, get_indices(len(close), nbuys))
            profits[i] = sells.sum() - buys.sum()

        print "Mean", profits.mean() 
        print "Std", profits.std()

        #4. Plot a histogram of the profits
        matplotlib.pyplot.hist(profits)
        matplotlib.pyplot.show()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test']
    unittest.main()