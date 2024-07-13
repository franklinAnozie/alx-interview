#!/usr/bin/python3
""" minimum operations """


def minOperations(n) -> int:
    value = 0
    divisor = 2

    if n <= 1:
        return value

    while n > 1:
        while n % divisor == 0:
            value += divisor
            n = n // divisor
        divisor += 1

    return value
