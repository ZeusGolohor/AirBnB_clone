#!/usr/bin/python3
"""
This module used to manager Place class instances.
"""
from models.base_model import BaseModel
from models import storage
from datetime import datetime

class Place(BaseModel):
    """
    This class is used to manage the Place class
    instances.
    """
    def __init__(self, *args, **kwagrs):
        """
        This method is called wherever this class gets
        instanciated.
        """
        if ("id" not in kwagrs.keys()):
            super().__init__()
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = int(0)
        self.number_bathrooms = int(0)
        self.max_guest = int(0)
        self.price_by_night = int(0)
        self.latitude = float(0.0)
        self.longitude = float(0.0)
        self.amenity_ids = []
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
