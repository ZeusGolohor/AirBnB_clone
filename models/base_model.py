#!/usr/bin/python3
"""
This module is defines all common attributes/methods for other classes.
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """
    This class defines all common attributes/methods
    for other classes.
    """
    def __init__(self, *args, **kwargs):
        """
        A method called whenever this class gets instantiated.
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at":
                        self.created_at = datetime.fromisoformat(value)
                    elif key == "updated_at":
                        self.updated_at = datetime.fromisoformat(value)
                    else:
                        setattr(self, key, value)

    def __str__(self):
        """
        A method that prints the string representation of
        the class.
        """
        obj = {}
        for key, value in self.__dict__.items():
            if (key not in ["created_at", "updated_at"]):
                try:
                    value_len = len(value)
                except TypeError:
                    obj[key] = value
                else:
                    if (len(value) > 0):
                        obj[key] = value
            else:
                obj[key] = value
        res = "[{}] ({}) {}".format(self.__class__.__name__,
                                    self.id,
                                    obj
                                    )
        return (res)

    def save(self):
        """
        A method that updates the updated_at public instance
        variable to the current time.
        """
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        A dictionary containing all keys/values of
        __dict__ of the instance.
        """
        """
        if isinstance(self.__dict__["created_at"], datetime):
            self.__dict__["created_at"] = self.created_at.isoformat()
        if isinstance(self.__dict__["updated_at"], datetime):
            self.__dict__["updated_at"] = self.updated_at.isoformat()
        self.__dict__["__class__"] = self.__class__.__name__
        """
        obj = {}
        for key, value in self.__dict__.items():
            if key == "created_at":
                obj["created_at"] = datetime.isoformat(value)
            elif key == "updated_at":
                obj["updated_at"] = datetime.isoformat(value)
            else:
                try:
                    value_len = len(value)
                except TypeError as e:
                    obj[key] = value
                else:
                    if (value_len > 0):
                        obj[key] = value
            obj["__class__"] = self.__class__.__name__
        return (obj)
