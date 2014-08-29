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
        
class ZigZagTest(unittest.TestCase):
    '''
    Unit tests for ZigZag problem
    http://community.topcoder.com/stat?c=problem_statement&pm=1259&rd=4493
    '''
    
    knownInputOutput = ( ([1, 7, 4, 9, 2, 5], 6),
                         ([1, 17, 5, 10, 13, 15, 10, 5, 16, 8], 7),
                         ([44], 1),
                         ([1, 2, 3, 4, 5, 6, 7, 8, 9], 2),
                         ([70, 55, 13, 2, 99, 2, 80, 80, 80, 80, 100, 19, 7, 5, 
                           5, 5, 1000, 32, 32], 8),
                         ([374, 40, 854, 203, 203, 156, 362, 279, 812, 955, 
                            600, 947, 978, 46, 100, 953, 670, 862, 568, 188, 
                            67, 669, 810, 704, 52, 861, 49, 640, 370, 908, 
                            477, 245, 413, 109, 659, 401, 483, 308, 609, 120, 
                            249, 22, 176, 279, 23, 22, 617, 462, 459, 244], 36)
                        )
    
    def test_longestZigZag_knownValues(self):
        for input, expected in self.knownInputOutput:
#             print input
            output = ZigZag.longestZigZag(input)
            self.assertEqual(expected, output)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()