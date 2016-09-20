---
layout: post
title: "Tutorial: More about Quick Sort"
date: 2016-08-31 21:48:49 -0700
comments: true
categories: 
- Tutorial
- Algorithm
- Addepar
---

This post discuses more about partition algorithms used in Quick Sort and its runtime. 
Partition algorithms are also used to efficiently find certain groups of the list, also known as "Quick Select". 

<!-- more -->

### Discussion of Quick-sort runtime

The Quick-sort algorithm has a very serious weakness: O(n^2) runtime in the worst-case scenarios. 
Because of this weakness, it should not used in any large-scale applications with arbitrary inputs.
This section discusses when those worst-case scenarios happen and how we can limit the chance of those scenarios.
Before going into details, it should be noted that worst-case scenarios cannot be avoided, and those scenarios depend on the partition strategy that Quick-sort uses.
To find the worst-case scenarios for a partition strategy, find a class of inputs such that after each partition, only one item is moved to either side of the pivot.

In the standard two-way partition strategy ("< pivot" and ">= pivot") shown in [this post](/blog/2016/08/30/tutorial-sorting-algorithms/), it has the O(n^2) runtime when the input list is sorted (Quiz: in which direction?).
One simple way to work around that problem is to shuffle the input list (by swapping random elements).
Shuffling the list can be done in O(n) time and should has no effect to overall O(nlogn) sorting runtime. 

However, even with shuffling, the worst-case scenario happens when the input list has many repeated items.
One way to work around that is to three-way partition as shown below, only proceed with the "<" and ">" partitions, and ignoring "=" partition. 
This Quick-sort partition is usually the one used in most libraries and typically very fast in practice.

#### Three-way partitions

``` python
def quicksort3(mlist, lo=0, hi=None):
    """ Quick-sort using three-way partition strategy.
    """

    def partition3(mlist, lo, hi):
        """ In-place three-way partition of the list will return [< pivot] [== pivot] [> pivot]

        The two-way partition ([< pivot] [>= pivot]) seen in previous quicksort has the following degenerate cases:
         1. Almost sorted lists. -> Defense: Use random swaps to scramble the lists before sorting.
         2. Almost equal items. -> Defense: Use this three-way partition strategy.
        """
        pivot = mlist[hi-1]

        idx1 = lo
        for i in range(lo, hi-1):
            if mlist[i] < pivot:
                mlist[i], mlist[idx1] = mlist[idx1], mlist[i]
                idx1 += 1

        idx2 = idx1
        for i in range(idx1, hi-1):
            if mlist[i] == pivot:
                mlist[i], mlist[idx2] = mlist[idx2], mlist[i]
                idx2 += 1

        # move the pivot to the right partition
        mlist[idx2], mlist[hi - 1] = mlist[hi - 1], mlist[idx2]

        return idx1, idx2

    if hi is None:
        hi = len(mlist)

    if lo == hi:
        # empty list
        return mlist
    elif lo == hi - 1:
        # singleton list
        return mlist
    else:
        p, q = partition3(mlist, lo, hi)
        quicksort(mlist, lo, p)
        quicksort(mlist, q + 1, hi)
        return mlist
```

### Quick Select

Sometimes, interview questions will involve "order statistics", such as finding k-th smallest element in an array.
To do this, you select a random pivot and partition the array as you would in the Quicksort algorithm.
Then, based on the index of the pivot element, you know which half of the array contains the desired element.
For example: k=10 and n=20, if the first half contains 5 elements, then you should ignore the first half, and recursively process the second half with k=4 and n=14.
The runtime of this algorithm is O(n), not O(n log n), since the recursive call is only on one half of the array.

#### Find median

Find median is a special case of finding k-th smallest item. 
You still have to implement finding k-th smallest helper function.

``` python
def find_median(mlist):
    """ Find the median of a given list of numbers.
    """
    def partition(alist, lo, hi):
        pivot = alist[hi - 1]
        idx = lo

        for i in range(lo, hi-1):
            if alist[i] < pivot:
                alist[i], alist[idx] = alist[idx], alist[i]
                idx += 1
        # move the pivot
        alist[idx], alist[hi - 1] = alist[hi - 1], alist[idx]
        return idx

    def find_kth(mlist, k, lo, hi):
        if lo == hi:
            # empty list
            return None
        elif lo == hi-1:
            # singleton list
            return mlist[lo] if k == lo else None
        else:
            p = partition(mlist, lo, hi)
            if p == k:
                return mlist[p]
            elif p < k:
                return find_kth(mlist, k, p+1, hi)
            else:
                return find_kth(mlist, k, lo, p)
        pass

    length = len(mlist)
    if length == 0:
        return None

    if length % 2 == 1:
        # if odd length
        return find_kth(mlist, length/2, 0, length)
    else:
        # if length is even
        first = find_kth(mlist, length/2-1, 0, length)
        second = find_kth(mlist, length/2, 0, length)
        return (first+second)/2.0
```
