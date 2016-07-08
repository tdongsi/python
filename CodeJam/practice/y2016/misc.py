
import heapq


def merge_sorted_lists(*lists):
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
    if len(alist) <= 1:
        return alist
    else:
        med = len(alist)/2
        left = combine_intervals(alist[:med])
        right = combine_intervals(alist[med:])
        return merge(left, right)


def merge(left, right):
    if len(left) == 0:
        return right
    elif len(right) == 0:
        return left

    out = []
    ol = overlap(left[-1], right[0])
    if ol is not None:
        out.extend(left[:-1])
        out.append(ol)
        out.extend(right[1:])
    else:
        out.extend(left)
        out.extend(right)
    return out


def overlap(interval1, interval2):
    # Assumption: interval1[0] <= interval2[0]
    if interval1[0] > interval2[0]:
        interval1, interval2 = interval2, interval1

    if interval1[0] <= interval2[0] <= interval1[1]:
        return interval1[0], max(interval1[1], interval2[1])
    else:
        return None