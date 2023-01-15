#!/usr/bin/python3

# Author: Brian Sakwa
""" Defines a class Rectangle that inherits from Base:"""
from models.base import Base


class Rectangle(Base):
    """ Represent a Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Defines attributes of a class Rectangle

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
            x (int): The x coordinate of the rectangle
            y (int): The y coordinate of the rectangle
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

        @property
        def width(self):
            """Validate and set the width of the rectangle"""
            return self.__width

        @width.setter
        def width(self, value):
            if type(value) != int:
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

        @property
        def height(self):
            """Validate and set the height of the rectangle"""
            return self.__height

        @height.setter
        def height(self, value):
            if type(value) != int:
                raise TypeError("height must be an integer")
            if value <= 0:
                raise ValueError("value must be > 0")
            self.__height = value
