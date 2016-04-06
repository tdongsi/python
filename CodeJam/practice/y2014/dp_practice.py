"""
Created on Oct 17, 2015

@author: cdongsi
"""

def maximal_subarray(number_list):
    """
    Given an array, find the subarray with the maximum sum.
    """
    
    sum = 0
    running_sum = [0] * len(number_list)
    for idx, num in enumerate(number_list):
        sum += num
        running_sum[idx] = sum
    
#     print number_list
#     print running_sum
    
    bot_idx = -1
    bot = max(number_list) # some large value
    peak_bot_idx = -1
    peak_idx = -1
    diff = 0 # some small value
    
    for idx, sum in enumerate(running_sum):
        if (sum < bot):
            bot_idx = idx
            bot = sum
            if peak_bot_idx == -1:
                peak_bot_idx = bot_idx
            
        if (sum - bot > diff):
            diff = sum - bot
            peak_idx = idx
            peak_bot_idx = bot_idx
    
    print "Bottom: %d, Peak: %d" % (peak_bot_idx, peak_idx)
    print "Maximum subarray sum: %d" % diff
    
    return number_list[peak_bot_idx+1:peak_idx+1]


def test_maximal_subarray():
    """
    Test maximal_subarray
    """
    
    input_list = [1, -3, 5, -2, 9, -8, -6, 4]
    print maximal_subarray(input_list)


def find_coin_number(sum, coins):
    """
    Given a list of N coins, their values (V1, V2, ... , VN), and the total sum S. 
    Find the minimum number of coins the sum of which is S (we can use as many coins of one type as we want), 
    or report that it's not possible to select coins in such a way that they sum up to S.
    Retun -1 if it's not possible
    """
    
    min_coin = min(coins)
    numbers = [-1]*(sum+1)
    
    if min_coin > sum:
        return -1
    
    numbers[0] = 0
    
    for total in range(1, sum+1):
        
        # initialized to sum large value
        LARGE_VALUE = 2*sum
        min_num = LARGE_VALUE
        
        for coin in coins:
#             print numbers
            if (total-coin >= 0) and numbers[total-coin] >= 0:
                if min_num > (numbers[total-coin] + 1):
                    min_num = numbers[total-coin] + 1
        
        if (min_num != LARGE_VALUE):
            numbers[total] = min_num
    
    return numbers[sum]


def test_find_coint_number():
    """
    Run tests
    """
    sum = 79
    
    coins_1 = [1, 5, 10, 25, 100]
    print find_coin_number(sum, coins_1)
    
    coins_2 = [5, 10, 25, 100]
    print find_coin_number(sum, coins_2)
    
    coins_3 = [2, 5, 10, 25, 100]
    print find_coin_number(sum, coins_3)
    
    sum_3 = 3
    print find_coin_number(sum_3, coins_3)


def main():
    
#     test_find_coint_number()
    test_maximal_subarray()


if __name__ == '__main__':
    main()