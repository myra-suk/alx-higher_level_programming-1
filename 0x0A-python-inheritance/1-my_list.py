#!/usr/bin/python3

# Author: Brian Sakwa
"""Defines a class Mylist that inherits from List"""


class MyList(list):
    """ Sorts printing for the built in class list"""

    def print_sorted(self):
        """Prints a list in sorted order"""
        print(sorted(self))
