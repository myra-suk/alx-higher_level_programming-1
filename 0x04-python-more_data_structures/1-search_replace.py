#!/usr/bin/python3

# Author: Brian Sakwa

def search_replace(my_list, search, replace):
    """
    Replaces all occurences of an element by another in a list

    """
    new_list = my_list[:]
    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace
    return (new_list)
