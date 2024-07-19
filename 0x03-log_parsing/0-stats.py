#!/usr/bin/python3
import sys
import signal

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_stats():
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) != 7:
            continue
        ip, dash, date, request, protocol, status, size = parts
        if request != '"GET' or protocol != 'HTTP/1.1"' or not status.isdigit() or not size.isdigit():
            continue
        status = int(status)
        size = int(size)
        total_size += size
        if status in status_codes:
            status_codes[status] += 1
        line_count += 1
        if line_count % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
