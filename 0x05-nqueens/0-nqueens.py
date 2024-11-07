#!/usr/bin/python3

import sys
from typing import List


def nqueens(n) -> List[List[int]]:
    """N queens"""
    col = set()
    pos_diag = set()
    neg_diag = set()
    res = []
    board = [["."] * n for _ in range(n)]
    answer = []

    def backktrack(row):
        positions = []
        if row == n:
            res.append(["".join(row) for row in board])
            return
        for i in range(n):
            if i in col or row + i in pos_diag or row - i in neg_diag:
                continue

            col.add(i)
            pos_diag.add(row + i)
            neg_diag.add(row - i)
            board[row][i] = "Q"
            positions.append([row, i])
            backktrack(row + 1)
            col.remove(i)
            pos_diag.remove(row + i)
            neg_diag.remove(row - i)
            board[row][i] = "."
        answer.append(positions) if positions else None

    backktrack(0)
    return answer


if __name__ == "__main__":
    n = int(sys.argv[1])
    res = nqueens(n)
    for i in res:
        print(i)
