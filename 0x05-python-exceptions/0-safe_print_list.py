#!/usr/bin/python3

# Author: Brian Sakwa

def safe_print_list(my_list=[], x=0):
    """
    Prints x elements of a list

    """
    lst = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            lst += 1
        except IndexError:
            break
    print("")
    return (lst)
