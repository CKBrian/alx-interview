#!/usr/bin/python3
'''
This module contains a function that returns
the perimeter of the island described in grid
'''


def island_perimeter(grid):
    '''
    Calculates the perimeter of a land represented in a 2D matric

    Args:
        grid (list): 2D matrix representation of land

    Returns:
        int: The perimeter of the land
    '''
    perimeter = 0
    s_up = 0
    s_down = 0
    s_left = 0
    s_right = 0
    sides = 0
    has_side = lambda x: 0 if x == 1 else 1

    for row in range(0, len(grid) - 1):
        for cell in range(0, len(grid[row]) - 1):
            if grid[row][cell] == 1:
                if row > 0 and row < len(grid) - 1:
                    s_up = has_side(grid[row - 1][cell])
                    s_down = has_side(grid[row + 1][cell])

                if cell > 0 and cell < len(grid[row]) - 1:
                    s_left = has_side(grid[row][cell - 1])
                    s_right = has_side(grid[row][cell + 1])

                sides = s_up + s_down + s_left + s_right
                perimeter += sides
    return perimeter
