#!/usr/bin/python3

# Author: Brian Sakwa
"""Defines a python class to JSON function"""


def class_to_json(obj):
    """Return the dictionary representation of a simple data structure"""
    return obj.__dict__
