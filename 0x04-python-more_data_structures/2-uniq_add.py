#!/usr/bin/python3

# Author: Brian Sakwa

def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list

    """
    res = 0
    for x in set(my_list):
        res += x
    return (res)
