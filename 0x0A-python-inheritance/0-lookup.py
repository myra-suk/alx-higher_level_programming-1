#!/usr/bin/python3

# Author: Brian Sakwa
"""Returns the list of available attributes and methods of an object"""


def lookup(obj):
    """Return a list of an objects available attributes"""
    return (dir(obj))
