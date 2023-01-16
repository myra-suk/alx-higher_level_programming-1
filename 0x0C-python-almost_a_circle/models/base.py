#!/usr/bin/python3

# Author: Brian Sakwa
""" Defines a class Base"""
import json


class Base:
    """Defines a base model

    Attribute:
        __nb_objects (int): The number of instantiated bases
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Instantiates a new Base

        Args:
            id (int): The id of the new base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON rep of list dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of a list_objs

        Args:
            list_objs (list): A list of inherited base instances
        """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        list_dictionaries = []
        for instance in list_objs:
            list_dictionaries.append(instance.to_dictionary())
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the Json String representation"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)
