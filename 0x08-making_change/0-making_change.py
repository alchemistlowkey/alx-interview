#!/usr/bin/python3
"""
Given a pile of coins of different values,
determine the fewest number of coins needed to meet a given amount total.

Prototype: def makeChange(coins, total)
Return: fewest number of coins needed to meet total
If total is 0 or less, return 0
If total cannot be met by any number of coins you have, return -1
coins is a list of the values of the coins in your possession
The value of a coin will always be an integer greater than 0
You can assume you have an infinite number of each
denomination of coin in the list
Your solution’s runtime will be evaluated in this task
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list of int): List of coin denominations available.
        total (int): The amount to be achieved using the coins.

    Returns:
        int: Fewest number of coins needed to meet the total.
             Returns -1 if the total cannot be met by any number of coins.
    """
    if total <= 0:
        return 0

    sorted_coins = sorted(coins, reverse=True)
    coin_length = len(coins)
    coin_position = 0
    count = 0

    while total > 0:
        if coin_position >= coin_length:
            return -1
        if total - sorted_coins[coin_position] >= 0:
            total -= sorted_coins[coin_position]
            count += 1
        else:
            coin_position += 1
    return count
