#!/usr/bin/python3
"""
A method that determines if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing individual bytes of data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """

    remaining_bytes = 0

    for size in data:
        if remaining_bytes:
            if size >> 6 == 0b10:
                remaining_bytes -= 1
            else:
                return False
        else:
            if size >> 7 == 0:
                remaining_bytes = 0
            elif size >> 5 == 0b110:
                remaining_bytes = 1
            elif size >> 4 == 0b1110:
                remaining_bytes = 2
            elif size >> 3 == 0b11110:
                remaining_bytes = 3
            else:
                return False

    return remaining_bytes == 0
