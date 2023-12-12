#!/usr/bin/python3
from models.base_model import BaseModel

ins = BaseModel()
ins.save()

ins1 = BaseModel(**ins.to_dict())
print(ins)
print()
print()
print(ins1)
print(ins.id == ins1.id)
