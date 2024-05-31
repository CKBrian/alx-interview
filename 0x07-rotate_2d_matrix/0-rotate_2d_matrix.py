#!/usr/bin/python3


def rotate_2d_matrix(matrix: list) -> list:
    """Returns a +90 degree rotated 2D matrix.

    The function takes a 2D matrix as input and returns a new 2D matrix
    where the elements are rotated by 90 degrees clockwise.

    Args:
        matrix(list): A 2D list of numbers
    Return: A new 2D list representing the rotated matrix
    """
    length = len(matrix)
    for i in range(length):
        rotated_row = []
        for j in range(i, length):
            first = matrix[i][j]
            matrix[i][j], matrix[j][i] = matrix[j][i], first
    for row in matrix:
        row.reverse()
