#!/usr/bin/python3

# Author: Brian Sakwa
"""Defines a function thatt returns the JSON representation of a string"""
import json


def to_json_string(my_obj):
    """ Returns the JSON representation

    Args:
        my_obj: The object to obtain the JSON(JavaScript Object Notation)
    Return:
        The JSON representation
    """
    return json.dumps(my_obj)
