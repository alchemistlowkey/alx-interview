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

    byte = 0
    while byte < len(data):
        if data[byte] >> 7 == 0:
            byte += 1
        else:
            num_bytes = 0
            while (data[byte] >> (7 - num_bytes)) & 1:
                num_bytes += 1
            if num_bytes < 2 or num_bytes > 4:
                return False
            for size in range(1, num_bytes):
                byte += 1
                if byte >= len(data) or (data[byte] >> 6) != 0b10:
                    return False
            byte += 1
    return True
