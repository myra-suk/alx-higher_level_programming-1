#!/usr/bin/python3

# Author: Brian Sakwa
""" Defines a base geometry Class BaseGeometry."""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates a parameter as an integer.

        Args:
            name: The name of the parameter
            value: The value of the parameter
        Raises:
            TypeError: If the value is not an integer
            ValueError: if the value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
