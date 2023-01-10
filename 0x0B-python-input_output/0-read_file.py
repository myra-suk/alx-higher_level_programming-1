#!/usr/bin/python3

# Author: Brian Sakwa
""" Defines a function that reads a file"""


def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as my_file:
        print(my_file.read(), end="")
