#!/usr/bin/python3

"""
Module Rectangle
"""


class Rectangle(BaseGeometry):
    """class that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Instantiation with width and height"""
        self.integer_validator('width', width)
        self.integer_validator('height', height)
