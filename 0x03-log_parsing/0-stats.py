#!/usr/bin/python3
"""Defines a module that reads stdin line by line and computes logs"""

import sys

if __name__ == "__main__":

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
                timer -= 1
                file_size += int(line.split(" ")[-1])
                code = line.split(" ")[-2]
                status_codes[code] += 1
                size = "File size: {:d}".format(file_size)
                logs = "\n".join("{}: {}".format(key, val)
                                 for key, val in status_codes.items() if val)
                if timer == 0:
                    print(size)
                    print(logs)
                    timer = 10
                    logs = ""
        except KeyboardInterrupt:
            print(size)
            print(logs)

    get_stats()
