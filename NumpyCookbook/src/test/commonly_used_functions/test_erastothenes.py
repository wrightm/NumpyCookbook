'''
Created on 9 Jul 2014

@author: wrightm
'''
import unittest
import numpy

def check_primes(a, p):
    #2. Sieve out multiples of p
    a = a[a % p != 0]

    return a

class EratosthenesTest(unittest.TestCase):


    def test(self):
        
        LIM = 10 ** 6
        N = 10 ** 9
        P = 10001
        primes = []
        p = 2
        
        for i in xrange(3, N, LIM):
            #1. Create a list of consecutive integers
            a = numpy.arange(i, i + LIM, 2)

            while len(primes) < P:
                a = check_primes(a, p)
                primes.append(p)

                p = a[0]

        print len(primes), primes[P-1]


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test']
    unittest.main()