#!/usr/bin/python3

# Author: Brian Sakwa
""" Defines a class Base"""


class Base:
    """Defines a base model

    Attribute:
        __nb_objects (int): The number of instantiated bases
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Instantiates a new Base

        Args:
            id (int): The id of the new base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
