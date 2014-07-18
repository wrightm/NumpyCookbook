'''
Created on 14 Jul 2014

@author: wrightm
'''
import unittest
import timeit
import matplotlib.pyplot
import numpy

lst = []

def dosort():
    lst.sort()

def measure():
    timer = timeit.Timer('dosort()', 'from __main__ import dosort')

    return timer.timeit(10 ** 2)

if __name__ == "__main__":
    powersOf2 = numpy.arange(0, 19)
    sizes = 2 ** powersOf2

    times = numpy.array([])

    for size in sizes:
        lst = numpy.random.random_integers(1, 10 ** 6, size)
        times = numpy.append(times, measure())

    fit = numpy.polyfit(sizes * powersOf2, times, 1)
    print fit
    matplotlib.pyplot.title("Sort array sizes vs execution times")
    matplotlib.pyplot.xlabel("Size")
    matplotlib.pyplot.ylabel("(s)")
    matplotlib.pyplot.semilogx(sizes, times, 'ro')
    matplotlib.pyplot.semilogx(sizes, numpy.polyval(fit, sizes * powersOf2))
    matplotlib.pyplot.show()
