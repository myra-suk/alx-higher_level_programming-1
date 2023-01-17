#!/usr/bin/python3

# Author: Brian Sakwa
""" Defines a class Base"""
import json
import csv


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
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of a list_objs

        Args:
            list_objs (list): A list of inherited base instances
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dictionaries = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the Json String representation"""
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all the attributes set"""
        if cls.__name__ == "Rectangle":
            instance = cls(1, 2, 0, 0)
        if cls.__name__ == "Square":
            instance = cls(1, 0, 0)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """ Returns the list of instances"""
        filename = cls.__name__ + ".json"
        results = []
        try:
            with open(filename, 'r') as f:
                for instance in cls.from_json_string(f.read()):
                    results.append(cls.create(**instance))
        except Exception as err:
            pass
        return (results)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ CSV serialization of a list object to file"""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ Returns a list of classes instantiated from a csv file"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r', newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dictionaries = csv.DictReader(csvfile,
                                                   fieldnames=fieldnames)
                list_dictionaries = [dict([k,
                                     int(v)] for k, v in d.items())
                                     for d in list_dictionaries]
                return [cls.create(**d) for d in list_dictionaries]
        except IOerror:
            return []
