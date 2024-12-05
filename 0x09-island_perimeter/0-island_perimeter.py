#!/usr/bin/python3
"""
island perimeter
"""


def island_perimeter(grid):
    """island perimeter"""

    perim = 0
    rows, cols = len(grid), len(grid[0])
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perim += 4
                if row < rows - 1 and grid[row + 1][col] == 1:
                    perim -= 1
                if col < cols - 1 and grid[row][col + 1] == 1:
                    perim -= 1
                if row > 0 and grid[row - 1][col] == 1:
                    perim -= 1
                if col > 0 and grid[row][col - 1] == 1:
                    perim -= 1

    return perim
