#!/usr/bin/python3

# Author: Brian Sakwa

def best_score(a_dictionary):
    """
    Returns the key with the biggest value

    """
    if a_dictionary:
        return (max(a_dictionary, key=a_dictionary.get))
    else:
        return (None)
