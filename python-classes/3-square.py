#!/usr/bin/python3
"""Module contains square class"""


class Square:
    """Class defines a square"""

    def __init__(self, size=0):
        """initialize the data"""
        if not isinstance(size, int):
            raise TypeError("size must be an int")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """generate the area"""
        return self.__size ** 2
