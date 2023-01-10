#!/usr/bin/python3

# Author: Brian Sakwa
""" Defines a function that appends a string at the end ofa text file"""


def append_write(filename="", text=""):
    """ Appends a string

    Args:
        filename: The name of the file to append the string to
        text: The string to append
    Return:
        The number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as my_file:
        return my_file.write(text)
