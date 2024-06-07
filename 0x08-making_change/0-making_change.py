#!/usr/bin/python3

'''
Makes coin change
'''


def findMinCoins(total, coins, memo):
    '''Determines the minimum number of coins needed
       to make a given total recursively'''
    if total in memo:
        return memo[total]

    if total == 0:
        return 0

    if total < 0:
        return float('inf')

    min_coins = float('inf')
    for coin in coins:
        result = findMinCoins(total - coin, coins, memo)
        if result != float('inf'):
            min_coins = min(min_coins, result + 1)

    memo[total] = min_coins
    return min_coins


def makeChange(coins, total):
    '''Returns the fewest number of coins needed to make the given total'''
    if total <= 0:
        return 0

    memo = {}
    min_coins = findMinCoins(total, coins, memo)
    return min_coins if min_coins != float('inf') else -1
