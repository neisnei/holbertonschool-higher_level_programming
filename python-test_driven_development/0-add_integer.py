#!/usr/bin/python3
"""
    This module have function that add 2 intergers.
    First number be a and second number passed be b.
    Returning the addition of both number.
"""


def add_integer(a, b=98):
    """
        Function that adds 2 intergers.
        Check if a and b are intergers or floats.
        If not a error will be raised.
        Otherwise float will be casted to interger in order to
        recreate add both.
    """
 if a is None or (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return imt(a) + int(b)
