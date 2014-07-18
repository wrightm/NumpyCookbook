import unittest
import numpy
import matplotlib.pyplot
import scipy.misc


class IXTest(unittest.TestCase):

    def shuffle_indices(self, size):
        arr = numpy.arange(size)
        numpy.random.shuffle(arr)

        return arr

    def test(self):
        
        lena = scipy.misc.lena()
        xmax = lena.shape[0]
        ymax = lena.shape[1]

        xindices = self.shuffle_indices(xmax)
        numpy.testing.assert_equal(len(xindices), xmax)
        yindices = self.shuffle_indices(ymax)
        numpy.testing.assert_equal(len(yindices), ymax)

        # Plot Lena
        matplotlib.pyplot.imshow(lena[numpy.ix_(xindices, yindices)])
        # matplotlib.pyplot.show()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()