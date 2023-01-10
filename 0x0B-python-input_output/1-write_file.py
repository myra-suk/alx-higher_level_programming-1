#!/usr/bin/python3

# Author: Brian Sakwa
""" Defines a function that reads a file"""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns the number
    of characters.

    Args:
        filename: The name of the file to write to
        text: The string to write
    Return:
        The number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as my_file:
        return my_file.write(text)
