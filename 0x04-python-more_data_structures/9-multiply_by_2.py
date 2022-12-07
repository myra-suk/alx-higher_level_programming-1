#!/usr/bin/python3

# Author: Brian Sakwa

def multiply_by_2(a_dictionary):
    """
    Return a new dictionary with the values multiplied by two

    """
    return ({i: a_dictionary[i] * 2 for i in a_dictionary})
