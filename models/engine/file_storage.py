#!/usr/bin/pytyhon3
"""
This module recreate a BaseModel from another
one by using a dictionary representation.
"""
import json


class FileStorage():
    """
    A class that recreates a BaseModel from
    another one by using a dictionary representation.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        A method to return the dictionary __objects.
        """
        """
        if self.__objects is None:
            return {}
        from models.base_model import BaseModel
        objs = {}
        for key, value in self.__objects.items():
            objs[
                 "{}.{}".format(
                                self.__class__.__name__,
                                value["id"])
                ] = BaseModel(**value)
        return (objs)
        """
        from console import HBNBCommand
        console = HBNBCommand()
        objs = {}
        if (self.__objects):
            for key, value in self.__objects.items():
                if (value["__class__"] in console.dictOfClasses.keys()):
                    className = console.dictOfClasses[value["__class__"]]
                    instance = className(**value)
                    objs[
                          "{}.{}".format(
                                          value["__class__"],
                                          value["id"])
                         ] = instance
        return (objs)

    def new(self, obj):
        """
        A method thats sets in __objects the obj
        with key <obj class name>.id.
        """
        self.__objects[
                        "{}.{}".format(
                                        str(obj.__class__.__name__),
                                        str(obj.id))
                        ] = obj.to_dict()

    def save(self):
        """
        A method that serializes __objects to the
        JSON file (path: __file_path).
        """
        with open(self.__file_path, "w", encoding="utf-8") as json_file:
            res = json_file.write(json.dumps(self.__objects))

    def reload(self):
        """
        A method that deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise,
        do nothing. If the file doesn’t exist, no exception should
        be raised).
        """
        try:
            with open(self.__file_path, 'r') as objs:
                objs_dict = json.load(objs)
                self.__objects.update(objs_dict)
        except FileNotFoundError:
            pass
