#!/usr/bin/python3
"""
This module defines the function validUTF8.
"""
def validUTF8(data):
    """Determines if a given data set
    represents a valid utf-8 encoding
    """
    
    # Count of remaining continuation bytes
    remaining_bytes = 0
    
    for byte in data:
        # Check if the current byte is a continuation byte
        if remaining_bytes > 0:
            # Check if the two most significant bits are '10'
            if (byte & 0b11000000) != 0b10000000:
                return False
            remaining_bytes -= 1
        else:
            # Count the number of leading 1s to determine the character length
            mask = 0b10000000
            while (byte & mask) and mask > 0b00100000:
                remaining_bytes += 1
                mask >>= 1

            # Handle the case where the character length is 1
            if remaining_bytes == 1 or remaining_bytes > 4:
                return False

    # Check if there are any remaining continuation bytes
    return remaining_bytes == 0
