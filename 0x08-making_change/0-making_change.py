#!/usr/bin/python3
"""Change comes from within"""


def makeChange(coins, total):
    """
    determine the fewest number of coins
    needed to meet a given amount total
    """
    if total <= 0:
        return 0

    counter = 0
    idx = 0
    coins = sorted(coins, reverse=True)
    length = len(coins)

    while total > 0:
        if idx >= length:
            return -1
        if total - coins[idx] >= 0:
            total -= coins[idx]
            counter += 1
        else:
            idx += 1
    return counter
