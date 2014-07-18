import unittest
import numpy


def factor(n, limit, prime_factors):
    #1. Create array of trial values
    a = numpy.ceil(numpy.sqrt(n))
    limit = min(n, limit)
    a = numpy.arange(a, a+limit)
    b2 = a**2 - n
    #2. Check whether b is a square
    fractions = numpy.modf(numpy.sqrt(b2))[0]
    #3. Find 0 fractions
    indices = numpy.where(fractions == 0)
    #4. find the first occurrence of a 0 fractions
    a = numpy.ravel(numpy.take(a, indices))
    if len(a) == 0:
        return prime_factors
    
    a = int(a[0])
    b = int(numpy.sqrt(a ** 2 - n))
    c = a + b
    d = a - b
    
    if c == 1 or d == 1:
        prime_factors.append(1,1)
        return [1,1]
    
    prime_factors += factor(c, limit, prime_factors)
    prime_factors += factor(d, limit, prime_factors)
    return [c,d]
    
class FactorTest(unittest.TestCase):


    def test_factor(self):
        prime_factors = []
        prime_factors += factor(1000, 1000, prime_factors)

        self.assertEqual(prime_factors,[10, 2, 50, 20])

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    suite = unittest.TestSuite()
    suite.addTests([FactorTest])
    unittest.TextTestRunner(verbosity=2).run(suite)