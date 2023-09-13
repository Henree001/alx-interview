#!/usr/bin/python3
"""The minimum operations coding challenge.
"""


def minOperations(n):
    """Computes the fewest number of operations needed to result
    in exactly n H characters.
    """
    if n <= 1:
        return 0

    factor = 2
    num_operations = 0

    while factor <= n:
        if n % factor == 0:
            num_operations += factor
            n //= factor
        else:
            factor += 1
    return num_operations
