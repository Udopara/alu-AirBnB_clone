#!/usr/bin/python3
"""
Contains the BaseModel class
"""
from datetime import datetime
import uuid

class BaseModel:
    def __init__(self):
        super().__setattr__("id", str(uuid.uuid4()))
        now = datetime.now()
        super().__setattr__("created_at", now)
        super().__setattr__("updated_at", now)
        

    def __str__(self):
        return f"[BaseModel] ({self.id}) {self.__dict__}"
    
    def __setattr__(self, name, value):
        # Always set the attribute
        super().__setattr__(name, value)
        # Update updated_at (but not during init of id/created_at/updated_at)
        if name not in {"id", "created_at", "updated_at"}:
            self.save()

    def save(self):
        super().__setattr__("updated_at", datetime.now())

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict






if __name__ == "__main__":
    test_model = BaseModel()
    print(test_model.to_dict())