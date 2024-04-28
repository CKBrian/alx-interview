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
    body = 'H'
    dp = 0
    while (len(body) < n):
        if n % len(body) == 0:
            dp += 2
            nxt = body
            body += body
        else:
            dp += 1
            body += nxt
    if len(body) != n:
        return 0
    return dp
