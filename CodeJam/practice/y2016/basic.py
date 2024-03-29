
import heapq
import itertools
import collections


def insertion_sort(mlist):
    if len(mlist) <= 1:
        return mlist

    for i in range(1, len(mlist)):
        pos = i
        cur = mlist[i]

        while pos > 0 and cur < mlist[pos-1]:
            mlist[pos] = mlist[pos-1]
            pos -= 1
        mlist[pos] = cur

    return mlist


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
    print("* Matrix *")
    for row in matrix:
        print(row)


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


def quicksort3(mlist, lo=0, hi=None):
    """ Quick-sort using three-way partition strategy.

    See comment below to see when to use three-way partition strategy and this sorting.
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

    _REMOVED = "<REMOVED>"

    def __init__(self):
        self.heap = []
        self.entries = {}
        self.counter = itertools.count()

    def add(self, task, priority=0):
        """Add a new task or update the priority of an existing task"""
        if task in self.entries:
            self.remove(task)

        count = next(self.counter)
        # weight = -priority since heap is a min-heap
        entry = [-priority, count, task]
        self.entries[task] = entry
        heapq.heappush(self.heap, entry)
        pass

    def remove(self, task):
        """ Mark the given task as REMOVED.

        Do this to avoid breaking heap-invariance of the internal heap.
        """
        entry = self.entries[task]
        entry[-1] = PriorityQueue._REMOVED
        pass

    def pop(self):
        """ Get task with highest priority.

        :return: Priority, Task with highest priority
        """
        while self.heap:
            weight, count, task = heapq.heappop(self.heap)
            if task is not PriorityQueue._REMOVED:
                del self.entries[task]
                return -weight, task
        raise KeyError("The priority queue is empty")

    def peek(self):
        """ Check task with highest priority, without removing.

        :return: Priority, Task with highest priority
        """
        while self.heap:
            weight, count, task = self.heap[0]
            if task is PriorityQueue._REMOVED:
                heapq.heappop(self.heap)
            else:
                return -weight, task

        return None

    def __str__(self):
        temp = [str(e) for e in self.heap if e[-1] is not PriorityQueue._REMOVED]
        return "[%s]" % ", ".join(temp)


Point = collections.namedtuple('Point', ['x', 'y'])


def merge_skyline(shape1, shape2):
    """ Check if two shapes are overlapping. Return combined shape if overlapped.

    :param shape1: list of points for shape1
    :param shape2: list of points for shape2
    :return: The combined shape, None if the two shapes are not overlapping.
    """
    out = []
    cur_y = 0
    lidx = 0
    ridx = 0
    l_y = 0
    r_y = 0

    while lidx < len(shape1) and ridx < len(shape2):
        if shape1[lidx].x < shape2[ridx].x:
            cur_x = shape1[lidx].x
            l_y = shape1[lidx].y
            if max(l_y, r_y) != cur_y:
                cur_y = max(l_y, r_y)
                out.append(Point(cur_x, cur_y))
            lidx += 1

        elif shape1[lidx].x > shape2[ridx].x:
            cur_x = shape2[ridx].x
            r_y = shape2[ridx].y
            if max(l_y, r_y) != cur_y:
                cur_y = max(l_y, r_y)
                out.append(Point(cur_x, cur_y))
            ridx += 1

        else:
            # shape1[lidx].x == shape2[ridx].x
            cur_x = shape1[lidx].x
            l_y = shape1[lidx].y
            r_y = shape2[ridx].y
            max_y = max(l_y, r_y)
            if max_y != cur_y:
                cur_y = max_y
                out.append(Point(cur_x, cur_y))
                lidx += 1
                ridx += 1

    while lidx < len(shape1):
        cur_x = shape1[lidx].x
        l_y = shape1[lidx].y
        if max(l_y, r_y) != cur_y:
            cur_y = max(l_y, r_y)
            out.append(Point(cur_x, cur_y))
        lidx += 1

    while ridx < len(shape2):
        cur_x = shape2[ridx].x
        r_y = shape2[ridx].y
        if max(l_y, r_y) != cur_y:
            cur_y = max(l_y, r_y)
            out.append(Point(cur_x, cur_y))
        ridx += 1

    return out


def solve_skyline(mlist):
    """ Solve the skyline problem.

    :param mlist: list of buildings in format (start, end, height).
    :return: List of end points
    """

    def buildings_to_endpoints(building):
        """ Convert (start, end, height) tuple to (start_point, end_point).
        start_point and end_point are corners of the building.

        :param building: (start, end, height) tuple
        :return:
        """
        start, end, height = building
        return Point(start, height), Point(end, 0)

    def skyline(shapes):
        """ Recursively solve the skyline problem.

        :param shapes: list of shapes. Each shape is a list of multiple points.
        :return: list of points for the skyline.
        """
        if len(shapes) <= 2:
            return shapes

        building = len(shapes)/2
        med = building/2
        med *= 2
        left = skyline(shapes[:med])
        right = skyline(shapes[med:])
        return merge_skyline(left, right)

    endpoints = []
    for building in mlist:
        endpoints.extend(buildings_to_endpoints(building))
    return [(pt.x, pt.y) for pt in skyline(endpoints)]


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


def dfs(graph, start):
    """ Simple depth first search.

    :param graph: a dict that map a node to a set of its neighbor.
    :param start: starting node
    :return: ordered list of visited nodes.
    """
    visited = []
    stack = [start]

    while stack:
        ele = stack.pop()
        if ele not in visited:
            visited.append(ele)
            stack.extend(graph[ele] - set(visited))

    return visited


def bfs(graph, start):
    """ Simple breadth first search.

    :param graph: a dict that map a node to a set of its neighbor.
    :param start: starting node
    :return: ordered list of visited nodes.
    """

    visited = []
    queue = collections.deque([start])

    while queue:
        ele = queue.popleft()
        if ele not in visited:
            visited.append(ele)
            queue.extend(graph[ele] - set(visited))

    return visited