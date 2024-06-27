#!/usr/bin/python3
"""
Module for validating UTF-8 encoding
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    Args:
        data (list): List of integers representing the data set.
    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    n_bytes = 0

    for num in data:
        bin_rep = format(num, '#010b')[-8:]

        if n_bytes == 0:
            if bin_rep.startswith('110'):
                n_bytes = 1
            elif bin_rep.startswith('1110'):
                n_bytes = 2
            elif bin_rep.startswith('11110'):
                n_bytes = 3
            elif bin_rep.startswith('10'):
                return False
        else:
            if not bin_rep.startswith('10'):
                return False
            n_bytes -= 1

    return n_bytes == 0
