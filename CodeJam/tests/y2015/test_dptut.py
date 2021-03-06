"""
Created on Aug 27, 2014

@author: tdongsi
"""

import unittest
import practice.y2016.dp as y16

from codejam.y2015.DpTut import *


class MinNumOfCoin(object):

    @staticmethod
    def minNumOfCoin(sum, coinValues):
        print "Input: %d, %s" %(sum, str(coinValues))
        return y16.find_coin_number(sum, coinValues)


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
        self.assertEqual(-1, MinNumOfCoin.minNumOfCoin(5, [3]))
        self.assertEqual(-1, MinNumOfCoin.minNumOfCoin(5, [6]))

        self.assertEqual(1, MinNumOfCoin.minNumOfCoin(5, [5]))

        self.assertEqual(-1, MinNumOfCoin.minNumOfCoin(5, []))
        self.assertEqual(-1, MinNumOfCoin.minNumOfCoin(5, [0]))
        self.assertEqual(-1, MinNumOfCoin.minNumOfCoin(5, [0, 0]))


class ZigZagTest(unittest.TestCase):
    """
    Unit tests for ZigZag problem
    http://community.topcoder.com/stat?c=problem_statement&pm=1259&rd=4493
    """
    
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
            output = ZigZag.longestZigZag(input)
            self.assertEqual(expected, output)
            
            
class BadNeighborTest(unittest.TestCase):
    """
    Unit tests for Bad Neighbors problem
    http://mattcb.blogspot.com/2013/03/bad-neighbors.html
    """
    
    def test_maxDonations(self):
        self.assertEqual(11, BadNeighbors().maxDonations([11]))
        self.assertEqual(15, BadNeighbors().maxDonations([11, 15]))
        self.assertEqual(19, BadNeighbors().maxDonations([19, 11, 15]))
        
        self.assertEqual(44, BadNeighbors().maxDonations([19, 29, 13, 14, 15]))
        self.assertEqual(8, BadNeighbors().maxDonations([1, 2, 3, 4, 5]))
        self.assertEqual(19, BadNeighbors().maxDonations([10, 3, 2, 5, 7, 8]))
        self.assertEqual(21, BadNeighbors().maxDonations([7, 7, 7, 7, 7, 7, 7]))
        self.assertEqual(16, BadNeighbors().maxDonations([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))
        self.assertEqual(2926, BadNeighbors().maxDonations([94, 40, 49, 65, 21, 21, 
                  106, 80, 92, 81, 679, 4, 61,  
                  6, 237, 12, 72, 74, 29, 95, 265, 35, 47, 1, 61, 397,
                  52, 72, 37, 51, 1, 81, 45, 435, 7, 36, 57, 86, 81, 72]))


class FlowerGardenTest(unittest.TestCase):
    """
    Unit tests for Flower Garden problem
    http://community.topcoder.com/stat?c=problem_statement&pm=1918&rd=5006
    """
    
    def test_compare(self):
        self.assertTrue(FlowerGarden().block(Flower(1,1,10), Flower(2,1,10)))
        self.assertFalse(FlowerGarden().block(Flower(1,1,5), Flower(2,6,10)))
        
        self.assertEqual( -1, FlowerGarden().compare(Flower(1,1,10), Flower(2,1,10)) )
        self.assertEqual( 1, FlowerGarden().compare(Flower(1,1,5), Flower(2,6,10)) )
        
        self.assertEqual( -1, FlowerGarden().compare(Flower(6,3,4), Flower(5,1,2)) )
        self.assertEqual( 1, FlowerGarden().compare(Flower(6,3,4), Flower(4,3,4)) )
    
    def test_getOrdering(self):
        """
        These flowers all bloom on January 1st and wilt on December 31st. 
        Since they all may block each other, you must order them from shortest to tallest
        """
        self.assertListEqual([1, 2, 3, 4, 5],
                              FlowerGarden().getOrdering([5,4,3,2,1], 
                                                         [1,1,1,1,1], 
                                                         [365,365,365,365,365])
                             )
        
        self.assertListEqual([5,  4,  3,  2,  1],
                              FlowerGarden().getOrdering([5,4,3,2,1], 
                                                         [1,5,10,15,20], 
                                                         [4,9,14,19,24])
                             )
        
        self.assertListEqual([1, 2, 3, 4, 5],
                              FlowerGarden().getOrdering([5,4,3,2,1], 
                                                         [1,5,10,15,20], 
                                                         [5,10,15,20,25])
                             )
        
        self.assertListEqual([3,  4,  5,  1,  2],
                              FlowerGarden().getOrdering([5,4,3,2,1], 
                                                         [1,5,10,15,20], 
                                                         [5,10,14,20,25])
                             )
        
        self.assertListEqual([2,  4,  6,  1,  3,  5],
                              FlowerGarden().getOrdering([1,2,3,4,5,6], 
                                                         [1,3,1,3,1,3], 
                                                         [2,4,2,4,2,4])
                             )
        
        
        self.assertListEqual([4, 5, 2, 3],
                              FlowerGarden().getOrdering([3,2,5,4], 
                                                         [1,2,11,10], 
                                                         [4,3,12,13])
                             )


class AvoidRoadTest(unittest.TestCase):
    """
    Unit tests for AvoidRoads problem
    """
    
    def test_numWays(self):
        self.assertEqual(252, AvoidRoads().numWays(6, 6, ("0 0 0 1","6 6 5 6")) )
        self.assertEqual(2, AvoidRoads().numWays(1, 1, ()) )
        self.assertEqual(6406484391866534976, AvoidRoads().numWays(35, 31, ()) )
        self.assertEqual(0, AvoidRoads().numWays(2, 2, ("0 0 1 0", "1 2 2 2", "1 1 2 1")) )
    

class ChessMetricsTest(unittest.TestCase):
    """
    Unit tests for ChessMetrics problem
    """
    
    def test_numWays(self):
        self.assertEqual(1, ChessMetric.howMany(3, (0,0), (1,0), 1) )
        self.assertEqual(1, ChessMetric.howMany(3, (0,0), (1,2), 1) )
        self.assertEqual(0, ChessMetric.howMany(3, (0,0), (2,2), 1) )
        self.assertEqual(5, ChessMetric.howMany(3, (0,0), (0,0), 2) )
        self.assertEqual(243097320072600, ChessMetric.howMany(100, (0,0), (0,99), 50) )


class JewelryTest(unittest.TestCase):
    """
    Unit tests for Jewelry problem
    """
    
    def test_howMany(self):
        self.assertEqual(9, Jewelry().howMany([1,2,5,3,4,5]))
        self.assertEqual(18252025766940, Jewelry().howMany([1000,1000,1000,1000,1000,
                                                     1000,1000,1000,1000,1000,
                                                     1000,1000,1000,1000,1000,
                                                     1000,1000,1000,1000,1000,
                                                     1000,1000,1000,1000,1000,
                                                     1000,1000,1000,1000,1000]))
        self.assertEqual(4, Jewelry().howMany([1,2,3,4,5]))
        self.assertEqual(607, Jewelry().howMany([7,7,8,9,10,11,1,2,2,3,4,5,6]))
        self.assertEqual(0, Jewelry().howMany([123,217,661,678,796,964,54,111,417,526,917,923]))


class StripePainterTest(unittest.TestCase):
    """
    Unit tests for StripePainter problem
    """
    
    def test_minStrokes(self):
        self.assertEqual(3, StripePainter().minStrokes('RGBGR'))
        self.assertEqual(3, StripePainter().minStrokes('RGRG'))
        self.assertEqual(4, StripePainter().minStrokes('ABACADA'))
        self.assertEqual(7, StripePainter().minStrokes('AABBCCDDCCBBAABBCCDD'))
        self.assertEqual(26, StripePainter().minStrokes('BECBBDDEEBABDCADEAAEABCACBDBEECDEDEACACCBEDABEDADD'))

        
class QuickSumsTest(unittest.TestCase):
    """
    Unit tests for QuickSums problem
    """
    
    def test_minSums(self):
        self.assertEqual(4, QuickSums().minSums('99999', 45))
        self.assertEqual(3, QuickSums().minSums('1110', 3))
        self.assertEqual(8, QuickSums().minSums('0123456789', 45))
        self.assertEqual(-1, QuickSums().minSums('99999', 100))
        self.assertEqual(2, QuickSums().minSums('382834', 100))
        self.assertEqual(4, QuickSums().minSums('9230560001', 71))


class ShortPalindromesTest(unittest.TestCase):
    """
    Unit tests for ShortPalindromes problem
    """
    
    def test_shortest(self):
        self.assertEqual('ECARACE', ShortPalindromes().shortest('RACE'))
        self.assertEqual('REDTOCPCOTDER', ShortPalindromes().shortest('TOPCODER'))
        self.assertEqual('Q', ShortPalindromes().shortest('Q'))
        self.assertEqual('MADAMIMADAM', ShortPalindromes().shortest('MADAMIMADAM'))
        self.assertEqual('AFLRCAGIOEOUAEOCEGRURGECOEAUOEOIGACRLFA', 
                     ShortPalindromes().shortest('ALRCAGOEUAOEURGCOEUOOIGFA'))


class StarAdventureTest(unittest.TestCase):
    """
    Unit tests for StarAdventure problem
    """
    
    def test_mostStars(self):
        map = ["01",
               "11"]
        self.assertEqual(3, StarAdventure().mostStars(map))
        
        map = [  "0999999999"
                ,"9999999999"
                ,"9999999999"
                ,"9999999999"
                ,"9999999999"
                ,"9999999999"
                ,"9999999999"
                ,"9999999999"
                ,"9999999999"
                ,"9999999999"]
        self.assertEqual(450, StarAdventure().mostStars(map))

        map = [  "012"
                ,"012"
                ,"012"
                ,"012"
                ,"012"
                ,"012"
                ,"012"]
        self.assertEqual(21, StarAdventure().mostStars(map))
        
        map = [  "0123456789",
                 "1123456789",
                 "2223456789",
                 "3333456789",
                 "4444456789",
                 "5555556789",
                 "6666666789",
                 "7777777789",
                 "8888888889",
                 "9999999999"]
        self.assertEqual(335, StarAdventure().mostStars(map))


class MiniPaintTest(unittest.TestCase):
    """
    Unit tests for MiniPaint problem
    """
    
    def test_leastBad(self):
        pic = [ "BBBBBBBBBBBBBBB",
                "WWWWWWWWWWWWWWW",
                "WWWWWWWWWWWWWWW",
                "WWWWWBBBBBWWWWW"]
        self.assertEqual(0, MiniPaint().leastBad(pic, 6))
        
        self.assertEqual(5, MiniPaint().leastBad(pic, 4))
        
        self.assertEqual(60, MiniPaint().leastBad(pic, 0))
        
        pic =[  "BWBWBWBWBWBWBWBWBWBWBWBWBWBWBW",
                "BWBWBWBWBWBWBWBWBWBWBWBWBWBWBW",
                "BWBWBWBWBWBWBWBWBWBWBWBWBWBWBW",
                "BWBWBWBWBWBWBWBWBWBWBWBWBWBWBW",
                "BWBWBWBWBWBWBWBWBWBWBWBWBWBWBW",
                "BWBWBWBWBWBWBWBWBWBWBWBWBWBWBW"]
        self.assertEqual(40, MiniPaint().leastBad(pic, 100))
        
        pic = ["B"]
        self.assertEqual(0, MiniPaint().leastBad(pic, 1))


if __name__ == "__main__":
    unittest.main()
