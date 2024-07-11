#!/usr/bin/python3
"""Minimum Operations Module"""


def minOperations(n):
    """write a method that calculates the fewest number of operations
    needed to result in exactly n H characters in the file"""
    have = 1
    start = 0
    op = 0
    while have < n:
        remainder = n - have
        if (remainder % have == 0):
            start = have
            have += start
            op += 2
        else:
            have += start
            op += 1
    return op
