#!/usr/bin/python3
'''
This module contains a function that returns
the perimeter of the island described in grid
'''


def island_perimeter(grid) -> int:
    '''
    Calculates the perimeter of a land represented in a 2D matrix

    Args:
        grid (list): 2D matrix representation of land

    Returns:
        int: The perimeter of the land
    '''
    perimeter = 0

    def has_side(side: int) -> int:
        '''Checks if a side is present'''
        return 0 if side == 1 else 1

    for row in range(len(grid)):
        for cell in range(len(grid[row])):
            if grid[row][cell] == 1:
                s_up = (1 if row == 0 or not grid[row - 1][cell]
                        else 0)

                s_down = (1 if row == len(grid) - 1 or not grid[row + 1][cell]
                          else 0)
                s_left = 1 if cell == 0 or not grid[row][cell - 1] else 0

                s_right = (1 if cell == len(grid[row]) - 1 or
                           not grid[row][cell + 1] else 0)
                perimeter += s_up + s_down + s_left + s_right
    return perimeter
