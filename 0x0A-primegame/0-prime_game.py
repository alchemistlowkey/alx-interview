#!/usr/bin/python3
"""
Maria and Ben are playing a game.
Given a set of consecutive integers starting from 1 up to and including n,
they take turns choosing a prime number from the set and removing that number
and its multiples from the set.
The player that cannot make a move loses the game.

They play x rounds of the game, where n may be different for each round.
Assuming Maria always goes first and both players play optimally,
determine who the winner of each game is.

Prototype: def isWinner(x, nums)
where x is the number of rounds and nums is an array of n
Return: name of the player that won the most rounds
If the winner cannot be determined, return None
You can assume n and x will not be larger than 10000
You cannot import any packages in this task
Example:

x = 3, nums = [4, 5, 1]
First round: 4

Maria picks 2 and removes 2, 4, leaving 1, 3
Ben picks 3 and removes 3, leaving 1
Ben wins because there are no prime numbers left for Maria to choose
Second round: 5

Maria picks 2 and removes 2, 4, leaving 1, 3, 5
Ben picks 3 and removes 3, leaving 1, 5
Maria picks 5 and removes 5, leaving 1
Maria wins because there are no prime numbers left for Ben to choose
Third round: 1

Ben wins because there are no prime numbers for Maria to choose
Result: Ben has the most wins
"""


def is_prime(n):
    """
    Check if a number is prime.

    Args:
    num (int): The number to check.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    sieve = [True] * n
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * int((n - i * i - 1) / (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


def playMatch(n):
    """
    plays a single round
    """
    primes = is_prime(n + 1)
    return 1 - (len(primes) % 2) if n > 1 else 1


def isWinner(x, nums):
    """
    Determine the winner of the game.

    Args:
    x (int): The number of rounds.
    nums (list of int): An array of n for each round.

    Returns:
    str or None:
        The name of the player who won the most rounds.
        If the winner cannot be determined, returns None.
    """
    if type(x) is not int or x < 1:
        return None
    players = {0: 'Maria', 1: 'Ben'}
    wins = {0: 0, 1: 0}
    for num in nums:
        wins[playMatch(num)] += 1
    return (None if wins[0] == wins[1]
            else players[0] if wins[0] > wins[1]
            else players[1])
