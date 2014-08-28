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

    def test_minNumOfCoin_knownValues(self):
        for input, expected in self.knownInputOutput:
            output = MinNumOfCoin.minNumOfCoin(input, self.coinValues)
            self.assertEqual(expected, output)

    def test_minNumOfCoin_invalid(self):
        self.assertEqual(0, MinNumOfCoin.minNumOfCoin(5, [3]))
        self.assertEqual(0, MinNumOfCoin.minNumOfCoin(5, [6]))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()