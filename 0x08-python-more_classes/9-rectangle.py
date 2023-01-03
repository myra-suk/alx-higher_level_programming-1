#!/usr/bin/python3

# Author: Brian Sakwa

""" Real definition of a rectangle"""


class Rectangle:
    """ Define the class Rectangle
    Attributes:
        number_of_instances (int) : The number of Rectangle instances
        print_symbol (any): The symbol used for string representation
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initialize a new Rectangle.
        Args:
            height (int): The height of the Rectangle
            Width (int):  The width of the Rectangle
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Get/set the height of the Rectangle."""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Return the area of the Rectangle"""
        return (self.__width * self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Return the biggest rectangle based on the area
        Args:
            rect_1: The first instance of rectangle
            rect_2: The second instance of rectangle
        Raises:
            TypeError: if none of the two instances are rectangles
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """ Returns a new rectangles instance

        Args:
            size (int): The width and height of the new instance
        """
        return (cls(size, size))

    def perimeter(self):
        """ Return the Perimeter of the Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """ Return a string character representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Print a message when an Rectangle is deleted."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
