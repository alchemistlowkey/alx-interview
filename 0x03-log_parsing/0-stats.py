#!/usr/bin/python3
"""
Script to read stdin line by line and compute metrics.
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status
code> <file size>
After every 10 lines and/or a keyboard interruption (CTRL + C), print these
statistics from the beginning:
Total file size: File size: <total size>
where <total size> is the sum of all previous <file size> (see input format
above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear or is not an integer, don’t print anything
for this status code
format: <status code>: <number>
status codes should be printed in ascending order
"""
import sys


def compute_metrics(total_size, status_codes):
    """
    Reads stdin line by line, computes metrics, and prints statistics after
    every 10 lines or upon keyboard interruption.

    Args:
        total_size (int):
            The total file size computed from the processed lines.
        status_codes (dict):
            A dictionary containing the count of lines for each status code.
    """
    print(f"File size: {total_size}")
    for key, value in sorted(status_codes.items()):
        if value > 0:
            print(f"{key}: {value}")


total_size = 0
status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()
        # Check if line matches the expected format
        if len(parts) > 2:
            size = int(parts[-1])
            status = (parts[-2])
            total_size += size
            if status in status_codes:
                status_codes[status] += 1

            line_count += 1

            if line_count % 10 == 0:
                compute_metrics(total_size, status_codes)
                line_count = 0

except KeyboardInterrupt:
    pass
finally:
    compute_metrics(total_size, status_codes)
