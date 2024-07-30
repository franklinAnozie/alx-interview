#!/usr/bin/python3
""" nqueens algo """

import sys


def is_point_safe(board: list[list], n: int, col: int) -> bool:
    """ checking if point is safe """
    for i in range(n):
        if board[i][1] == col or \
           board[i][1] - board[i][0] == col - n or \
           board[i][1] + board[i][0] == col + n:
            return False
    return True


def recurse(board: list[list],
            n: int, N: int, solutions: list[list[list]]) -> None:
    """ recursively placing queen """
    if n == N:
        solutions.append([row[:] for row in board])
    else:
        for col in range(N):
            if is_point_safe(board, n, col):
                board[n][1] = col
                recurse(board, n+1, N, solutions)


def nqueens(N: int) -> list[list[list]]:
    """ fxn entry point """
    board: list[list] = [[i, -1] for i in range(N)]
    solutions: list[list[list]] = []
    recurse(board, 0, N, solutions)
    return solutions


if __name__ == "__main__":
    args = sys.argv
    if len(args) == 2:
        try:
            n = int(args[1])
            if n < 4:
                print("N must be at least 4")
                sys.exit(1)
            solutions = nqueens(n)
            for solution in solutions:
                print(solution)
        except ValueError:
            print("N must be a number")
            sys.exit(1)
    else:
        print("Usage: nqueens N")
        sys.exit(1)
