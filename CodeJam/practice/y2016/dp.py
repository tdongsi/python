
from collections import Counter

def find_coin_number(total, coin_list):
    """
    Given a list of N coins, their values (V1, V2, ... , VN), and the total sum S.
    Find the minimum number of coins the sum of which is S (we can use as many coins of one type as we want),
    or report that it's not possible to select coins in such a way that they sum up to S.

    :param total:
    :param coin_list:
    :return:
    """

    if not coin_list:
        # Return 0 if coin list is empty
        return -1

    if sum(coin_list) == 0:
        return -1

    coin_list.sort()
    if coin_list[0] > total:
        return -1

    num = [-1] * (total + 1)
    num[0] = 0
    num[coin_list[0]] = 1

    for x in xrange(coin_list[0], total+1):
        tmin = 1000
        for vi in coin_list:
            if x - vi >= 0 and num[x-vi] >= 0:
                cur = num[x-vi] + 1
                if cur < tmin:
                    tmin = cur

        if tmin == 1000:
            num[x] = -1
        else:
            num[x] = tmin

    return num[total]


def rearrange(astr):
    """ Rearrange a string to avoid duplicate characters in sequence.

    :param astr: input string
    :return:
    """
    if len(astr) <= 1:
        return astr

    counter = Counter()
    for c in astr:
        counter[c] += 1

    # largest count > the rest of all counts + 1

    new_string = []

    if len(counter.items()) <= 1:
        return None

    # binary heap: update O(log n)
    # Fibonacci heap: update O(1)

    # while counter is not empty
    while len(counter.items()) > 1:
        # max-heap: update O(log k) -> O(1) << O(log n)
        a, b = counter.most_common(2)

        new_string.append(a[0])
        counter[a[0]] -= 1
        if counter[a[0]] == 0:
            del counter[a[0]]

        new_string.append(b[0])
        counter[b[0]] -= 1
        if counter[b[0]] == 0:
            del counter[b[0]]

    # if the last item in new_string is the same as one in the counter
    items = counter.most_common(1)
    if len(items) == 0:
        return "".join(new_string)

    last_char, last_count = items[0]
    if new_string[-1] == last_char:
        return None
    elif last_count > 1:
        return None
    else:
        new_string.append(last_char)

    return "".join(new_string)


def main():
    print rearrange("AABBCC")


if __name__ == "__main__":
    main()