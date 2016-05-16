
import heapq
import itertools


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