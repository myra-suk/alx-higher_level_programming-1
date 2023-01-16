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
        self.size = size

    @property
    def size(self):
        """ Validates and sets the width of the Square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Updates and assigns attributes to the square class"""
        attr_list = ["id", "size", "x", "y"]
        if args and len(args) != 0:
            j = 0
            for arg in args:
                if j == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif j == 1:
                    self.size = arg
                elif j == 2:
                    self.x = arg
                elif j == 3:
                    self.y = arg
                j += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def __str__(self):
        """Return the string representation of the square"""
        sqr_str = "[Square] ({}) {}/{} - {}".format(
                str(self.id), str(self.x), str(self.y), str(self.width))
        return (sqr_str)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        sqr_dict = {}
        sqr_dict["id"] = self.id
        sqr_dict["size"] = self.size
        sqr_dict["x"] = self.x
        sqr_dict["y"] = self.y
        return sqr_dict
