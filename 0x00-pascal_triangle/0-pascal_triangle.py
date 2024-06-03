#!/usr/bin/python3
""" An implementation of Paschal's Triangle in Python """

def pascal_triangle(n):
    """ function definition of paschal triangle """
    if n <= 0:
        return []
    retVal = [[1]]
    for i in range(n - 1):
        temp = [0] + retVal[-1] + [0]
        row = []
        for j in range(len(retVal[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
        retVal.append(row)
    return retVal
