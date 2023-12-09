#!/usr/bin/python3
from models.user import User
from models import storage

i = storage.all()
print(i)
