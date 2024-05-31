#!/usr/bin/python3
'''@D matrix module'''


def rotate_2d_matrix(matrix):
    """Returns a +90 degree rotated 2D matrix.
    Args:
        matrix(list): A 2D list of numbers
    Return: A new 2D list representing the rotated matrix
    """
    for i in range(len(matrix)):
        for z in range(i):
            matrix[i][z], matrix[z][i] = matrix[z][i], matrix[i][z]

    for row in matrix:
        matrix.reverse()
