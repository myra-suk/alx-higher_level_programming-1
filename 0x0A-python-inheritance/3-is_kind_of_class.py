#!/usr/bin/python3

# Author: Brian Sakwa
"""Defines if the object is same class or inherited from"""


def is_kind_of_class(obj, a_class):
    """
    Defines whether an object is an instance of or an instance
    of a class that inherited from that specific class

    Args:
        obj: The object to be checked
        a_class: The class to match the type of obj to
    Return:
        True if is instance or inherited instance
        Otherwise - false
    """
    if isinstance(obj, a_class):
        return True
    return False
