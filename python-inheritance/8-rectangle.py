#!/usr/bin/python3

"""
Module Rectangle
"""

class Rectangle(BaseGeometry):
    """class that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Initialize with width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
