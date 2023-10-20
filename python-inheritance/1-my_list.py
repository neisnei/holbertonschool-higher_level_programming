#!/usr/bin/python3
"""
print sorted module
"""


class MyList(list):
    """
    MyList class
    """

    def print_sorted(self):
        """
        Prints list, but sorted (ascending sort)
        """
        print(sorted(self))
