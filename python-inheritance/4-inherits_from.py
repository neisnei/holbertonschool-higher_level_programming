#!/usr/bin/python3

"""
Module inherits.
"""

def inherits_from(obj, a_class):
    """function returns True or False.
    If the object an instance class that inherited the specified class"""
    return issubclass(type(obj), a_class) and type(obj)
