#!/usr/bin/python3
"""
Log parsing
"""

import sys

if __name__ == '__main__':

    def print_stats(stats: dict, file_size: int) -> None:
        """
        Prints statistics including file size and counts
        of different HTTP status codes.
        """
        print("File size: {:d}".format(file_size))
        for k, v in sorted(stats.items()):
            if v:
                print("{}: {}".format(k, v))

    def get_stats() -> None:
        """
        Reads stdin line by line, computes file size and
        counts of different HTTP status codes,
        and prints statistics every 10 lines.
        """
        filesize, count = 0, 0
        codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
        stats = {k: 0 for k in codes}

        try:
            for line in sys.stdin:
                count += 1
                data = line.split()
                try:
                    status_code = data[-2]
                    stats[status_code] += 1
                except BaseException:
                    pass
                try:
                    filesize += int(data[-1])
                except BaseException:
                    pass
                if count % 10 == 0:
                    print_stats(stats, filesize)
            print_stats(stats, filesize)
        except KeyboardInterrupt:
            print_stats(stats, filesize)
            raise

    get_stats()
