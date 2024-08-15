#!/usr/bin/python3
"""
rotate matrix 90 degrees
"""


def rotate_2d_matrix(matrix: list[list[int]]) -> list[list[int]]:
    """
    rotates a 2 by 2 matrix by 90 degrees
    """
    n = len(matrix)

    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer

        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]

            matrix[first][i] = matrix[last - offset][first]
            matrix[last - offset][first] = matrix[last][last - offset]
            matrix[last][last - offset] = matrix[i][last]
            matrix[i][last] = top
