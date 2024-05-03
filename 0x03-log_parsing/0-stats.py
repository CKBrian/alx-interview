#!/usr/bin/python3
"""Defines a module that reads stdin line by line and computes logs"""

import sys
import signal


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
                code_count = status_codes.get(code, 0) + 1
                status_codes.update({code: code_count})
                size = f"File size: {file_size}"
                logs = "\n".join(f"{key}: {val}"
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
