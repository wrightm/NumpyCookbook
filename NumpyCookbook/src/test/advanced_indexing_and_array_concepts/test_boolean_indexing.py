'''
Created on 6 Jul 2014

@author: wrightm
'''
import unittest
import numpy
import scipy.misc
import matplotlib.pyplot


class BooleanIndexingTest(unittest.TestCase):

    def get_indices(self, size):
        arr = numpy.arange(size)
        return arr % 4 == 0
    
    def test(self):
        # Plot Lena
        lena1 = scipy.misc.lena().copy() 
        xindices = self.get_indices(lena1.shape[0])
        yindices = self.get_indices(lena1.shape[1])
        lena1[xindices, yindices] = 0
        matplotlib.pyplot.subplot(211)
        matplotlib.pyplot.imshow(lena1)

        lena2 = scipy.misc.lena().copy() 
        # Between quarter and 3 quarters of the max value
        lena2[(lena2 > lena2.max()/4) & (lena2 < 3 * lena2.max()/4)] = 0
        matplotlib.pyplot.subplot(212)
        matplotlib.pyplot.imshow(lena2)

        matplotlib.pyplot.show()

        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()