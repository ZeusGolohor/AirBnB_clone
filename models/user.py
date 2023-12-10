#!/usr/bin/python3
"""
This model is used to handle a User instance.
"""
from models.base_model import BaseModel
from models import storage
from datetime import datetime
import uuid


class User(BaseModel):
    """
    This class is used to handle a new User instance.
    """
    def __init__(self, *args, **kwagrs):
        """
        This method is called whenever this class is instantiated.
        """
        if ("id" not in kwagrs.keys()):
            super().__init__()
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
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
