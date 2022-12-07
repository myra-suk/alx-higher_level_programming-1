#!/usr/bin/python3

# Author: Brian Sakwa

def multiply_list_map(my_list=[], number=0):
    """
    Returns a list with all the values multiplied by a number

    """
    return (list(map(lambda i: i * number, my_list)))
