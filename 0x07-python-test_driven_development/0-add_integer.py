#!/usr/bin/python3

# Author: Brian Sakwa

"""Defines an integer addition function."""


def add_integer(a, b=98):
    """
    Return addition of a and b.

    Raises:
        TypeError: if both a and b are non integers and non float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
