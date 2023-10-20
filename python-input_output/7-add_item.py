#!/usr/bin/python3
import json
import sys

from typing import List


def save_to_json_file(my_obj: List, filename: str):
    """Saves a Python object to a JSON file"""
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)


def load_from_json_file(filename: str) -> List:
    """Loads a Python object from a JSON file"""
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)


if __name__ == '__main__':
    # Set the filename to add_item.json
    filename = 'add_item.json'
    try:
        # Try to load the list from the file
        my_list = load_from_json_file(filename)
    except FileNotFoundError:
        # If the file doesn't exist, create an empty list
        my_list = []

    # Add the command line arguments to the list
    my_list.extend(sys.argv[1:])

    # Save the updated list to the file
    save_to_json_file(my_list, filename)
