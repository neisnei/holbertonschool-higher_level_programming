#!/usr/bin/python3

"""
Module Read file.
"""


def read_file(filename=""):
    """function reads a text file"""
    with open(filename, encoding='utf-8') as file:
        """use with statement"""
        print(file.read())
