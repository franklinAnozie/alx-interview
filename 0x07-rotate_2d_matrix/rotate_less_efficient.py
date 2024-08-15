#!/usr/bin/env python3
""" rotate matrix 90 degrees """

from typing import List


def rotate_matrix(matrix: List[List]) -> List:
    length_of_matrix = len(matrix)
    new_matrix = []
    smaller_matrix = []
    count = 0
    last = length_of_matrix - 1
    while count < length_of_matrix:
        smaller_matrix.append(matrix[last][count])
        if last == 0:
            count += 1
            last = length_of_matrix - 1
            new_matrix.append(smaller_matrix)
            smaller_matrix = []
        else:
            last -= 1
    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[i])):
            matrix[i][j] = new_matrix[i][j]


if __name__ == "__main__":
    to_rotate = [[1,  2,  3,  4,  5], [6,  7,  8,  9,  10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
    ## to_rotate = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix = rotate_matrix(to_rotate)
    print(to_rotate)
