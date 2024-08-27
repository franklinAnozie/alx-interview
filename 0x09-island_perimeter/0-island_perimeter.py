#!/usr/bin/python3
""" island perimeter algo """


def island_perimeter(grid):
    """ island perimeter function """
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                if i != 0 and i != (len(grid) - 1):
                    if (grid[i-1][j] == 0 or grid[i+1][j] == 0
                       or grid[i][j-1] == 0 or grid[i][j+1] == 0):
                        count += 1
    perimeter = count * 2 + 2

    return perimeter
