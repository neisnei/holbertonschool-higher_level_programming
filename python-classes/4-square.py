class Square:
    """Class Square that defines a square by: (based on 3-square.py)"""

    def __init__(self, size=0):
        """Initialize Square with size attribute"""
        self.__size = size

    @property
    def size(self):
        """Getter method to retrieve the size of Square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size of Square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Public instance method that returns the current square area"""
        return self.__size ** 2
