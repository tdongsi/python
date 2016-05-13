
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