'''
Created on 11 Jul 2014

@author: wrightm
'''
import unittest
import matplotlib.pyplot
import numpy
import scipy.misc


class MaskedTest(unittest.TestCase):


    def test(self):
        lena = scipy.misc.lena()
        random_mask = numpy.random.randint(0, 2, size=lena.shape)

        matplotlib.pyplot.subplot(221)
        matplotlib.pyplot.title("Original")
        matplotlib.pyplot.imshow(lena)
        matplotlib.pyplot.axis('off')

        masked_array = numpy.ma.array(lena, mask=random_mask)

        matplotlib.pyplot.subplot(222)
        matplotlib.pyplot.title("Masked")
        matplotlib.pyplot.imshow(masked_array)
        matplotlib.pyplot.axis('off')

        matplotlib.pyplot.subplot(223)
        matplotlib.pyplot.title("Log")
        matplotlib.pyplot.imshow(numpy.log(lena))
        matplotlib.pyplot.axis('off')

        matplotlib.pyplot.subplot(224)
        matplotlib.pyplot.title("Log Masked")
        matplotlib.pyplot.imshow(numpy.log(masked_array))
        matplotlib.pyplot.axis('off')

        # matplotlib.pyplot.show()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()