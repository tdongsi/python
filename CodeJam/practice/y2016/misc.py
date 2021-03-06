
import heapq
import itertools
from collections import defaultdict
from practice.y2016.basic import PriorityQueue


def merge_sorted_lists(*lists):
    """ Merge a number of sorted number lists into a single sorted list.

    :param lists: list of sorted lists
    :return: single list of sorted items.
    """
    merged = []
    heap = []

    # reverse each list for convenient pop()
    for mlist in lists:
        mlist.reverse()

    for idx, mlist in enumerate(lists):
        if len(mlist) > 0:
            heapq.heappush(heap, (mlist.pop(), idx))

    while len(heap) > 0:
        item, idx = heapq.heappop(heap)
        merged.append(item)
        if len(lists[idx]) > 0:
            heapq.heappush(heap, (lists[idx].pop(), idx))

    # undo reverse each list for convenient pop()
    for mlist in lists:
        mlist.reverse()

    return merged


def combine_intervals(alist):
    """ Merge list of number intervals.
    For example: 4-6, 5-8, 20-25 -> 4-8, 20-25

    :param alist: list of number intervals.
    :return: Merged list of number intervals.
    """

    def overlap(interval1, interval2):
        """ Check if two number intervals overlap. Return the merged number interval.

        :param interval1: tuple (start, end) for first number interval
        :param interval2: tuple (start, end) for second number interval
        :return: merged number interval. Return None if the two intervals do not overlap.
        """
        # Assumption: interval1[0] <= interval2[0]
        if interval1[0] > interval2[0]:
            interval1, interval2 = interval2, interval1

        if interval1[0] <= interval2[0] <= interval1[1]:
            return interval1[0], max(interval1[1], interval2[1])
        else:
            return None

    def merge_item(out, item, staging):
        """ Merge item into a common list.

        :param out: common list
        :param item: new interval
        :param staging: current staging interval
        :return:
        """
        if staging is None:
            staging = item
        else:
            new_staging = overlap(staging, item)
            if new_staging is None:
                # No overlapping
                out.append(staging)
                staging = item
            else:
                # item and staging overlapped
                staging = new_staging

        # return new staging
        return staging

    def merge(left, right):
        """ Merge two list of number intervals into one.

        :param left:
        :param right:
        :return:
        """
        if len(left) == 0:
            return right
        elif len(right) == 0:
            return left

        out = []
        staging = None
        lidx = 0
        ridx = 0

        while lidx < len(left) and ridx < len(right):
            if left[lidx] < right[ridx]:
                staging = merge_item(out, left[lidx], staging)
                lidx += 1
            else:
                staging = merge_item(out, right[ridx], staging)
                ridx += 1

        while lidx < len(left):
            staging = merge_item(out, left[lidx], staging)
            lidx += 1

        while ridx < len(right):
            staging = merge_item(out, right[ridx], staging)
            ridx += 1

        # append the final item
        out.append(staging)
        return out

    if len(alist) <= 1:
        return alist
    else:
        med = len(alist)/2
        left = combine_intervals(alist[:med])
        right = combine_intervals(alist[med:])
        return merge(left, right)


def solve_skyline(mlist):
    """ Solve the Skyline problem.

    :param mlist: list of buildings in format (start, end, height).
    :return: List of end points
    """

    skyline = []
    cur_height = 0
    pq = PriorityQueue()
    events = defaultdict(list)
    START = "start"
    END = "end"

    for idx, building in enumerate(mlist):
        start, end, height = building
        events[start].append((idx, START))
        events[end].append((idx, END))

    # k_events is the ordered list of x-coordinates where buildings start or end (events)
    k_events = sorted(events.keys())

    # Add and remove buildings into a priority-queue for each event.
    for key in k_events:
        # print skyline
        buildings = events[key]

        for e in buildings:
            idx, label = e
            if label == START:
                pq.add(idx, mlist[idx][2])
            elif label == END:
                pq.remove(idx)

        # after processing all buildings for a x-coordinate "key", check the current highest building
        temp = pq.peek()
        new_height = 0
        if temp is not None:
            new_height = temp[0]
        if new_height != cur_height:
            skyline.append((key, new_height))
            cur_height = new_height

    return skyline


class SkylineTracker(object):
    """ Supporting class for solving Skyline problem.
    A heap-based priority-queue for buildings.
    """

    REMOVED = "<REMOVED>"

    def __init__(self):
        self.heap = []
        self.entries = {}
        self.counter = itertools.count()

    def add(self, building, height=0):
        """ Add building into the max heap.

        :param building: building ID
        :param height: height
        :return:
        """
        if building in self.entries:
            self.remove(building)

        count = next(self.counter)
        # weight = -height since heapq is a min-heap
        entry = [-height, count, building]
        self.entries[building] = entry
        heapq.heappush(self.heap, entry)
        pass

    def remove(self, building):
        """ Mark the given building as REMOVED.

        Do this to avoid breaking heap-invariance of the internal heap.

        :param building: building ID
        :return:
        """
        entry = self.entries[building]
        entry[-1] = SkylineTracker.REMOVED
        pass

    def pop(self):
        """ Get highest building.

        :return: Highest building
        """
        while self.heap:
            height, count, building = heapq.heappop(self.heap)
            if building is not SkylineTracker.REMOVED:
                del self.entries[building]
                return -height, building
        raise KeyError("The priority queue is empty")

    def peek(self):
        """ Get highest building.

        :return: Highest building
        """
        while self.heap:
            height, count, building = self.heap[0]
            if building is SkylineTracker.REMOVED:
                heapq.heappop(self.heap)
            else:
                return -height, building

        return None

    def __str__(self):
        temp = [str(e) for e in self.heap if e[-1] is not SkylineTracker.REMOVED]
        return "[%s]" % ", ".join(temp)

