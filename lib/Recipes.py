import json
import os

class Recipes:
    """
    This class contains all the recipes we are provided
    """

    def __init__(self, recipe_file):
        self.__recipes_data = {}
        self.__recipes_data = self.load_recipes(recipe_file)

    def load_recipes(self, recipe_file):
        self.__recipes_data = {}
        if (isinstance(recipe_file, str) and (recipe_file.endswith(".json") or
            recipe_file.endswith(".JSON")) and os.path.isfile(recipe_file)):
            with open(recipe_file) as f:
                self.__recipes_data = json.load(f)
        return self.__recipes_data

    def get_recipe_name(self, produce):
        if(isinstance(produce, str)):
            for name,recipe in self.__recipes_data.items():
                if produce in recipe['produces'].keys():
                    return name
        return ""

    def get_consumes(self, recipe_name):
        if (isinstance(recipe_name, str) and recipe_name in self.__recipes_data.keys() and
        "consumes" in self.__recipes_data[recipe_name].keys()):
            return self.__recipes_data[recipe_name]["consumes"].items()
        return {}

    def get_produce_qty(self, recipe_name):
        if(isinstance(recipe_name, str) and recipe_name in self.__recipes_data.keys() and
        "produces" in self.__recipes_data[recipe_name].keys()):
            return list(self.__recipes_data[recipe_name]["produces"].values())[0]
        return 0

    def get_time(self, recipe_name):
        if(isinstance(recipe_name, str) and recipe_name in self.__recipes_data.keys() and
        "time" in self.__recipes_data[recipe_name].keys()):
            return self.__recipes_data[recipe_name]["time"]
        return 0
