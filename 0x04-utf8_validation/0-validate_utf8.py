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
    bytes_following = 0
    for byte in data:
        if bytes_following > 0:
            if byte >> 6 != 0b10:
                return False
            bytes_following -= 1
        else:
            if byte >> 7 == 0:
                continue
            elif byte >> 5 == 0b110:
                bytes_following = 1
            elif byte >> 4 == 0b1110:
                bytes_following = 2
            elif byte >> 3 == 0b11110:
                bytes_following = 3
            else:
                return False
    return bytes_following == 0
