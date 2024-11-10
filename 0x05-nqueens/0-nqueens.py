#!/usr/bin/python3

import sys


def is_safe(board, row, col, n):
    """
    Check if a queen can be placed on board[row][col]
    """
    # Check this row on left side
    for j in range(col):
        if board[row][j] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(n):
    """
    Solve the N queens problem and print all solutions
    """
    # Initialize the board
    board = [[0 for x in range(n)] for y in range(n)]
    solutions = []

    def solve_util(board, col):
        # Base case: If all queens are placed, return True
        if col >= n:
            solution = []
            for i in range(n):
                for j in range(n):
                    if board[i][j] == 1:
                        solution.append([i, j])
            solutions.append(solution)
            return

        # placing this queen in all rows one by one
        for i in range(n):
            if is_safe(board, i, col, n):
                # Place this queen in board[i][col]
                board[i][col] = 1

                # Recur to place rest of the queens
                solve_util(board, col + 1)

                # If placing queen in board[i][col] doesn't lead to a solution,
                # then remove queen from board[i][col]
                board[i][col] = 0

    # Start from first column
    solve_util(board, 0)

    # Print all solutions
    for solution in solutions:
        print(solution)


def main():
    """Main function to handle input and run the program"""
    # Check number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n)


if __name__ == "__main__":
    main()
