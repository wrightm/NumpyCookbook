'''
Created on 11 Jul 2014

@author: wrightm
'''
import unittest
import urllib2
import re
import numpy


class ChararrayTest(unittest.TestCase):


    def test(self):
        response = urllib2.urlopen('http://python.org/')
        html = response.read()
        html = re.sub(r'<.*?>', '', html)
        carray = numpy.array(html).view(numpy.chararray)
        carray = carray.expandtabs(1)
        carray = carray.splitlines()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()