#!/usr/bin/python3
"""
Contains the FileStorage class
"""
from models import BaseModel
import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}


    def all(self):
        """Return the objects in storage"""
        return self.__objects
    
    def new(self, obj):
        """Add a new object instance to __objects"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj


    def save(self):
        """Serialize __objects to the JSON file"""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as f:
            json.dump(obj_dict, f)


    def reload(self):
        """Deserialize JSON file to __objects if file exists"""
        try:
            with open(self.__file_path, "r") as f:
                # Load JSON string from file
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name = value.get("__class__")
                    if class_name == "BaseModel":
                        self.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            # Do nothing if file does not exist
            pass
