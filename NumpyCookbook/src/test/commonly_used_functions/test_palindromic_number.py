import unittest
import numpy


def isPalindromic(number):
    s_num = str(number)
    if s_num == s_num[::-1]:
        return True
    else:
        return False

class PalindromicNumberTest(unittest.TestCase):


    def test(self):
        #1. Create  3-digits numbers array
        a = numpy.arange(100, 1000)
        numpy.testing.assert_equal(100, a[0])
        numpy.testing.assert_equal(999, a[-1])
        #2. Create products array
        numbers = numpy.outer(a,a)
        numbers = numpy.ravel(numbers)
        numbers.sort()
        numpy.testing.assert_equal(810000, len(numbers))
        numpy.testing.assert_equal(10000, numbers[0])
        numpy.testing.assert_equal(998001, numbers[-1])
        
        palindromic_numbers = []
        for i in xrange(-1, -1*len(numbers), -1):
            number = numbers[i]
            if isPalindromic(number):
                palindromic_numbers.append(number)
        palindromic_numbers.sort()
        
        is_palindromic = numpy.vectorize(isPalindromic)
        is_palindromic_numbers = is_palindromic(numbers)
        vectorize_palindromic_numbers= numbers[is_palindromic_numbers].tolist()

        self.assertEqual(palindromic_numbers, vectorize_palindromic_numbers)
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test']
    unittest.main()