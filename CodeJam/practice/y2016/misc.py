
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


def merge_item(out, item, staging):
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


def overlap(interval1, interval2):
    # Assumption: interval1[0] <= interval2[0]
    if interval1[0] > interval2[0]:
        interval1, interval2 = interval2, interval1

    if interval1[0] <= interval2[0] <= interval1[1]:
        return interval1[0], max(interval1[1], interval2[1])
    else:
        return None


def solve_skyline(mlist):
    """ Solve the skyline problem.

    :param mlist: list of buildings in format (start, end, height).
    :return: List of end points
    """
    return []