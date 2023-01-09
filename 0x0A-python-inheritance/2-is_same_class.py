#!/usr/bin/python3

# Author: Brian Sakwa

"""Defines a class and specifies whether a given class is its instance"""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance

    Args:
        obj: The object to check
        a_class: The class to match the type of obj to
    Return:
        True if its the exact instance
        Otherwise- False
    """
    if type(obj) == a_class:
        return True
    return False
