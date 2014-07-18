'''
Created on 16 Jul 2014

@author: wrightm
'''
import unittest
import datetime
from matplotlib.finance import quotes_historical_yahoo
import numpy
import sklearn.cluster


class ClusteringTest(unittest.TestCase):


    def test(self):
        # 2011 to 2012
        start = datetime.datetime(2011, 01, 01)
        end = datetime.datetime(2012, 01, 01)

        #Dow Jones symbols
        symbols = ["AA", "AXP", "BA", "BAC", "CAT",
                   "CSCO", "CVX", "DD", "DIS", "GE", "HD",
                   "HPQ", "IBM", "INTC", "JNJ", "JPM",
                   "KO", "MCD", "MMM", "MRK", "MSFT", "PFE",
                   "PG", "T", "TRV", "UTX", "VZ", "WMT", "XOM"]

        quotes = [quotes_historical_yahoo(symbol, start, end, asobject=True)
                  for symbol in symbols]

        close = numpy.array([q.close for q in quotes]).astype(numpy.float)
        self.assertEqual(close.shape, (29,252))

        #2. Calculate affinity matrix
        logreturns = numpy.diff(numpy.log(close))
        self.assertEqual(logreturns.shape, (29, 251))

        logreturns_norms = numpy.sum(logreturns ** 2, axis=1)
        
        #print logreturns_norms.shape
        #print logreturns_norms[:, numpy.newaxis].shape
        #print logreturns_norms[numpy.newaxis, :].shape
        #print (logreturns_norms[:, numpy.newaxis] - logreturns_norms[numpy.newaxis, :]).shape
        #print logreturns.shape, logreturns.T.shape
        S = - logreturns_norms[:, numpy.newaxis] - logreturns_norms[numpy.newaxis, :] + 2 * numpy.dot(logreturns, logreturns.T)

        #3. Cluster using affinity propagation
        aff_pro = sklearn.cluster.AffinityPropagation().fit(S)
        labels = aff_pro.labels_

        d = {}
        for i in xrange(len(labels)):
            d[labels[i]] = []
            
        for i in xrange(len(labels)):
            d[labels[i]].append(symbols[i])       
            
        self.assertEqual(d, {0: ['BAC'], 1: ['CAT'], 2: ['CSCO'], 3: ['HPQ'], 4: ['AA', 'JPM'], 5: ['AXP', 'BA', 'CVX', 'DD', 'DIS', 'GE', 'MMM', 'TRV', 'UTX', 'XOM'], 6: ['HD', 'IBM', 'INTC', 'JNJ', 'KO', 'MCD', 'MRK', 'MSFT', 'PFE', 'PG', 'T', 'VZ', 'WMT']})     


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test']
    unittest.main()