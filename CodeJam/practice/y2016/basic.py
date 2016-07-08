
import heapq
import itertools


def quicksort_July(alist, lo=0, hi=None):
    if hi is None:
        hi = len(alist)

    if lo == hi:
        # empty list
        return alist
    elif lo == hi-1:
        # singleton list
        return alist
    else:
        pivot = partition(alist, lo, hi)
        quicksort_July(alist, lo, pivot)
        quicksort_July(alist, pivot+1, hi)
        return alist


def partition(alist, lo, hi):

    pivot = alist[hi-1]
    j = lo
    for i in range(lo, hi-1):
        if alist[i] < pivot:
            alist[j], alist[i] = alist[i], alist[j]
            j += 1
    alist[j], alist[hi-1] = alist[hi-1], alist[j]
    return j


def binary_search_June(alist, item, start=0, end=None):
    if end is None:
        end = len(alist)

    if start == end:
        # empty list
        return -1
    elif start == end-1:
        # singleton list
        if alist[start] == item:
            return start
        else:
            return -1
    else:
        med = (start+end) // 2
        if alist[med] == item:
            return med
        elif alist[med] > item:
            return binary_search_June(alist, item, start, med)
        else:
            return binary_search_June(alist, item, med+1, end)


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


def mergesort_June(mlist):

    def merge(left, right):

        out = []
        idx1 = 0
        idx2 = 0

        while idx1 < len(left) and idx2 < len(right):
            if left[idx1] < right[idx2]:
                out.append(left[idx1])
                idx1 += 1
            else:
                out.append(right[idx2])
                idx2 += 1

        out.extend(left[idx1:])
        out.extend(right[idx2:])
        return out

    if len(mlist) <= 1:
        return mlist
    else:
        mid = len(mlist)/2
        left = mergesort_June(mlist[:mid])
        right = mergesort_June(mlist[mid:])
        return merge(left, right)


def rotate(matrix):
    """ Rotate matrix counter-clockwise.

    Counter-closewise rotation is transpose + reverse ordering.
    """
    temp = [list(e) for e in zip(*matrix)]
    return temp[::-1]


def transpose(matrix):
    """ Transpose matrix.
    """
    # zip returns the transpose with each row as tuple instead of list
    return [list(e) for e in zip(*matrix)]


def print_matrix(matrix):
    print "* Matrix *"
    for row in matrix:
        print row


def spiral_list(matrix):
    """ Print the matrix to a list of items in spiral.

    First going right to end of row, then going down, then left, then up.

    :param matrix:
    :return:
    """
    # print_matrix(matrix)
    mlist = []

    if len(matrix) == 0:
        return mlist
    elif len(matrix) == 1:
        mlist.extend(matrix[0])
        return mlist
    else:
        mlist.extend(matrix[0])
        matrix_t = rotate(matrix[1:])
        mlist.extend(spiral_list(matrix_t))
        return mlist
    pass


def mergesort(mlist):

    def merge(first, second):
        idx1 = 0
        idx2 = 0
        result = []
        while idx1 < len(first) and idx2 < len(second):
            if first[idx1] < second[idx2]:
                result.append(first[idx1])
                idx1 += 1
            else:
                result.append(second[idx2])
                idx2 += 1

        result.extend(first[idx1:])
        result.extend(second[idx2:])
        return result

    if len(mlist) <= 1:
        return mlist

    med = len(mlist)//2
    first = mergesort(mlist[:med])
    second = mergesort(mlist[med:])
    return merge(first, second)


def quicksort2(mlist):
    """ Conceptual Quick-sort algorithm (not in-place).
    """
    if len(mlist) <= 1:
        return mlist

    pivot = mlist[0]
    left = [e for e in mlist if e < pivot]
    right = [e for e in mlist if e >= pivot]
    right.remove(pivot)

    result = quicksort2(left)
    result.append(pivot)
    result.extend(quicksort2(right))
    return result


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

    pass


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


def reverse_words(inputs):
    reverse_in = inputs[::-1]
    tokens = reverse_in.split(' ')
    out = ' '.join([token[::-1] for token in tokens])
    return out


class PriorityQueue(object):

    REMOVED = "<removed-task>"

    def __init__(self):
        self.heap = []
        self.entries = {}
        self.counter = itertools.count()

    def add_task(self, task, priority=0):
        if task in self.entries:
            self.remove_task(task)

        count = next(self.counter)
        # weight = -priority since heapq is a min-heap
        entry = [-priority, count, task]
        self.entries[task] = entry
        heapq.heappush(self.heap, entry)
        pass

    def remove_task(self, task):
        """ Mark the given task as REMOVED.

        Do this to avoid breaking heap-invariance of the internal heap.

        :param task:
        :return:
        """
        entry = self.entries[task]
        entry[-1] = PriorityQueue.REMOVED
        pass

    def pop_task(self):
        """ Get task with highest priority.

        :return: Task with highest priority
        """
        while self.heap:
            weight, count, task = heapq.heappop(self.heap)
            if task is not PriorityQueue.REMOVED:
                del self.entries[task]
                return task
        raise KeyError("The priority queue is empty")

    def __str__(self):
        temp = [str(e) for e in self.heap if e[-1] is not PriorityQueue.REMOVED]
        return "[%s]" % ", ".join(temp)


def solve_skyline(mlist):
    return []


def heap_sort(mlist):
    heapq.heapify(mlist)
    return [heapq.heappop(mlist) for e in range(len(mlist))]


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


def atoi(sinput):
    """ Convert string to integer.

    :param input:
    :return:
    """

    neg = False
    num = sinput
    if sinput[0] == "-":
        neg = True
        num = sinput[1:]

    total = 0
    for c in num:
        total *= 10
        total += int(c)
    if neg:
        total = -total

    return total