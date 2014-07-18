import unittest
import datetime
from matplotlib.finance import quotes_historical_yahoo
import numpy
import scipy.stats
import matplotlib.pyplot

class TradingPeriodicallyTest(unittest.TestCase):


    def test(self):
        #Get close prices.
        today = datetime.date.today()
        start = (today.year - 1, today.month, today.day)

        quotes = quotes_historical_yahoo('AAPL', start, today)
        close =  numpy.array([q[4] for q in quotes])

        #2. Get log returns.
        logreturns = numpy.diff(numpy.log(close))

        #3. Calculate breakout and pullback
        freq = 1/float(50)
        breakout = scipy.stats.scoreatpercentile(logreturns, 100 * (1 - freq) )
        pullback = scipy.stats.scoreatpercentile(logreturns, 100 * freq)

        print breakout
        print pullback
        print logreturns
        #4. Generate buys and sells
        buys = numpy.compress(logreturns < pullback, close)
        sells = numpy.compress(logreturns > breakout, close)
        profit = sells.sum() - buys.sum()

        print 'profit: from log_returns = %s' % profit
        #5. Plot a histogram of the log returns
        matplotlib.pyplot.hist(logreturns)
        # matplotlib.pyplot.show()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test']
    unittest.main()