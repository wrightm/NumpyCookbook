'''
Created on 11 Jul 2014

@author: wrightm
'''
import unittest
import numpy


class TripletsTest(unittest.TestCase):


    def test(self):
        #1. Create m and n arrays
        m = numpy.arange(33)
        n = numpy.arange(33)

        #2. Calculate a, b and c
        a = numpy.subtract.outer(m ** 2, n ** 2)
        b = 2 * numpy.multiply.outer(m, n)
        c = numpy.add.outer(m ** 2, n ** 2)

        #3. Find the index
        idx =  numpy.where((a + b + c) == 1000)

        #4. Check solution
        numpy.testing.assert_equal(a[idx]**2 + b[idx]**2, c[idx]**2)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()