#!/usr/bin/python3

# Author : Brian Sakwa

def max_integer(my_list=[]):
    """
    Returns the largest integer in the list

    """
    if len(my_list) == 0:
        return None

    max = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > max:
            max = my_list[i]

    return (max)
