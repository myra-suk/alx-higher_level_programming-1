#!/usr/bin/python3

# Author: Brian Sakwa

def safe_print_integer(value):
    """
    Prints an Integer in the format "{:d}".format().

    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
