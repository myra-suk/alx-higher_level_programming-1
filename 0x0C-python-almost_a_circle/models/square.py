#!/usr/bin/python3

# Author: Brian Sakwa
"""Defines a class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a class square"""
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize a new instance

        Args:
            size (int): The size of the new square
            x (int): The x coordinate of the new square
            y (int): The y coordinate of the new square
            id (int): The identity of the new square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Validates and sets the width of the Square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
