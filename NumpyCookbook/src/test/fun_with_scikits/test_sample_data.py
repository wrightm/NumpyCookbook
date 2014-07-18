import unittest
from sklearn import datasets

class SampleDataTest(unittest.TestCase):


    def test(self):
        boston_prices = datasets.load_boston()
        self.assertEqual(boston_prices.data.shape, (506, 13))
        self.assertEqual(boston_prices.data.max(), 711.0)
        self.assertEqual(boston_prices.data.min(), 0.0)
        self.assertEqual(boston_prices.target.shape, (506,))
        self.assertEqual(boston_prices.target.max(), 50.0) 
        self.assertEqual(boston_prices.target.min(), 5.0)



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()