#!/usr/bin/python3
"""
Validate UTF-8 encoding of a file.
"""


from typing import List


def validUTF8(data: List[int]):
    """
    Validate UTF-8 encoding
    """
    valid = False
    # print(format(0b10000000 >> 6, "08b"))
    idx = 0
    while idx < len(data):
        byt = data[idx]
        if byt >> 6 == 0b10:
            return valid
        valid = True

        # For a 1-byte character, the first bit is a 0, followed by its Unicode code.
        if byt >> 7 == 0b0:
            continue

        # For an n-bytes character,
        # the first n bits are all one's,
        # the n + 1 bit is 0,
        if byt >> 6 == 0b11:
            if byt >> 5 == 0b110:
                if data[idx + 1] >> 6 == 0b10:
                    valid = True
                    idx = idx + 2
            else:
                return valid
        # followed by n - 1 bytes with the most significant 2 bits being 10.
