
import heapq
import itertools


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
    pq = SkylineTracker()
    events = []
    START = "start"
    END = "end"

    for idx in range(len(mlist)):
        start, end, height = mlist[idx]
        events.append((start, idx, START))
        events.append((end, idx, END))

    events.sort()

    # Add and remove buildings into a priority-queue (SkylineTracker) for each event.
    for event in events:
        # print skyline
        x, idx, label = event
        height = mlist[idx][2]

        if label == START:
            pq.add_building(idx, height)
        elif label == END:
            pq.remove_building(idx)

        tuple = pq.peek_building()
        after = 0
        if tuple is not None:
            after = tuple[0]
        if after != cur_height:
            skyline.append((x, after))
            cur_height = after

    # merge skyline points with same x
    print skyline
    staging = skyline[0]
    out = []
    for idx in range(1, len(skyline)):
        if staging[0] != skyline[idx][0]:
            out.append(staging)
            staging = skyline[idx]
        else:
            new_staging = (staging[0], max(staging[1], skyline[idx][1]))
            staging = new_staging
    # append the last point
    out.append(staging)

    return out


class SkylineTracker(object):
    """ Supporting class for solving Skyline problem.
    A heap-based priority-queue for buildings.
    """

    REMOVED = "<removed-building>"

    def __init__(self):
        self.heap = []
        self.entries = {}
        self.counter = itertools.count()

    def add_building(self, building, height=0):
        """ Add building into the max heap.

        :param building: building ID
        :param height: height
        :return:
        """
        if building in self.entries:
            self.remove_building(building)

        count = next(self.counter)
        # weight = -height since heapq is a min-heap
        entry = [-height, count, building]
        self.entries[building] = entry
        heapq.heappush(self.heap, entry)
        pass

    def remove_building(self, building):
        """ Mark the given building as REMOVED.

        Do this to avoid breaking heap-invariance of the internal heap.

        :param building: building ID
        :return:
        """
        entry = self.entries[building]
        entry[-1] = SkylineTracker.REMOVED
        pass

    def pop_building(self):
        """ Get highest building.

        :return: Highest building
        """
        while self.heap:
            height, count, building = heapq.heappop(self.heap)
            if building is not SkylineTracker.REMOVED:
                del self.entries[building]
                return -height, building
        raise KeyError("The priority queue is empty")

    def peek_building(self):
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

