#!/usr/bin/python3

def multiple_returns(sentence):
    """
    Returns the length and the first letter of a string

    """
    for i in range(len(sentence)):
        if sentence == "":
            return (0, None)
        return (len(sentence), sentence[0])
