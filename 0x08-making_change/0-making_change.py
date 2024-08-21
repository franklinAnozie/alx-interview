#!/usr/bin/python3
""" making change """


def makeChange(coins, total):
    """ makeChange Algo """
    coins.sort(reverse=True)

    num_coins = 0
    f_total = total
    for coin in coins:
        if total <= 0:
            break
        count = total // coin
        num_coins += count
        total -= count * coin
    return num_coins if total == 0 or f_total <= 0 else -1
