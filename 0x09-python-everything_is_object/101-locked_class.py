#!/usr/bin/python3

# Author: Brian Sakwa

""" Defines a locked class"""


class LockedClass:
    """
    Prevents a user from dynamically creating a new
    instance attribute except if the new instance is called first_name

    """
    __slots__ = ["first_name"]
