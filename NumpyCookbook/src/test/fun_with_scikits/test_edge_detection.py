'''
Created on 16 Jul 2014

@author: wrightm
'''
import unittest
from sklearn.datasets.base import load_sample_images
import skimage.filter
from matplotlib.pyplot import imshow, show, axis


class EdgeDetectionTest(unittest.TestCase):


    def test(self):
        dataset = load_sample_images()
        img = dataset.images[0] 
        edges = skimage.filter.canny(img[..., 0], 2, 0.3, 0.2)
        axis('off')
        imshow(edges)
        show()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test']
    unittest.main()