#!/usr/bin/python3
"""
This module used to manager State class instances.
"""
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class State(BaseModel):
    """
    This class is used to manage the State class
    instances.
    """
    def __init__(self, *args, **kwagrs):
        """
        This method is called wherever this class gets
        instanciated.
        """
        if ("id" not in kwagrs.keys()):
            super().__init__()
        name = ""
        for key, value in kwagrs.items():
            if key != "__class__":
                if (key == "created_at"):
                    self.created_at = datetime.fromisoformat(value)
                elif (key == "updated_at"):
                    self.updated_at = datetime.fromisoformat(value)
                else:
                    setattr(self, key, value)
        if ("id" not in kwagrs.keys()):
            storage.new(self)
