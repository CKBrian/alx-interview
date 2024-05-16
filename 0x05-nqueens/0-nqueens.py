#!/usr/bin/python3
'''Defines a mdule with a program that solves the N queens problem.'''
import sys
from typing import List, Tuple


def is_safe(board: List[int], row: int, col: int) -> bool:
    '''Check if it's safe to place a queen at the given row and column.'''
    # Check if there's a queen in the same column
    for i in range(row):
        if board[i] == col:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i] == j:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, len(board))):
        if board[i] == j:
            return False

    return True


def solve_nqueens_util(board: List[int], row: int, n: int, solutions:
                       List[List[Tuple[int, int]]],
                       current_solution: List[Tuple[int, int]]) -> None:
    '''Utility function to recursively solve the N queens problem.'''
    if row == n:
        solutions.append(current_solution[:])
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            current_solution.append((row, col))
            solve_nqueens_util(board, row + 1, n, solutions, current_solution)
            current_solution.pop()  # Backtrack


def solve_nqueens(n: int) -> List[List[Tuple[int, int]]]:
    '''Solve the N queens problem and return a list of solutions.'''
    if n < 4:
        print('N must be at least 4')
        sys.exit(1)

    solutions: List[List[Tuple[int, int]]] = []
    board = [-1] * n
    solve_nqueens_util(board, 0, n, solutions, [])
    return solutions


def main() -> None:
    '''Main function to parse command-line arguments and print solutions.'''
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solutions = solve_nqueens(N)

        for solution in solutions:
            print(solution)

    except ValueError:
        print("N must be an integer")
        sys.exit(1)


if __name__ == '__main__':
    main()
