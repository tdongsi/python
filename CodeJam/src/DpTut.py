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
        
        diff = [0]*(length-1)
        for idx in range(len(diff)):
            if ( input[idx+1] - input[idx] != 0 ):
                diff[idx] = math.copysign(1, input[idx+1] - input[idx])
            
        maxLength = [0]*len(diff)
        maxLength[0] = 1;
        
        for idx in range(1, len(maxLength)):
            maxLength[idx] = maxLength[idx-1]
            
            for j in range(idx):
                temp = 0
                if ( diff[idx] != 0 and diff[j] == -diff[idx]):
                    temp = maxLength[j]+1
                
                if ( temp > maxLength[idx] ):
                    maxLength[idx] = temp
         
        return (maxLength[-1] + 1)   

if __name__ == "__main__":
    # Check
    ZigZag.longestZigZag([1, 7, 4, 9, 2, 5])
    ZigZag.longestZigZag([1, 17, 5, 10, 13, 15, 10, 5, 16, 8])
    
    