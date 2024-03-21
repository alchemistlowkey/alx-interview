#!/usr/bin/python3
"""
In a text file, there is a single character H.
Your text editor can execute only 2 operations in this file: Copy All & Paste.
Given a number n, write a method that calculates the fewest number of
operations needed to result in exactly n H characters in the file.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
"""


def minOperations(n):
    """
    Calculate the fewest number of operations to have exactly n 'H'
    characters in the file.

    Args:
    - n (int): The desired number of 'H' characters.

    Returns:
    - int: The fewest number of operations needed.
    """
    # If n is 1 or less, no operations needed
    if n <= 1:
        return 0

    ops = 0  # Initialize the number of operations
    curr_H = 1  # Initial 'H' in the file
    clip = 1  # Initial content in the clipboard that's been copied

    # Iterate until the desired number of 'H' characters is reached
    for _ in range(n):
        # If the current number of 'H' characters => n, exit the loop
        if curr_H >= n:
            break

        # If the current number of 'H' characters is a divisor of n, updat clip
        if n % curr_H == 0:
            clip = curr_H  # Update clipboard
            ops += 1  # Increment operations count for copying

        curr_H += clip  # Paste clipboard content into the file
        ops += 1  # Increment operations count for pasting

    return ops  # Return the total number of operations
