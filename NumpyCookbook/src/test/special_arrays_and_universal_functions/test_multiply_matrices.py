'''
Created on 11 Jul 2014

@author: wrightm
'''
import unittest
import numpy


class Test(unittest.TestCase):


    def testName(self):
        x = numpy.ones((2, 1)) 
        y = numpy.ones((1, 2)) 
        self.assertEqual(numpy.dot(x, y).shape, (2,2))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()