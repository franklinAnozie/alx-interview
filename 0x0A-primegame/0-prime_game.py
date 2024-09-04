#!/usr/bin/python3

def makeSetInRound(num):
    return set(range(1, num + 1))


def isPrime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def isWinner(x, nums):
    winner = {"Maria": 0, "Ben": 0}

    for round in range(x):
        primeCount = 0
        s_o_n = makeSetInRound(nums[round])
        for num in s_o_n:
            if isPrime(num):
                primeCount += 1
        if primeCount % 2 or primeCount == 0:
            winner["Ben"] += 1
        else:
            winner["Maria"] += 1

    if winner["Ben"] > winner["Maria"]:
        return "Ben"
    elif winner["Maria"] > winner["Ben"]:
        return "Maria"
    else:
        return None
