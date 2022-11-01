#!/usr/bin/python3
"""
    Defines 'Base' class
"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class initialization"""
        if (id is not None):
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dict"""
        if (list_dictionaries is None or list_dictionaries == []):
            return ("[]")

        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the json string rep of list_objs to a file"""
        filename = cls.__name__ + ".json"
        filecontent = []

        if list_objs is not None:
            for item in list_objs:
                item = item.to_dictionary()
                json_rep = json.loads(cls.to_json_string(item))
                filecontent.append(json_rep)

        with open(filename, mode="w") as f:
            json.dump(filecontent, f)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of json string rep of json_string"""
        if (json_string is None or len(json_string) == 0):
            return []
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with already set attributes"""
        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == "Rectangle":
            r = Rectangle(7, 11)
        elif cls.__name__ == "Square":
            r = Square(5)
        r.update(**dictionary)
        return (r)

    @classmethod
    def load_from_file(cls):
        """Returns a list of all instances"""
        file_name = cls.__name__ + ".json"

        try:
            with open(file_name, encoding="UTF8") as f:
                content = cls.from_json_string(f.read())
        except IOError:
            return []

        instances = []

        for instance in content:
            tmp = cls.create(**instance)
            instances.append(tmp)

        return (instances)
