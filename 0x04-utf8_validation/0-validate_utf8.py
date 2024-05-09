#!/usr/bin/python3
'''Defines a module with a UTF-8 Validation function'''


def validUTF8(data: list) -> bool:
    '''
    determines if a given data set represents a valid UTF-8 encoding.
    Args:
        data(list): List of integers
    Returns:
        bool: True if data is a valid UTF-8 encoding, else return False
    '''
    less_than_255 = [False for i in data if i > 255]
    if less_than_255 and less_than_255[0] == False:
        return False
    return True
