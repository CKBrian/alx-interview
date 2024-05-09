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
    num_bytes_following = 0
    for byte in data:
        if num_bytes_following > 0:
            if byte >> 6 != 0b10:
                return False  # Invalid continuation byte
            num_bytes_following -= 1
        else:
            if byte >> 7 == 0:
                continue  # Single-byte character
            elif byte >> 5 == 0b110:
                num_bytes_following = 1
            elif byte >> 4 == 0b1110:
                num_bytes_following = 2
            elif byte >> 3 == 0b11110:
                num_bytes_following = 3
            else:
                return False  # Invalid leading byte
    return num_bytes_following == 0
