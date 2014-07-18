'''
Created on 6 Jul 2014

@author: wrightm
'''
import unittest
import scipy.misc
import matplotlib.pyplot



class CopyViewTest(unittest.TestCase):

    def setUp(self):
        self.lena = scipy.misc.lena()
        self.copy = self.lena.copy()
        self.view = self.lena.view()
        
    def test(self):
        
        # Plot the Lena array
        matplotlib.pyplot.subplot(221)
        matplotlib.pyplot.imshow(self.lena)

        #Plot the copy
        matplotlib.pyplot.subplot(222)
        matplotlib.pyplot.imshow(self.copy)

        #Plot the view
        matplotlib.pyplot.subplot(223)
        matplotlib.pyplot.imshow(self.view)

        # Plot the view after changes
        self.view.flat = 0
        matplotlib.pyplot.subplot(224)
        matplotlib.pyplot.imshow(self.view)

        # matplotlib.pyplot.show()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()