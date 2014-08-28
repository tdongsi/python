'''
Created on Aug 27, 2014

@author: tdongsi
'''
import unittest
from DpTut import *


class MinNumOfCoinTest(unittest.TestCase):
    coinValues = [1, 3, 5]
    knownInputOutput = ( (1, 1),
                    (2, 2),
                    (3, 1),
                    (4, 2),
                    (5, 1),
                    (6, 2),
                    (7, 3),
                    (8, 2),
                    (9, 3),
                    (10, 2),
                    (11, 3)
                   )

    def test_minNumOfCoin(self):
        for input, expected in self.knownInputOutput:
            output = MinNumOfCoin.minNumOfCoin(input, self.coinValues)
            self.assertEqual(expected, output)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()