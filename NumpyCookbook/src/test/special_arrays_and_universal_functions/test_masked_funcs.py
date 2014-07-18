'''
Created on 11 Jul 2014

@author: wrightm
'''
import unittest
from matplotlib.finance import quotes_historical_yahoo
import datetime
import numpy
import matplotlib.pyplot

def get_close(ticker):
    today = datetime.date.today()
    start = (today.year - 1, today.month, today.day)

    quotes = quotes_historical_yahoo(ticker, start, today)

    return numpy.array([q[4] for q in quotes])

class ExtremeValueMaskedFuncTest(unittest.TestCase):

    def test(self):
        close = get_close('AAPL')

        triples = numpy.arange(0, len(close), 3)
        print "Triples", triples[:10], "..."

        signs = numpy.ones(len(close))
        print "Signs", signs[:10], "..."

        signs[triples] = -1
        print "Signs", signs[:10], "..."

        ma_log = numpy.ma.log(close * signs)
        print "Masked logs", ma_log[:10], "..."

        dev = close.std()
        avg = close.mean()
        inside = numpy.ma.masked_outside(close, avg - dev, avg + dev)
        print "Inside", inside[:10], "..."
        outside = numpy.ma.masked_inside(close, avg-dev, avg + dev)
        print "Outside", outside[:10], "..."

        matplotlib.pyplot.subplot(411)
        matplotlib.pyplot.title("Original")
        matplotlib.pyplot.plot(close)

        matplotlib.pyplot.subplot(412)
        matplotlib.pyplot.title("Log Masked")
        matplotlib.pyplot.plot(numpy.exp(ma_log))

        matplotlib.pyplot.subplot(413)
        matplotlib.pyplot.title("Not Extreme")
        matplotlib.pyplot.plot(inside)
        
        matplotlib.pyplot.subplot(414)
        matplotlib.pyplot.title("Extreme")
        matplotlib.pyplot.plot(outside)

        matplotlib.pyplot.show()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()