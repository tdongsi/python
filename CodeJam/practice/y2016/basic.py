
import heapq
import itertools


def quicksort2(mlist, lo=0, hi=None):
    """ Quick-sort algorithm with in-place implementation.
    """
    def partition(mlist, lo, hi):
        i = lo
        pivot = mlist[hi-1]
        for j in range(lo+1, hi-1):
            if mlist[j] < pivot:
                mlist[i], mlist[j] = mlist[j], mlist[i]
                i += 1
        mlist[i], mlist[hi-1] = mlist[hi-1], mlist[i]
        return i

    if hi is None:
        hi = len(mlist)

    if lo == hi:
        return mlist
    elif lo == hi-1:
        return mlist

    p = partition(mlist, lo, hi)
    quicksort2(mlist, lo, p)
    quicksort2(mlist, p+1, hi)

    return mlist


def quicksort(mlist):

    if len(mlist) <= 1:
        return mlist

    pivot = mlist[0]
    left = [e for e in mlist if e < pivot]
    right = [e for e in mlist if e >= pivot]
    right.remove(pivot)

    result = quicksort(left)
    result.append(pivot)
    result.extend(quicksort(right))
    return result


def merge_sort(mlist):

    def _merge_sort(start, end):
        if start == end:  # empty list
            return []
        elif start == end-1:  # singleton list
            return mlist[start:end]
        else:
            med = (start+end)/2
            first = _merge_sort(start, med)
            second = _merge_sort(med, end)
            return _merge(first, second)

    def _merge(first, second):
        idx1 = 0
        idx2 = 0
        li = []

        while idx1 < len(first) and idx2 < len(second):
            if first[idx1] < second[idx2]:
                li.append(first[idx1])
                idx1 += 1
            else:
                li.append(second[idx2])
                idx2 += 1

        if idx1 < len(first):
            li.extend(first[idx1:])
        if idx2 < len(second):
            li.extend(second[idx2:])

        return li

    if len(mlist) == 0 or len(mlist) == 1:
        return mlist
    else:
        return _merge_sort(0, len(mlist))


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
    heap = []
    for e in mlist:
        heapq.heappush(heap, e)
    return [heapq.heappop(heap) for i in xrange(len(mlist))]


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


def bin_search(mlist, num, start=0, end=None):
    """ Binary search.

    :param mlist:
    :param num:
    :return: -1 if num is not found in the list
    """
    if start < 0:
        raise ValueError("start cannot be negative")
    if end is None:
        end = len(mlist)

    if start == end:
        # empty sublist
        return -1

    if start == end-1:
        # singleton sublist
        if mlist[start] == num:
            return start
        else:
            return -1

    med = (start + end) // 2
    if mlist[med] == num:
        return med
    elif mlist[med] > num:
        return bin_search(mlist, num, start, med)
    else:
        return bin_search(mlist, num, med+1, end)


def bin_search_old(mlist, num):
    """ Binary search.

    :param mlist:
    :param num:
    :return: -1 if num is not found in the list
    """

    def _bin_search(mlist, num, start, end):
        if start == end:
            # empty sublist
            return -1

        if start == end-1:
            # singleton sublist
            if mlist[start] == num:
                return start
            else:
                return -1

        med = (start + end) // 2
        if mlist[med] == num:
            return med
        elif mlist[med] > num:
            return _bin_search(mlist, num, start, med)
        else:
            return _bin_search(mlist, num, med+1, end)

    return _bin_search(mlist, num, 0, len(mlist))


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