#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N non-attacking queens
on an N×N chessboard. Write a program that solves the N queens problem.
"""
import sys


def is_safe(board, row, col, n):
    """
    Checks if it's safe to place a queen at board[row][col]

    Args:
        board (list): The chessboard represented as a 2D list.
        row (int): The row index of the position to check.
        col (int): The column index of the position to check.
        size (int): The size of the board.

    Returns:
        bool:
            True if it's safe to place a queen at the given position
    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_u(board, col, n, solutions):
    """
    Utility function to solve N queens problem
    """
    if col >= n:
        queens_positions = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    queens_positions.append([i, j])
        solutions.append(queens_positions)
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1

            solve_nqueens_u(board, col + 1, n, solutions)

            board[i][col] = 0


def solve_nqueens(n):
    """
    A function to solve N queens problem
    """
    if not type(int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens_u(board, 0, n, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(n)
