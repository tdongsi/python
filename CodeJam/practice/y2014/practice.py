"""
Created on Oct 2, 2015

@author: cdongsi
"""
import random


def quick_sort(input):
    """
    Implement quick-sort algorithm
    """
    
    if len(input) < 2:
        return input
    else:
        # pivot is the middle
        n = len(input)//2
        pivot = input[n]
        
        # Pivoting is the tricky part in quick-sort
        # In C++/Java, it is done by swapping
        left = [x for x in input if x <= pivot]
        right = [x for x in input if x > pivot]
        left.remove(pivot)
        
        merged = quick_sort(left)
        merged.append(pivot)
        merged.extend(quick_sort(right))
    
        return merged


def merge(sorted_left, sorted_right):
    """
    Merging two sorted lists to produce a sorted list
    """
    merged = []
    idx_left, idx_right = 0, 0
    
    while idx_left < len(sorted_left) and idx_right < len(sorted_right):
        if sorted_left[idx_left] <= sorted_right[idx_right]:
            merged.append(sorted_left[idx_left])
            idx_left += 1
        else:
            merged.append(sorted_right[idx_right])
            idx_right += 1
    
    # Append the remaining to merged
    # If you want to determine which half remains
    """
    if idx_left < len(sorted_left):
        merged.extend(sorted_left[idx_left:])
    else:
        merged.extend(sorted_right[idx_right:])
    """
    
    merged.extend(sorted_left[idx_left:])
    merged.extend(sorted_right[idx_right:])
    return merged


def merge_sort(input):
    """
    Do merge sort
    """
    
    if len(input) <= 1:
        return input
    else:
        n = len(input)//2
        sorted_left = merge_sort(input[:n])
        sorted_right = merge_sort(input[n:])
        
        return merge(sorted_left, sorted_right)


def find_order(input, k):
    """
    Find the kth smallest number in a list of integers
    k = 0 for the smallest number.
    """
    if ( k >= len(input) or k < 0 ):
        return None
    elif len(input) == 0:
        return None
    elif len(input) == 1:
        # k should be 0
        assert k == 0
        return input[0]
    else:
        pivot = input[len(input)//2]
        left = [x for x in input if x <= pivot]
        left.remove(pivot)
        
        if len(left) == k:
            return pivot
        elif len(left) > k:
            return find_order(left, k)
        else:
            right = [x for x in input if x > pivot]
            return find_order(right, k-1-len(left))


def find_median(input):
    """
    Find the median of a list of integers
    """
    return find_order(input, len(input)//2)


def main_sort():
    """
    Run test program of sorting algorithms
    """
    
    input_1 = [7, 6, 5, 4, 3, 2, 1]
    print find_median(input_1)
    
    input_2 = [5, 4, 3, 2, 1, 6, 7]
    print find_median(input_2)
    
    input_3 = [1, 2, 3, 4, 5, 7, 6]
    print find_median(input_3)
    
    input_4 = [1, 1, 3, 3, 2, 2, 4]
    print find_median(input_4)


def shuffle(input):
    """
    Random shuffling of a deck, represented by a list of integers
    """
    deck = input[:]
    for i in xrange(len(deck)-1):
        # Find a random index between i and end of deck
        dest = random.randint(i+1,len(deck)-1)
        deck[i], deck[dest] = deck[dest], deck[i]
        
    return deck


def main():
    """
    Run test of shuffling algorithm
    """
    input_1 = [7, 6, 5, 4, 3, 2, 1]
    print shuffle(input_1)
    print input_1


if __name__ == '__main__':
    main()