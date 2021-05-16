import json

class Recipes:
    """
    This class contains all the recipes we are provided
    """

    def __init__(self):
        self.recipes_data = {}
        self.recipes_data = self.load_recipes()

    def load_recipes(self):
        with open('json/recipes.json') as f:
            self.recipes_data = json.load(f)
        return self.recipes_data

    def get_recipe(self, recipe_name):
        return self.recipes_data[recipe_name]

    def get_recipe_name(self, produces):
        found = ""
        for name,recipe in self.recipes_data.items():
            for product in recipe['produces'].keys():
                if produces in product:
                    found = name
                    break
        return found

    def print_recipe(self, recipe_name):
        print(self.recipes_data[recipe_name])

    def get_consumes(self, recipe_name):
        return self.recipes_data[recipe_name]["consumes"]

    def get_time(self, recipe_name):
        return self.recipes_data[recipe_name]["time"]

    def get_produces(self, recipe_name):
        return self.recipes_data[recipe_name]["produces"]

    def is_subcomponent(self, component_name):
        flag = False
        recipe_name = self.get_recipe_name(component_name)
        if(recipe_name != ""):
            flag = True
        return flag
