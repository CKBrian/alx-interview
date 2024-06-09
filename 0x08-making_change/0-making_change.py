#!/usr/bin/python3

'''
Makes coin change
'''

def makeChange(coins, total):
    '''Returns the fewest number of coins needed to make the given total'''
    if total <= 0:
        return 0

    memo = {}
    min_coins = findMinCoins(total, coins, memo)
    return min_coins if min_coins != float('inf') else -1

    if total <= 0:
        return 0
    check = 0
    temp = 0
    coins.sort(reverse=True)
    for i in coins:
        while check < total:
            check += i
            temp += 1
        if check == total:
            return temp
        check -= i
        temp -= 1
    return -1
