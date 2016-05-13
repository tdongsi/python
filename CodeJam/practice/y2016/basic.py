
def bin_search(mlist, num):
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