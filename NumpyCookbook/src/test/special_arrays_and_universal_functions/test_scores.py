'''
Created on 11 Jul 2014

@author: wrightm
'''
import unittest
import datetime
from matplotlib.finance import quotes_historical_yahoo
import numpy

def get_close(ticker):
    today = datetime.date.today()
    start = (today.year - 1, today.month, today.day)

    quotes = quotes_historical_yahoo(ticker, start, today)

    return numpy.array([q[4] for q in quotes])

class Test(unittest.TestCase):


    def test(self):
        tickers = ['MRK', 'T', 'VZ']
        weights = numpy.recarray((len(tickers),), 
                                 dtype=[('symbol', numpy.str_, 16), 
                                        ('stdscore', float), ('mean', float), ('score', float)])
        # fill weights array
        for i in xrange(len(tickers)):
            close = get_close(tickers[i])
            logrets = numpy.diff(numpy.log(close))
            weights[i]['symbol'] = tickers[i]
            weights[i]['mean'] = logrets.mean()
            weights[i]['stdscore'] = 1/logrets.std()
            weights[i]['score'] = 0
        
        for key in ['mean', 'stdscore']:
            wsum = weights[key].sum()
            weights[key] = weights[key]/wsum

        weights['score'] = (weights['stdscore'] + weights['mean'])/2
        weights['score'].sort()

        for record in weights:
            print "%s,mean=%.4f,stdscore=%.4f,score=%.4f" % (record['symbol'], record['mean'], record['stdscore'], record['score'])

        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()