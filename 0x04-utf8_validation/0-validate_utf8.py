#!/usr/bin/python3
"""This module defines the function validUTF8."""


def validUTF8(data):
    """Determines if a given data set
    represents a valid utf-8 encoding
    """
    number_bytes = 0
    
    for i in data:

        mask_byte = 0b10000000

        if number_bytes == 0:

            while i & mask_byte:
                number_bytes += 1
                mask_byte >>= 1

            if number_bytes == 0:
                continue

            if number_bytes == 1 or number_bytes > 4:
                return False

        else:
            if (i & 0b11000000) != 0b10000000:
                return False

        number_bytes -= 1


    return True

    
