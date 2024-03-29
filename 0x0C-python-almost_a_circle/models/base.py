#!/usr/bin/python3
""" Python - Almost a circlee """
import json
import csv
import os
import turtle


class Base:
    """ Class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ class constractor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries and list_dictionaries != []:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves the JSON string representation of list_objs in a file"""
        filename = cls.__name__ + ".json"
        dictionary = []

        if list_objs and list_objs != []:
            for i in range(len(list_objs)):
                dictionary.append(list_objs[i].to_dictionary())

        to_json = cls.to_json_string(dictionary)

        with open(filename, 'w') as f:
            f.write(to_json)

    @staticmethod
    def from_json_string(json_string):
        """that returns the list of the JSON string
        representation json_string"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already
        set"""

        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            dummy_instance = cls()

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        filename = cls.__name__ + ".json"

        if not os.path.exists(filename):
            return []

        with open(filename, 'r') as f:
            json_str = f.read()

        dictionaries = cls.from_json_string(json_str)
        instances_list = []

        for i in range(len(dictionaries)):
            instances_list.append(cls.create(**dictionaries[i]))

        return instances_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Serializes objects to a CSV file """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)

            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            elif cls.__name__ == "Square":
                fieldnames = ["id", "size", "x", "y"]
            else:
                fieldnames = []

            writer.writerow(fieldnames)

            for obj in list_objs:
                writer.writerow(obj.to_dictionary().values())

    @classmethod
    def load_from_file_csv(cls):
        """ Deserializes objects from a CSV file """
        filename = cls.__name__ + ".csv"
        if not os.path.exists(filename):
            return []

        instances_list = []

        with open(filename, 'r') as f:
            reader = csv.DictReader(f)

            for row in reader:
                dictionary = {k: int(v) for k, v in row.items()}
                instances_list.append(cls.create(**dictionary))

        return instances_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws Rectangles and squares"""
        screen = turtle.Screen()
        screen.setup(width=800, height=600)
        screen.title("Rectangles and Squares")

        t = turtle.Turtle()

        for rect in list_rectangles:
            t.penup()
            t.goto(rect.x, rect.y)
            t.pendown()
            t.color("blue")
            for _ in range(2):
                t.forward(rect.width)
                t.left(90)
                t.forward(rect.height)
                t.left(90)

        for square in list_squares:
            t.penup()
            t.goto(square.x, square.y)
            t.pendown()
            t.color("red")
            for _ in range(4):
                t.forward(square.size)
                t.left(90)

        screen.mainloop()
