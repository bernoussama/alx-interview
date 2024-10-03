#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Return the pascal triangle
    """
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    triangle = [[1]]
    for i in range(n - 1):
        tmp = [0] + triangle[-1] + [0]
        row = []
        for j in range(len(triangle[-1]) + 1):
            row.append(tmp[j] + tmp[j + 1])
        triangle.append(row)
    return triangle
