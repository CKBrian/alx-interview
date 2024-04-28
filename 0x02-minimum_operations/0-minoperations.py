#!/usr/bin/python3
"""
    Defines a method that calculates the fewest number of dperations
    needed to result in exactly n H characters in the file
"""


def minOperations(n: int) -> int:
    """ Returns the no of Operations needed to get n H characters """
    if n == 1:
        return 0
    nxt = 'H'
    msg = 'H'
    dp = 0
    while (len(msg) < n):
        if n % len(msg) == 0:
            dp += 2
            nxt = msg
            msg += msg
        else:
            dp += 1
            msg += nxt
    if len(msg) != n:
        return 0
    return dp
