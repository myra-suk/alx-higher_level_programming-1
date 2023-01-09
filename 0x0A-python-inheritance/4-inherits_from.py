#!/usr/bin/python3

# Author: Brian Sakwa
"""Defines if an object is an instance inherited directly or indirectly"""


def inherits_from(obj, a_class):
    """Defines if an object is inherited directly or indirectly

    Args:
        obj: The object to be checked
        a_class: The class to match the type of obj to.
    Return:
        if inherited directly or indirectly True
        Otherwise - False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
