#!/usr/bin/python3
"""
    rotate 2d matrix clockwise in place
"""


def rotate_2d_matrix(matrix):
    """
    rotate 2d matrix clockwise in place
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        matrix[i].reverse()
