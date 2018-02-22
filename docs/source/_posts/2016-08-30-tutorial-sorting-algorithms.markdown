---
layout: post
title: "Tutorial: Sorting algorithms"
date: 2016-08-30 21:23:48 -0700
comments: true
categories: 
- Tutorial
- Algorithm
---

Quick overview and implementations of the most common sorting algorithms.

Most updated implementations are in [this Python module](https://github.com/tdongsi/python/blob/master/CodeJam/practice/y2016/basic.py).

<!-- more -->

### Sorting algorithms

#### Overview of space/time complexity

| | Time Complexity (Avg/Worst) | Space Complexity | In-place/Stable? | Notes |
| --- | --- | --- | --- | --- |
| **Heapsort** |  O(n * log n) / O(n * log n) | O(1) | Yes/No | NA |
| **Mergesort** | O(n * log n) / O(n * log n).| O(n) | No/Yes | Space O(1) for doubly-linked list. |
| **Quicksort** | O(n * log n) / O(n * n) | O(1) | Yes/No | It is stable for linked-list. |
| **Insertion sort** | O(n * n) / O(n * n) | O(1) | Yes/Yes | Adaptive: quick for largely sorted list. Online. Efficient for small lists. |
| **Selection sort** | O(n * n) / O(n * n) | O(1) | Yes/No | Adaptive: similar to Insertion Sort. More comparisons. Less write operations. |
| **Counting sort** | O(n + k) / O(n + k) | O(1) | ?/? |  Not comparison-sort. For small range. |
| **Radix sort** | O(w * n) / O(w * n) | O(1) | Yes/Yes (some variants) |  Not comparison-sort. *w -> log n* for arbitrary range. |

<br>

Note that **insertion sort** still has its place even though it is not a `O(n * log n)` algorithm. 
It is shown in practice that "insertion sort" is faster than other sorting algorithms for sufficiently small, mostly sorted lists. 
A common application of "insertion sort" is in **merge sort** implementations where 
"merge sort" calls its own internal "insertion sort" to sort small enough sub-lists before merging (instead of keeping recursing to singleton lists).

**Selection sort** seems inferior to **insertion sort** as an O(n^2) sorting algorithm in most cases.
However, selection sort will perform identically regardless of the order of the array (almost sorted or unsorted), which can be a plus in real-time application.
While selection sort is preferable to insertion sort in terms of number of writes (Θ(n) swaps versus Ο(n2) swaps), **cycle sort** is the most optimal in "number of write" metric (write can be expensive in some situations).

#### How to approach sorting questions

Simply using quick-sort for any sorting in algorithmic questions could fail you, since it shows inexperience.
Asking clarifying questions is key: sorting a very large list of integers can have different approach, depending on its input size, data structure, numeric range and distribution.

* Small range: O(n) with array-based map.
* Medium range: O(wn) with radix sort.
* Arbitrary number: O(n log n)

**Example**: "Design an algorithm to sort a list".

* What kind of list? Array list or linked list? Array list.
* What data in it? Numbers or characters or strings? Numbers.
* Are numbers integers? Yes.
* What range of numbers? Are they IDs or values of something? Ages of customers.
* How many numbers? One million.

Based on the answers above, the best solution is to use an array of size 200 to keep count of customers for a given age. 
Size 200 is chosen because the oldest person is less than 200 years old. 
You can see that the space and time complexity is much different from Merge-Sort when you know characteristics of input data.  

### Merge Sort

``` python
def merge_sort(mlist):
    def _merge(left, right):
        alist = []
        l_idx = 0
        r_idx = 0

        while l_idx < len(left) and r_idx < len(right):
            if left[l_idx] < right[r_idx]:
                alist.append(left[l_idx])
                l_idx += 1
            else:
                alist.append(right[r_idx])
                r_idx += 1

        # append the rest
        alist.extend(left[l_idx:])
        alist.extend(right[r_idx:])

        return alist

    if len(mlist) <= 1:
        return mlist
    else:
        med = len(mlist) // 2
        left = merge_sort(mlist[:med])
        right = merge_sort(mlist[med:])
        return _merge(left, right)
```

### Quick Sort

One important characteristic of Quick Sort is in-place. 
Naive implementation tends to ignore this, focusing on its divide-and-conquer strategy.
The standard implementation is as follows, but see [this post](/blog/2016/08/31/tutorial-more-about-quick-sort/) for more details.

``` python
def quicksort(mlist, lo=0, hi=None):

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


    if hi is None:
        hi = len(mlist)

    if lo == hi:
        # empty list
        return mlist
    elif lo == hi-1:
        # singleton list
        return mlist
    else:
        p = partition(mlist, lo, hi)
        quicksort(mlist, lo, p)
        quicksort(mlist, p+1, hi)
        return mlist
```

### Heap Sort

Straight from `heapq` module's documentation.

``` python
def heap_sort(mlist):
    heapq.heapify(mlist)
    return [heapq.heappop(mlist) for e in range(len(mlist))]
```

### Insertion Sort

``` python Insertion sort
def insertion_sort(mlist):
    if len(mlist) <= 1:
        return mlist

    for i in xrange(1, len(mlist)):
        pos = i
        cur = mlist[i]

        while pos > 0 and cur < mlist[pos-1]:
            mlist[pos] = mlist[pos-1]
            pos -= 1
        mlist[pos] = cur

    return mlist
```

### Selection sort

``` python Selection sort
def selection_sort(mlist):
    for i in range(0, len(mlist)-1):
        iMin = i
        for j in range(i+1, len(mlist)):
            if mlist[j] < mlist[iMin]:
                iMin = j

        if iMin != i:
            mlist[iMin], mlist[i] = mlist[i], mlist[iMin]

    return mlist
```

### Counting Sort

Based on [this lecture](https://www.youtube.com/watch?v=Nz1KZXbghj8&t=1925s).

``` python Counting Sort
def counting_sort(mlist, k=None, key=None):
    """Counting sort

    :param mlist: List of items.
    :param k: Maximum range of key [0,k)
    :param key: function to get key of item. (for radix sort)
    :return:
    """
    if k is None:
        k = max(mlist) + 1

    if key is None:
        key = lambda x: x

    counter = [[] for i in range(k)]
    for i in range(len(mlist)):
        counter[key(mlist[i])].append(mlist[i])

    output = []
    for i in range(k):
        output.extend(counter[i])
    return output
```

### Radix Sort

Use `counting_sort` in the last section as the subroutine.
See [here](https://www.youtube.com/watch?v=Nz1KZXbghj8&t=1925s).

``` python Radix sort
def radix_sort(mlist, w=None):
    RADIX = 10

    # Find the max length
    if w is None:
        temp = max(mlist)
        w = 0
        while temp > 0:
            w += 1
            temp //= RADIX

    output = mlist
    for digit in range(w):
        def my_key(num):
            for _ in range(digit):
                num //= RADIX
            return num % RADIX

        output = counting_sort(output, RADIX, my_key)
        # print(output)

    return output
```

### Testing sorting algorithms

Codes to verify your sorting algorithm. 

``` python
import your_module.your_sort_impl as do_sort

class TestSorting(unittest.TestCase):

    def test_sort(self):
        # import sorting function as do_sort
        for i in xrange(1, 20):
            # Do it 5 times
            expected = range(i)
            for i in xrange(5):
                mlist = expected[:]
                random.shuffle(mlist)
                # print mlist
                self.assertEqual(do_sort(mlist), expected)

        pass

    def test_same_element(self):

        self.assertEqual(do_sort([2, 3, 5, 7, 4, 2, 6, 1]), [1, 2, 2, 3, 4, 5, 6, 7])
        self.assertEqual(do_sort([2, 2]), [2, 2])
        self.assertEqual(do_sort([1, 2, 1]), [1, 1, 2])
        self.assertEqual(do_sort([2, 3, 1, 2, 2, 4, 3, 1]), [1, 1, 2, 2, 2, 3, 3, 4])
        self.assertEqual(do_sort([2, 1]), [1, 2])
        pass
```
