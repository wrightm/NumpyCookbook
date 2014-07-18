'''
Created on 6 Jul 2014

@author: wrightm
'''
import unittest
import urllib2
import scipy.io.wavfile
import matplotlib.pyplot
import numpy


class BroadCastingTest(unittest.TestCase):


    def test(self):
        response = urllib2.urlopen('http://www.thesoundarchive.com/austinpowers/smashingbaby.wav')
        print response.info()
        WAV_FILE = '../../resources/smashingbaby.wav'
        filehandle = open(WAV_FILE, 'w')
        filehandle.write(response.read())
        filehandle.close()
        sample_rate, data = scipy.io.wavfile.read(WAV_FILE)
        print "Data type", data.dtype, "Shape", data.shape

        matplotlib.pyplot.subplot(2, 1, 1)
        matplotlib.pyplot.title("Original")
        matplotlib.pyplot.plot(data)

        newdata = data * 0.2
        newdata = newdata.astype(numpy.uint8)
        print "Data type", newdata.dtype, "Shape", newdata.shape

        scipy.io.wavfile.write("../../resources/quiet.wav",
                               sample_rate, newdata)

        matplotlib.pyplot.subplot(2, 1, 2)
        matplotlib.pyplot.title("Quiet")
        matplotlib.pyplot.plot(newdata)

        # matplotlib.pyplot.show()
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()