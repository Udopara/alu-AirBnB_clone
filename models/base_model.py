#!/usr/bin/python3
"""
Contains the BaseModel class
"""
from datetime import datetime
import uuid

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = self.created_at
        

    def __str__(self):
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        """Simulate saving to DB/storage by updating timestamp"""
        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        return obj_dict






if __name__ == "__main__":
    test_model = BaseModel()
    print(test_model.to_dict())