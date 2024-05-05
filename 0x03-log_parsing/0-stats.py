#!/usr/bin/python3
"""Defines a module that reads stdin line by line and computes metrics"""

import sys


def print_logs(file_size: int, status_codes: dict) -> None:
    """Prints the logs metrics"""
    size = "File size: {:d}".format(file_size)
    print(size)
    for key, val in status_codes.items():
        if val:
            print("{}: {}".format(key, val))


def get_stats() -> None:
    """reads stdin line by line and computes logs"""
    lines = sys.stdin
    timer = 10
    file_size = 0
    codes = {
               '200': 0, '301': 0, '400': 0,
               '401': 0, '403': 0, '404': 0,
               '405': 0, '500': 0
            }
    status_codes = codes.copy()
    try:
        for line in lines:
            try:
                timer -= 1
                file_size += int(line.split(" ")[-1])
                code = line.split(" ")[-2]
                status_codes[code] += 1
            except BaseException:
                pass
            if timer == 0:
                print_logs(file_size, status_codes)
                timer = 10
        print_logs(file_size, status_codes)
    except KeyboardInterrupt:
        print_logs(file_size, status_codes)


if __name__ == "__main__":
    get_stats()
