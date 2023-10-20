#!/usr/bin/python3
"""
Module inherits.
"""

def inherits_from(obj, a_class):
    """
    True or False  if the object is an instance of a class
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
