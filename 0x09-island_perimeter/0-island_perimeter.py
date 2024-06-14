#!/usr/bin/python3
'''
This module contains a function that returns
the perimeter of the island described in grid
'''
from typing import List


def island_perimeter(grid: List[List[int]]) -> int:
    '''
    Calculates the perimeter of a land represented in a 2D matrix

    Args:
        grid (list): 2D matrix representation of land

    Returns:
        int: The perimeter of the land
    '''
    perimeter: int = 0

    def has_side(side: int) -> int:
        '''Checks if a side is present'''
        return 0 if side == 1 else 1

    for row in range(len(grid)):
        for cell in range(len(grid[row])):
            if grid[row][cell] == 1:
                s_up = has_side(grid[row - 1][cell] if row > 0 else 0)
                s_down = has_side(grid[row + 1][cell]
                                  if row < len(grid) - 1 else 0)
                s_left = has_side(grid[row][cell - 1] if cell > 0 else 0)
                s_right = has_side(grid[row][cell + 1]
                                   if cell < len(grid[row]) - 1 else 0)
                perimeter += s_up + s_down + s_left + s_right

    return perimeter
