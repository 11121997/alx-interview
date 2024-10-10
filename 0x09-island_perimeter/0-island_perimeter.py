#!/usr/bin/python3
"""Island Perimeter Module"""


def island_perimeter(grid):
    """function that returns the perimeter of the island described in grid"""

    width = len(grid[0])
    height = len(grid)
    perimeter = 0

    for i in range(height):
        for k in range(width):
            if grid[i][k] == 1:
                perimeter += 4

                if k > 0 and grid[i][k - 1] == 1:
                    perimeter -= 2

                if i > 0 and grid[i - 1][k] == 1:
                    perimeter -= 2

    return perimeter
