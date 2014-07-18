'''
Created on 11 Jul 2014

@author: wrightm
'''
import unittest
import numpy
from numpy.core.numeric import asanyarray


def double(a):
    return 2*a

def diff(a, n=1, axis=-1, skip=1):
    if n == 0:
        return a
    if n < 0:
        raise ValueError(
                "order must be non-negative but got " + repr(n))

    a = asanyarray(a)
    nd = len(a.shape)
    # print 'nd', nd
    slice1 = [slice(None)]*nd
    # print '1st slice1', slice1
    slice2 = [slice(None)]*nd
    # print '1st slice2', slice2
    slice1[axis] = slice(skip, None)
    # print '2nd slice1', slice1
    slice2[axis] = slice(None, -skip)
    # print '2nd slice2', slice2
    slice1 = tuple(slice1)
    # print '3rd slice1', slice1
    slice2 = tuple(slice2)
    # print '3rd slice2', slice2
    if n > 1:
        # print 'n>1: a[slice1] = ', a[slice1]
        # print 'n>1: a[slice2] = ', a[slice2]
        # print 'n>1: a[slice1]-a[slice2] = ', a[slice1]-a[slice2]
        return diff(a[slice1]-a[slice2], n-1, axis=axis)
    else:
        # print 'n <= 1: a[slice1] = ', a[slice1]
        # print 'n <= 1: a[slice2] = ', a[slice2]
        # print 'n <= 1: a[slice1]-a[slice2] = ', a[slice1]-a[slice2]
        return a[slice1]-a[slice2]



class CreateUnfuncTest(unittest.TestCase):


    def test(self):
        ufunc = numpy.frompyfunc(double, 1, 1)
        numpy.testing.assert_array_equal(ufunc(numpy.arange(4)), numpy.array([0,2,4,6]))

    def test_diff(self):
        print diff(numpy.array([[1,2,3,4],[5,6,7,8]]), skip=2)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()