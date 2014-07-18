'''
Created on 7 Jul 2014

@author: wrightm
'''
import unittest
import numpy


golden_ratio = (1+numpy.sqrt(5))/2
psi_ratio = (1-numpy.sqrt(5))/2

def fibonacci(n_numbers):
    n = numpy.arange(1, n_numbers+1)
    fib = (golden_ratio**n - psi_ratio**n) / numpy.sqrt(5)
    return fib.astype(int)

class FibonacciTest(unittest.TestCase):


    def test_fibonacci(self):
        
        fib = fibonacci(12)
        numpy.testing.assert_array_equal(fib, [  1,   1,   2,   3,   5,   8,  13,  21,  34,  55,  89, 144])

    def test_fibonacci_even(self):
        fib = fibonacci(12)
        even_terms = fib[(fib % 2 == 0)]
        numpy.testing.assert_array_equal(even_terms, [2,8,34,144])

    def test_fibonacci_sum(self):
        fib = fibonacci(12)
        even_terms = fib[(fib % 2 == 0)]
        numpy.testing.assert_array_equal(even_terms.sum(), 188)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    suite = unittest.TestSuite()
    suite.addTests([FibonacciTest])
    unittest.TextTestRunner(verbosity=2).run(suite)