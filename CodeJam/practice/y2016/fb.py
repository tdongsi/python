import unittest


def watched_length(alist):
    """ Return the total watched time from a disjoint time intervals.

    :param alist: A list of disjoint time intervals
    :return: total sum
    """
    _sum = 0
    for ele in alist:
        start, end = ele
        _sum += end - start

    return _sum


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


def combine_intervals(alist):
    """ Merge list of number intervals.
    For example: 4-6, 5-8, 20-25 -> 4-8, 20-25

    :param alist: list of number intervals.
    :return: Merged list of number intervals.
    """

    if len(alist) <= 1:
        return alist
    else:
        med = len(alist)/2
        left = combine_intervals(alist[:med])
        right = combine_intervals(alist[med:])
        return merge(left, right)


class TestCode(unittest.TestCase):

    def test_merge_intervals(self):
        mlist = [(4, 6), (5, 8), (20, 25)]
        expected = [(4, 8), (20, 25)]
        self.assertEqual(expected, combine_intervals(mlist))

        mlist = [(4, 6), (5, 8), (20, 25), (25, 26)]
        expected = [(4, 8), (20, 26)]
        self.assertEqual(expected, combine_intervals(mlist))

        mlist = [(4, 6), (5, 8), (4, 25), (25, 26)]
        expected = [(4, 26)]
        self.assertEqual(expected, combine_intervals(mlist))

        mlist = [(4, 6), (5, 8), (4, 5), (25, 26)]
        expected = [(4, 8), (25, 26)]
        self.assertEqual(expected, combine_intervals(mlist))

        mlist = [(4, 6), (5, 8), (3, 5), (25, 26)]
        expected = [(3, 8), (25, 26)]
        self.assertEqual(expected, combine_intervals(mlist))

        mlist = [(4, 6), (7, 8), (5, 7), (25, 26)]
        expected = [(4, 8), (25, 26)]
        self.assertEqual(expected, combine_intervals(mlist))

        mlist = [(4, 6), (7, 8), (4, 26), (5, 7), (25, 26)]
        expected = [(4, 26)]
        self.assertEqual(expected, combine_intervals(mlist))
        pass


if __name__ == "__main__":
    unittest.main()
