#!/usr/bin/python3
"""
 min operations to reach n characters
"""


# copyAll(l) => l*2
def minOperations(n: int) -> int:
    """
    min operations to reach n characters
    """
    factors: list[int] = []
    divisor = 2
    while n > 1:
        # divide by divisor if it's divisible
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return sum(factors)
