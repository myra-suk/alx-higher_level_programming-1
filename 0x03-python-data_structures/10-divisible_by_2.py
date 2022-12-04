#!/usr/bin/python3

# Author: Brian Sakwa

def divisible_by_2(my_list=[]):
    """
    Finds all multiples of 2 in a list

    """
    multiples = []
    multiples += my_list
    for i in range(len(my_list)):
        if (my_list[i] % 2) == 0:
            multiples[i] = True
        else:
            multiples[i] = False

    return (multiples)
