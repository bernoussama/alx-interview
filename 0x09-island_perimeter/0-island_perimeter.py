#!/usr/bin/python3
"""
island perimeter
"""


def island_perimeter(grid):
    """island perimeter"""

    def left(x, y):
        return (x + 1, y)

    def down(x, y):
        return (x, y + 1)

    def right(x, y):
        return (x - 1, y)

    def up(x, y):
        return (x, y - 1)

    def traverse(x, y, visited):
        if (x, y) in visited:
            return 0
        visited.add((x, y))

        perim = 0

        # Check all four directions
        for nx, ny in [left(x, y), right(x, y), up(x, y), down(x, y)]:
            if (
                nx < 0
                or ny < 0
                or nx >= len(grid)
                or ny >= len(grid[0])
                or grid[nx][ny] == 0
            ):
                perim += 1
            elif grid[nx][ny] == 1:
                perim += traverse(nx, ny, visited)

        return perim

    x, y = 0, 0
    for idx, _ in enumerate(grid):
        for j, n in enumerate(grid[idx]):
            if n == 1:
                x, y = idx, j
                break
        else:
            continue  # only executed if the inner loop did NOT break
        break

    return traverse(x, y, set())
