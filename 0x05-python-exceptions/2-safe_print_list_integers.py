#!/usr/bin/python3

# Author: Brian Sakwa

def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first X elements of a list and only integers

    """
    lst = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            lst += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (lst)
