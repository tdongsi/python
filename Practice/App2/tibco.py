'''
Created on Oct 31, 2014

@author: tdongsi
'''

def maxArea(heights):
    '''
    Problem statement:
    You are given a list of integers, representing heights of columns.
    If a column is next to a higher or equal column, we can extend an "area" to
    the next column, and continue to either side until it meets a shorter column.
    Find the largest "area" formed by method above.
    
    Example: input is [4,6,5,1,3,2]
    The first column is 4. The next two columns are higher and it can be extended
    from 4 to 6 to 5. The total "area" is 4 x 3 = 12.
    Next column is 6. It cannot be extended to either left or right. The total
    "area" for this column is 6.
    For the next column 5, it can be extended to the left only. The total area for
    this column is 5 x 2 = 10.
    Similarly for column 3, it cannot be extended to either left or right. The
    total area is 3.
    
    In the end, the "area" associated with each column is [12, 6, 10, 6, 3, 6].
    The method should return 12.
    '''
    
    # Divide and conquer approach
    
    if len(heights) == 1:
        return heights[0]
    elif len(heights) == 0:
        return 0
    
    # This step takes O(N)
    minVal = min(heights)
    minIdx = heights.index(minVal)
    
    # Solve the smaller problem for sublist before smallest number 
    # E.g. solve [4,6,5]
    front = maxArea(heights[0:minIdx])
    # Solve the smaller problem for sublist after smallest number
    # E.g.: solve [3,2]
    back = maxArea(heights[minIdx+1:])
    # The area associated with minimum column is trivial to compute
    current = minVal*len(heights)
    
    # Find max of 3
    return max(front, current, back)
    

def main():
    # Expected 12
    print maxArea( [4,6,5,1,3,2])

if __name__ == '__main__':
    main()
