'''
Created on 16 Jul 2014

@author: wrightm
'''
import unittest
from sklearn.datasets.base import load_sample_images
from skimage.feature._harris import harris
import numpy
from matplotlib.pyplot import axis, imshow, plot, show


class CornerDetectionTest(unittest.TestCase):


    def test(self):
        dataset = load_sample_images()
        img = dataset.images[0] 
        harris_coords = harris(img)
        print "Harris coords shape", harris_coords.shape
        y, x = numpy.transpose(harris_coords)
        axis('off')
        imshow(img)
        plot(x, y, 'ro')
        show()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test']
    unittest.main()