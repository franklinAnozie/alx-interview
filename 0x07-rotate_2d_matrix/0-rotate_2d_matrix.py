#!/usr/bin/env python3
""" rotate matrix 90 degrees """

from typing import List


def rotate_matrix(matrix: List[List[int]]) -> List[List[int]]:
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


if __name__ == "__main__":
    to_rotate = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix = rotate_matrix(to_rotate)
    print(to_rotate)
