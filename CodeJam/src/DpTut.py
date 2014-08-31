'''
Created on Aug 27, 2014

Some Dynamic Programming exercises and solutions.

@author: cuongd
'''

import math
from _abcoll import Sequence

class MinNumOfCoin:
    '''
    Given a list of N coins, their values (V1, V2, ... , VN), and the total sum S. 
    Find the minimum number of coins the sum of which is S (we can use as many coins of one type as we want), 
    or report that it's not possible to select coins in such a way that they sum up to S.
    '''
    
    @staticmethod
    def minNumOfCoin(totalValue, coinValues):
        '''
        totalValue: an integer for totalValue
        coinValues: a list of coin values, assuming all positives.
        Return:
        0 indicates it's impossible to select coins. Otherwise, returns >= 1.
        '''
        
        # Largest number of coins to get that sum 
        _maxCount = math.ceil(totalValue/min(coinValues))
        _big = _maxCount + 10
        _min = [_big]*(totalValue+1)
        _min[0] = 0
        
        for _sum in range(1, totalValue+1):
            minCount = _big;
            for val in coinValues:
                if ( _sum - val >= 0 and _min[_sum-val]+1 < minCount):
                    minCount = _min[_sum-val]+1
                    
            _min[_sum] = minCount
    
        if (_min[totalValue] == _big):
            return 0
        return _min[totalValue]
    
    
class ZigZag:
    '''
    http://community.topcoder.com/stat?c=problem_statement&pm=1259&rd=4493
    
    A sequence of numbers is called a zig-zag sequence if the differences between 
    successive numbers strictly alternate between positive and negative. The first 
    difference (if one exists) may be either positive or negative. A sequence 
    with fewer than two elements is trivially a zig-zag sequence.

    For example, 1,7,4,9,2,5 is a zig-zag sequence because the differences 
    (6,-3,5,-7,3) are alternately positive and negative. In contrast, 1,4,7,2,5 
    and 1,7,4,5,5 are not zig-zag sequences, the first because its first two 
    differences are positive and the second because its last difference is zero.

    Given a sequence of integers, sequence, return the length of the longest 
    subsequence of sequence that is a zig-zag sequence. A subsequence is obtained 
    by deleting some number of elements (possibly zero) from the original sequence, 
    leaving the remaining elements in their original order.
    '''
    
    @staticmethod
    def longestZigZag(input):
        '''
        Parameters: a sequence of integers
        Returns: integer: length of the longest subsequence of sequence that is 
        a zig-zag sequence.
        '''
        
        length = len(input)
        if ( length == 1 ):
            return 1
        elif (length == 2 ):
            return 2
        
        # For zigzag sequence, we only care about signum of differences
        diff = [0]*(length-1)
        for i in range(len(diff)):
            if ( input[i+1] - input[i] != 0 ):
                diff[i] = math.copysign(1, input[i+1] - input[i])
            
        maxLength = [0]*len(diff)
        maxLength[0] = 1;
        
        for i in range(1, len(maxLength)):
            maxLength[i] = maxLength[i-1]
            
            for j in range(i):
                temp = 0
                if ( diff[i] != 0 and diff[j] == -diff[i]):
                    temp = maxLength[j]+1
                
                if ( temp > maxLength[i] ):
                    maxLength[i] = temp
         
        return (maxLength[-1] + 1)
    
    

class BadNeighbors:
    '''
    Each of the town's residents is willing to donate a certain amount, as 
    specified in the int[] donations, which is listed in clockwise order around 
    the well. However, nobody is willing to contribute to a fund to which his 
    neighbor has also contributed. Next-door neighbors are always listed 
    consecutively in donations, except that the first and last entries in 
    donations are also for next-door neighbors. You must calculate and return 
    the maximum amount of donations that can be collected.
    '''
    
    def maxDonations( self, donations ):
        '''
        Parameters: list of donations by each neighbor
        Returns: integer for max donations
        '''
        if (len(donations) == 1):
            return sum(donations)
        elif (len(donations) == 2):
            return max(donations)
        
        # Consider two possibilities:
        # 1) the first is in, the second and the last cannot be in
        # 2) the first is NOT in, the second and the last may be in
        return max( self.maxSum(donations[:-1]), self.maxSum(donations[1:]) )
    
    def maxSum( self, inputList ):
        '''
        Return the largest sum on the condition that two adjacent elements could 
        not counted together 
        '''
        maxSum = [0]*len(inputList)
        maxSum[0] = inputList[0]
        maxSum[1] = max(inputList[:2]) # larger of the two adjacent elements
        
        for i in range(2,len(inputList)):
            cur = inputList[i]
            
            # if the neighbor [i-1] contributes into maxSum[i-1], 
            # you cannot add the current element
            # if the neighbor [i-1] does not contribute into maxSum[i-1],
            # maxSum[i-1] is equal to maxSum[i-2]. 
            # maxSum[i] will be updated if cur + maxSum[i-2] is the best
            maxSum[i] = maxSum[i-1]
            
            for j in range(i-1):
                temp = maxSum[j] + cur
                
                if ( temp > maxSum[i]):
                    maxSum[i] = temp
                
#         print "maxSum call: %s" % str(maxSum)
        return maxSum[-1]

class Flower:
        
    def __init__(self, height, bloom, wilt):
        self.height = height
        self.bloom = bloom
        self.wilt = wilt
        assert self.bloom < self.wilt
        
    def __repr__(self):
        return '(H: %d, B: %d, W: %d)' % (self.height, self.bloom, self.wilt)
        

class FlowerGarden:
    '''
    http://community.topcoder.com/stat?c=problem_statement&pm=1918&rd=5006
    
    You will be given a int[] height, a int[] bloom, and a int[] wilt. 
    Each type of flower is represented by the element at the same index of height, 
    bloom, and wilt. height represents how high each type of flower grows, bloom 
    represents the morning that each type of flower springs from the ground, and 
    wilt represents the evening that each type of flower shrivels up and dies. 
    Each element in bloom and wilt will be a number between 1 and 365 inclusive, 
    and wilt[i] will always be greater than bloom[i]. You must plant all of the 
    flowers of the same type in a single row for appearance, and you also want 
    to have the tallest flowers as far forward as possible. However, if a flower 
    type is taller than another type, and both types can be out of the ground at 
    the same time, the shorter flower must be planted in front of the taller 
    flower to prevent blocking. A flower blooms in the morning, and wilts in the 
    evening, so even if one flower is blooming on the same day another flower is 
    wilting, one can block the other.

    You should return a int[] which contains the elements of height in the order 
    you should plant your flowers to acheive the above goals. The front of the 
    garden is represented by the first element in your return value, and is where 
    you view the garden from. The elements of height will all be unique, so there 
    will always be a well-defined ordering.
    '''
    
    def getOrdering(self, height, bloom, wilt):
        '''
        Parameters:    int[], int[], int[]
        Returns:    int[]
        '''
        length = len(height)
        assert len(bloom) == length
        assert len(wilt) == length
        
        flowers = []
        
        # Initialize the list of given flowers
        for i in range(length):
            flowers.append( Flower(height[i], bloom[i], wilt[i]) )
        
        orderedFlowers = []
        orderedFlowers.append(flowers[0])
        
        for i in range(1,length):
            print orderedFlowers
            check = [False]*len(orderedFlowers)
            
            # For each new flower, check with all the current flowers in orderedFlowers
            # If check returns False, new flower should be right/after to that flower
            # If check returns True, new flower should be left/before to that flower
            for j in range(len(orderedFlowers)):
                check[j] = self.tallerXorBlock(orderedFlowers[j], flowers[i])
            
            
            newOrder = [orderedFlowers[k] for k, val in enumerate(check) if val]
            newOrder.append(flowers[i])
            newOrder.extend([orderedFlowers[k] for k, val in enumerate(check) if not val])
            orderedFlowers = newOrder
                
        # Return the height of the flowers only                    
        ordering = [flower.height for flower in orderedFlowers]
        
        return ordering
    
    def tallerXorBlock(self, flower1, flower2):
        '''
        XOR of taller and block check
        
        Return true if flower1 should be left to flower 2
        Return false if flower 1 should be right to flower 2
        '''
        return self.block(flower1, flower2) != self.taller(flower1, flower2)
    
    def taller(self, flower1, flower2):
        return flower1.height > flower2.height
            
    def block(self, flower1, flower2):
        '''
        Return true if first Flower's bloom overlaps the second Flower's bloom
        '''
        if (flower2.bloom > flower1.wilt or flower2.wilt < flower1.bloom):
            return False
        else:
            return True
        
    def compare(self, flower1, flower2):
        if (flower1.height == flower2.height):
            return 0 # never happen
        if ( self.block(flower1,flower2) ):
            return int(math.copysign(1, flower1.height - flower2.height))
        else:
            return int(math.copysign(1, flower2.height - flower1.height))

if __name__ == "__main__":
    # Check
#     ordering = FlowerGarden().getOrdering([5,4,3,2,1], 
#                              [1,1,1,1,1], 
#                              [365,365,365,365,365])
#     
#     print ordering
    
    ordering = FlowerGarden().getOrdering([5,4,3,2,1], 
                                                         [1,5,10,15,20], 
                                                         [5,10,15,20,25])
    print ordering
    
    
    