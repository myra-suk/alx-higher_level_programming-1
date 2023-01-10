#!/usr/bin/python3

# Author: Brian Sakwa
"""Defines a function that creates an object file from a JSON file"""
import json


def load_from_json_file(filename):
    "Creates an object file from a json file"""
    with open(filename) as my_file:
        return json.load(my_file)
