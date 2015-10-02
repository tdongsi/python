'''
Created on Oct 2, 2015

@author: cdongsi
'''

def quick_sort(input):
    '''
    Implement quick-sort algorithm
    '''
    
    return input

def merge(sorted_left, sorted_right):
    '''
    Merging two sorted lists to produce a sorted list
    '''
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
    '''
    if idx_left < len(sorted_left):
        merged.extend(sorted_left[idx_left:])
    else:
        merged.extend(sorted_right[idx_right:])
    '''
    
    merged.extend(sorted_left[idx_left:])
    merged.extend(sorted_right[idx_right:])
    return merged

def merge_sort(input):
    '''
    Do merge sort
    '''
    
    if len(input) <= 1:
        return input
    else:
        n = len(input)//2
        sorted_left = merge_sort(input[:n])
        sorted_right = merge_sort(input[n:])
        
        return merge(sorted_left, sorted_right)

def main():
    '''
    Run test program
    '''
    
    input_1 = [7, 6, 5, 4, 3, 2, 1]
    print merge_sort(input_1)
    
    input_2 = [5, 4, 3, 2, 1, 6, 7]
    print merge_sort(input_2)
    
    input_3 = [1, 2, 3, 4, 5, 7, 6]
    print merge_sort(input_3)
    
    input_4 = [1, 1, 3, 3, 2, 2, 4]
    print merge_sort(input_4)


if __name__ == '__main__':
    main()