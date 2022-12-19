#!/usr/bin/python3

# Author: Brian Sakwa

def safe_print_division(a, b):
    """
    Divides 2 integers and prints the results

    """
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)
