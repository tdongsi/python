---
layout: post
title: "Tutorial: Basic algorithms"
date: 2016-09-02 01:04:37 -0700
comments: true
categories:
- Tutorial
- Algorithm
- TODO 
---

For sorting algorithms, see [this post](/blog/2016/08/30/tutorial-sorting-algorithms/).

<!--more-->

### Binary search

``` python Binary search
def binary_search(mlist, item):
    """ Binary search

    :param mlist: sorted list in ascending order
    :param item:
    :return: index of item in list. -1 if not found.
    """

    def _bin_search(start, end):
        if start == end:
            # empty
            return -1
        elif start == end-1:
            # singleton
            if mlist[start] == item:
                return start
            else:
                return -1
        else:
            med = (start+end)/2
            if mlist[med] == item:
                return med
            elif mlist[med] < item:
                return _bin_search(med+1, end)
            else:
                return _bin_search(start, med)

    if len(mlist) == 0:
        return -1
    else:
        return _bin_search(0, len(mlist))
```

For more advanced binary operations, check `bisect` module. 
Using `bisect` module for binary search will be awkward and not recommended in an interview.

