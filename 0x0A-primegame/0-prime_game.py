#!/usr/bin/python3
# Goal:
    # Maria and Ben are playing a game. Given a set of consecutive integers starting from 1 up to and including n,
    #  they take turns choosing a prime number from the set and removing that number and its multiples from the set.
    #  The player that cannot make a move loses the game.

# Sample inputs: isWinner(5, [2, 5, 1, 4, 3])
# Sample outputs: Winner: Ben
# Strategy: 
    # Maria picks 2 and removes 2, 4, leaving 1, 3, 5
    # Ben picks 3 and removes 3, leaving 1, 5
    # Maria picks 5 and removes 5, leaving 1
    # Maria wins because there are no prime numbers left for Ben to choose
    # Third round: 1
# constraints:
    # where x is the number of rounds and nums is an array of n
    # Return: name of the player that won the most rounds
    # If the winner cannot be determined, return None
    # You can assume n and x will not be larger than 10000
    # You cannot import any packages in this task
# Solution:
#     Determine if the number is prime using the is_prime function. Then find its multiples if available using .
#     If not prime, and an 
#         is_prime(n) returns True if n is a prime number and False if it is not

def is_prime(n):
    """Check if a number is a prime number."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


def isWinner(x, nums):
    '''Returns a winner in a prime game'''
    player = 'maria'
    winner = None

    for _ in range(x):

        for n in nums:
            if is_prime(n):
                nums.remove(n)

        winner = 'ben' if player == 'maria' else 'maria'
        player = winner
        print(winner)

    return winner