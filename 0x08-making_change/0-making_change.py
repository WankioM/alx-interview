#!/usr/bin/python3
""" The function returns the fewest number of coins needed to meet the target total.
If the total is 0 or less, it returns 0.
If the target total cannot be met with the available coins, it returns -1. """


def makeChange(coins, total):
    """ Generate changes needed to reach total

    Args:
        coins ([List]): [List of Coins available]
        total ([int]): [total amount needed]
    """
    if total <= 0:
        return 0
    check = 0
    temp = 0
    coins.sort(reverse=True)
    for i in coins:
        while check < total:
            check += i
            temp += 1
        if check == total:
            return temp
        check -= i
        temp -= 1
    return -1
