#!/usr/bin/python3
import sys


def is_safe(board, row, col, n):
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


def solve_n_queens(n):
    board = [[0 for x in range(n)] for y in range(n)]
    solutions = []

    def solve(board, col, n):
        if col == n:
            solution = []
            for row in board:
                solution.append(''.join(['Q' if x == 1 else '.' for x in row]))
            solutions.append(solution)
            return
        for row in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1
                solve(board, col + 1, n)
                board[row][col] = 0
    solve(board, 0, n)
    return solutions


if __name__ == '__main__':
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
    solutions = solve_n_queens(n)
    for solution in solutions:
        for row in solution:
            print(row)
        print()
