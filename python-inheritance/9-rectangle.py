#!/usr/bin/python3

"""Full rectangle module."""

class Rectangle(BaseGeometry):
    """Class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize Rectangle with width and height attributes"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return the string representation of the Rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
