#!/usr/bin/python3

# Author: Brian Sakwa

def weight_average(my_list=[]):
    """
    Returns the weighted average of all integers tuple

    """
    count = 0
    sumthemall = 0
    if my_list:
        for (a, b) in my_list:
            sumthemall += (a * b)
            count += b
        av = sumthemall / count
        return (av)
    else:
        return (0)
