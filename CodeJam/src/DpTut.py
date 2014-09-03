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
        
        arranged_flowers = []
        arranged_flowers.append(flowers[0])
        
        # For each new incoming flower
        for i in range(1,length):
#             print arranged_flowers
            
            offset = 0
            # Find the best position (offset) to put it in
            for j in range(i):
                if ( self.block(arranged_flowers[j], flowers[i])):
                    if ( arranged_flowers[j].height > flowers[i].height):
                        offset = j
                        break
                    else:
                        offset = j+1;
                else:
                    if ( arranged_flowers[j].height > flowers[i].height ):
                        offset = j + 1
                    else:
                        # keep offset the same as offset is smaller than j
                        pass
                    
            arranged_flowers.insert(offset, flowers[i])
            
                
        # Return the height of the flowers only                    
        ordering = [flower.height for flower in arranged_flowers]
        
        return ordering
    
            
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


class AvoidRoads:
    '''
    http://topcoder.bgcoder.com/print.php?id=382
    
    You are standing at the corner with coordinates 0,0. Your destination is at 
    corner width,height. You will return the number of distinct paths that lead 
    to your destination. Each path must use exactly width+height blocks. In 
    addition, the city has declared certain street blocks untraversable. These 
    blocks may not be a part of any path. You will be given a String[] bad 
    describing which blocks are bad. If (quotes for clarity) "a b c d" is an 
    element of bad, it means the block from corner a,b to corner c,d is untraversable. 
    
    For example, let's say
    width  = 6
    length = 6
    bad = {"0 0 0 1","6 6 5 6"}
    
    Each element of the bad will be in the format "a b c d" where,
    a,b,c,d are integers with no extra leading zeros,
    a and c are between 0 and width inclusive,
    b and d are between 0 and height inclusive,
    and a,b is one block away from c,d.
    '''
    
    def numWays(self, width, height, bad):
        '''
        Parameters: int, int, String[]
        Returns: int for number of ways to traverse
        
        Analysis:
        Each path must use exactly width+height blocks, meaning that at each point,
        either go right or up.
        
        This solution has the time and space complexity of O(N^2).
        Space complexity can be reduced to O(N) by maintaining just two rows.
        '''
        
        _width = width + 1
        _height = height + 1
        
        states = [[0]* _width for j in range(_height)]
        states[0][0] = 1
        
        for w in range(_width):
            for h in range(_height):
                check1 = self.isBlock(h, w, h-1, w, bad)
                check2 = self.isBlock(h, w, h, w-1, bad)
                
                if w == 0 and h == 0:
                    continue
                elif (check1 and check2):
                    # Both ways are blocked
                    continue                
                elif (w == 0 and not check1) or check2:
                    states[h][w] = states[h-1][w]
                elif (h == 0 and not check2) or check1:
                    states[h][w] = states[h][w-1]
                else:
                    states[h][w] = states[h-1][w] + states[h][w-1]
        
        return states[height][width]

    def isBlock(self, a, b, c, d, bad):
        '''
        Return True if it is blocked from (a,b) to (c,d), based on input bad[].
        '''
        edgeString = self.edgeString(a, b, c, d)
        if (len(edgeString & set(bad)) > 0):
            return True
        else:
            return False
        
    def edgeString(self, a, b, c, d):
        '''
        Return the strings that represent the edge from (a,b) to (c,d).
        Could be either "a b c d" or "c d a b".
        '''
        edgeString = []
        indexes = [str(i) for i in [a, b, c, d]]
        edgeString.append(" ".join(indexes))
        indexes = [str(i) for i in [c, d, a, b]]
        edgeString.append(" ".join(indexes))
        return set(edgeString)
        

class ChessMetric:
    '''
    Suppose you had an n by n chess board and a super piece called a kingknight.
    
    The kingknight can move either one space in any direction (vertical, 
    horizontal or diagonally) or can make an 'L' shaped move. An 'L' shaped move 
    involves moving 2 spaces horizontally then 1 space vertically or 2 spaces 
    vertically then 1 space horizontally. In addition, a kingknight may never 
    jump off the board.
    
    Given the size of the board, the start position of the kingknight and the 
    end position of the kingknight, your method will return how many possible 
    ways there are of getting from start to end in exactly numMoves moves. start 
    and finish are int[]s each containing 2 elements. The first element will be 
    the (0-based) row position and the second will be the (0-based) column 
    position. Rows and columns will increment down and to the right respectively. 
    The board itself will have rows and columns ranging from 0 to size-1 inclusive. 

    Note, two ways of getting from start to end are distinct if their respective 
    move sequences differ in any way. In addition, you are allowed to use spaces 
    on the board (including start and finish) repeatedly during a particular path 
    from start to finish.
    '''
    
    def __init__(self, size):
        self._size = size
        self._board = [0] * (size*size)
        
    def printBoard(self):
        '''
        Print the internal _board as 2D array
        '''
        print
        for r in range(self._size):
            print self._board[r*self._size:(r+1)*self._size]

    def affectedSquares(self, idx):
        '''
        Return the indexes of the affected squares by the king-knight, given the
        current position (r,c)
        '''
        indexList = []
        r = idx // self._size
        c = idx % self._size
        
        # Top L's
        if ( self.isValidSquare(r-2, c-1) ):
            indexList.append(idx - 2*self._size - 1)
        if ( self.isValidSquare(r-2, c+1) ):
            indexList.append(idx - 2*self._size + 1)
        
        # Bottom L's
        if ( self.isValidSquare(r+2, c-1)):
            indexList.append(idx + 2*self._size - 1)
        if ( self.isValidSquare(r+2, c+1) ):
            indexList.append(idx + 2*self._size + 1)
        
        # Same-row X's
        if ( self.isValidSquare(r, c-1) ):
            indexList.append(idx - 1)
        if ( self.isValidSquare(r, c+1) ):
            indexList.append(idx + 1)
        
        # The rest
        for i in range(-2, 3):
            if ( self.isValidSquare(r+1, c+i) ):
                indexList.append(idx + self._size + i)
            if ( self.isValidSquare(r-1, c+i) ):
                indexList.append(idx - self._size + i)
        
        return indexList
    
    def isValidSquare(self, r, c):
        if ( r < 0 or r >= self._size or c < 0 or c >= self._size):
            return False
        return True
    
    def toIndex(self, r, c):
        return (self._size*r + c)
    
    def filledSquares(self):
        '''
        Return the indexes of the filled squares on the board.
        '''
        index = [i for i, value in enumerate(self._board) if value != 0 ]
        return index
        
    def numWays(self, start, end, numMoves):
        # First move
        idx = self.affectedSquares(self.toIndex(start[0], start[1]))
        for i in idx:
            self._board[i] = 1
        
            
        for move in range(numMoves-1):
#             self.printBoard()
            
            idx = self.filledSquares()
            # save a copy of the boards
            temp = self._board[:]
            
            for i in idx:
                jdx = self.affectedSquares(i)
                
                for j in jdx:
                    self._board[j] += temp[i]
        
#         self.printBoard()
        return self._board[self.toIndex(end[0], end[1])]
    
    @staticmethod
    def howMany( size, start, end, numMoves):
        '''
        Parameters:    int, int[], int[], int
        Returns: int for number of moves
        '''
        return ChessMetric(size).numWays(start, end, numMoves)
    
    pass

if __name__ == "__main__":
    # Quick test of affectedSquares()
    ob = ChessMetric(7)
    idx = ob.affectedSquares(ob.toIndex(3, 3))
    for i in idx:
        ob._board[i] = 8
    ob.printBoard()
    
    print ChessMetric.howMany(3, (0,0), (0,0), 2)
    print ChessMetric.howMany(100, (0,0), (0,99), 50)
    
    # Check
#     ordering = FlowerGarden().getOrdering([5,4,3,2,1], 
#                              [1,1,1,1,1], 
#                              [365,365,365,365,365])
#     
#     print ordering
    
#     # [1,2,3,4,5]
#     ordering = FlowerGarden().getOrdering([5,4,3,2,1], 
#                                                          [1,5,10,15,20], 
#                                                          [5,10,15,20,25])
#     print ordering
#     
#     ordering = FlowerGarden().getOrdering([1,2,3,4,5,6], 
#                          [1,3,1,3,1,3], 
#                          [2,4,2,4,2,4])
#     print ordering
    