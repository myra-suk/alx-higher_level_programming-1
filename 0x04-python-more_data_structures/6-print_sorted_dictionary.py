#!/usr/bin/python3

# Author: Brian Sakwa

def print_sorted_dictionary(a_dictionary):
    """
    Prints a dictionary by ordered keys

    """
    [print("{}: {}".format(i, a_dictionary[i])) for i in sorted(a_dictionary)]
