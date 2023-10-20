#!/usr/bin/python3
"""
is_same_class module
"""


def is_same_class(obj, a_class):
    """
    True object is exactly an instance of the specified class
    Or False
    """
    if type(obj) == a_class:
        return True
    else:
        return False
