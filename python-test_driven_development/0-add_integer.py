#!/usr/bin/python3
"""
    This module have function that add 2 intergers.
    First number be a and second number passed be b.
    Returning the addition of both number.
"""


def add_integer(a, b=98):
 """
        Function adds 2 intergers.
        Check if a and b are intergers or floats.
        If not a error will be raised.
        Otherwise float will be casted to interger in order to
        recreate add both.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
