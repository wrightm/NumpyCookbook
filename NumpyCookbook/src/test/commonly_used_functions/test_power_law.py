'''
Created on 9 Jul 2014

@author: wrightm
'''
import unittest
import datetime
import numpy
from matplotlib.finance import quotes_historical_yahoo
import matplotlib.pyplot


class LinearFitTest(unittest.TestCase):


    def test(self):
        
        #1. Get close prices.
        today = datetime.date.today()
        start = (today.year - 1, today.month, today.day)

        quotes = quotes_historical_yahoo('AAPL', start, today)
        close =  numpy.array([q[4] for q in quotes])

        #2. Get positive log returns.
        logreturns = numpy.diff(numpy.log(close))
        pos = logreturns[logreturns > 0]

        #3. Get frequencies of returns.
        counts, values = numpy.histogram(pos,bins=5)
        values = values[:-1] + (values[1] - values[0])/2
        freqs = 1.0/counts
        freqs =  numpy.log(freqs)

        #4. Fit the frequencies and returns to a line.
        p = numpy.polyfit(values,freqs, 1)

        #5. Plot the results.
        matplotlib.pyplot.plot(values, freqs, 'o')
        matplotlib.pyplot.plot(values, p[0] * values + p[1])
        # matplotlib.pyplot.show()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()