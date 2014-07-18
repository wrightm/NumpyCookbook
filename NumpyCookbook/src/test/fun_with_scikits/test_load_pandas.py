'''
Created on 16 Jul 2014

@author: wrightm
'''
import unittest
import statsmodels.api


class LoadPandasTest(unittest.TestCase):


    def test(self):
        # See https://github.com/statsmodels/statsmodels/tree/master/statsmodels/datasets
        data = statsmodels.api.datasets.copper.load_pandas()

        print data
        x, y = data.exog, data.endog
        fit = statsmodels.api.OLS(y, x).fit()
        print "Fit params", fit.params
        print
        print "Summary"
        print
        print fit.summary()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()