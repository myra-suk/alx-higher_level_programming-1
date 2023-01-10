#!/usr/bin/python3

# Author: Brian Sakwa
"""Defines a function that returns an object represented by a JSON string"""
import json


def from_json_string(my_str):
    """ Returns the JSON representation
    Args:
        my_str: The object to obtain the JSON(JavaScript Object Notation)
    Return:
        The obj
    """
    return json.loads(my_str)
