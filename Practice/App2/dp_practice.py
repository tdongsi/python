'''
Created on Oct 17, 2015

@author: cdongsi
'''


def find_coin_number(sum, coins):
    '''
    Given a list of N coins, their values (V1, V2, ... , VN), and the total sum S. 
    Find the minimum number of coins the sum of which is S (we can use as many coins of one type as we want), 
    or report that it's not possible to select coins in such a way that they sum up to S.
    Retun -1 if it's not possible
    '''
    
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
    '''
    Run tests
    '''
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
    
    test_find_coint_number()

if __name__ == '__main__':
    main()