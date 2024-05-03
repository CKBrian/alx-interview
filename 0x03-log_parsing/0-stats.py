#!/usr/bin/env python3
"""Defines a module that reads stdin line by line and computes metrics"""
import sys
import signal


metrics = ""


def signal_handler(sig, frame):
    """Handling keyboard interruption (CTRL + C)"""
    print(sig, metrics)


def get_stats():
    """reads stdin line by line and computes metrics"""
    global metrics
    lines = sys.stdin
    timer = 10
    file_size = 0
    codes = {
                   '200': 0, '301': 0, '400': 0,
                   '401': 0, '403': 0, '404': 0,
                   '405': 0, '500': 0
                   }
    status_codes = codes.copy()
    signal.signal(signal.SIGINT, signal_handler)
    for line in lines:
        timer -= 1
        file_size += int(line.split(" ")[-1])
        code = line.split(" ")[-2]
        code_count = status_codes.get(code) + 1
        status_codes.update({code: code_count})
        metrics = (f"File size: {file_size}\n" +
                   "\n".join(f"{int(key)}: {val}"
                             for key, val in status_codes.items() if val))
        if timer == 0:
            print(metrics)
            timer = 10
            file_size = 0
            status_codes = codes.copy()
            metrics = ""


if __name__ == "__main__":
    get_stats()
