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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Validate and get the width of the Rectangle."""
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
        """Validate and get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Validate and get the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Validate and get the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns the area value of a Rectangle"""
        return self.height * self.width

    def display(self):
        """ Print out the rectangle with the character #"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        """Return the print and str representation of the triangle"""
        str_rep = "[Rectangle] ({}) {}/{} - {}/{}".format(
                str(self.id), str(self.x), str(self.y),
                str(self.width), str(self.height))
        return (str_rep)

    def update(self, *args):
        """Assigns an argument to each attribute"""
        attr_list = ["id", "width", "height", "x", "y"]
        if args and len(args) != 0:
            for j in range(len(args)):
                if j == 0:
                    self.id = args[j]
                if j == 1:
                    self.width = args[j]
                if j == 2:
                    self.height = args[j]
                if j == 3:
                    self.x = args[j]
                if j == 4:
                    self.y = args[j]
