#!/usr/bin/python3
"""
Validate UTF-8 encoding of a file.
"""


from typing import List


def validUTF8(data: List[int]):
    """
    Validate UTF-8 encoding
    """

    def countOnes(byt: int):
        count = 0
        for b in range(7, -1, -1):
            if byt & (1 << b):
                count += 1
            else:
                break
        return count

    idx = 0
    while idx < len(data):
        byt = data[idx]
        count = 0

        count = countOnes(byt)
        # For a 1-byte character, the first bit is a 0
        if count == 0:
            idx += 1
            continue

        if count == 1 or count > 4:
            return False

        # For an n-bytes character,
        # the first n bits are all one's,
        # the n + 1 bit is 0,
        for n in range(idx + 1, idx + count):
            # followed by n - 1 bytes
            # with the most significant 2 bits being 10.
            if countOnes(data[n]) != 1:
                return False

        idx += count - 1
    return True
