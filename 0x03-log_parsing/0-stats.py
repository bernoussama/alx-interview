#!/usr/bin/python3
"""
log parsing
"""

# input format : <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
# <status code> <file size>

from datetime import datetime
import sys
import re
from typing import Any

ip_pattern = r"(((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4})"
exp = r"^{} - \[(.*)\] \"(.*)\" (\d*) (\d*)$".format(ip_pattern)


def parse_line(line):

    result = {}

    match = re.search(
        exp,
        line,
    )
    if match is not None:

        ip = match.group(1)
        result["ip"] = ip

        try:
            # format : [2024-10-24 17:10:11.218665]
            date = datetime.strptime(match.group(5), "%Y-%m-%d %H:%M:%S.%f")
            result["date"] = date

        except ValueError:
            return

        http_method = match.group(6)
        result["http_method"] = http_method

        status_code = match.group(7)
        result["status_code"] = status_code

        file_size = match.group(8)
        result["file_size"] = file_size

        return result

    else:
        return


if __name__ == "__main__":
    lines = 1
    output = {
        "total_file_size": 0,
        "status_codes": {
            200: 0,
            301: 0,
            400: 0,
            401: 0,
            403: 0,
            404: 0,
            405: 0,
            500: 0,
        },
    }
    try:
        for line in sys.stdin:
            result = parse_line(line)
            output["total_file_size"] += int(result["file_size"])
            output["status_codes"][int(result["status_code"])] += 1
            if lines == 10:
                print(f"File size: {output['total_file_size']}")
                for status_code, count in output["status_codes"].items():
                    if count != 0:
                        print(f"{status_code}: {count}")
            lines = lines + 1 if lines < 10 else 1
        _ = sys.stdout.flush()
    except (KeyboardInterrupt, EOFError):
        print(f"File size: {output['total_file_size']}")
        for status_code, count in output["status_codes"].items():
            if count != 0:
                print(f"{status_code}: {count}")
        sys.exit(0)
