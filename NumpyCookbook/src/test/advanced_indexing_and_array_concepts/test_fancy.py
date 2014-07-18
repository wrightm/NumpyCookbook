'''
Created on 6 Jul 2014

@author: wrightm
'''
import unittest
import scipy.misc
import matplotlib.pyplot


class FancyTest(unittest.TestCase):


    def test(self):
        # Load the Lena array
        lena = scipy.misc.lena()
        xmax = lena.shape[0]
        ymax = lena.shape[1]

        # Fancy indexing
        # Set values on diagonal to 0
        # x 0-xmax
        # y 0-ymax
        lena[range(xmax), range(ymax)] = 0

        # Set values on other diagonal to 0
        # x xmax-0
        # y 0-ymax
        lena[range(xmax-1,-1,-1), range(ymax)] = 0

        # Plot Lena with diagonal lines set to 0
        matplotlib.pyplot.imshow(lena)
        # matplotlib.pyplot.show()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test']
    unittest.main()