#!/usr/bin/python3
"""Function that returns an object"""


def from_json_string(my_str):
    """Function that returns an object
    represented by a JSON string"""
    import json
    return json.loads(my_str)
