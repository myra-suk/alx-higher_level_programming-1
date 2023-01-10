#!/usr/bin/python3

# Author: Brian Sakwa
"""Defines a function that writes an object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object using JSON representation"""
    with open(filename, 'w') as my_file:
        json.dump(my_obj, my_file)
