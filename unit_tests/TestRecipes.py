import unittest
import json
import sys
import os
from lib.Recipes import Recipes

recipe_file = 'json/recipes.json'
expected_recipe_list = {
    "recipe_gear": {
        "title": "Gear",
        "time": 0.5,
        "consumes": {
            "iron_plate": 2
        },
        "produces": {
            "iron_gear": 1
        }
    },
    "recipe_pipe": {
        "title": "Pipe",
        "time": 0.5,
        "consumes": {
            "iron_plate": 1
        },
        "produces": {
            "pipe": 1
        }
    },
    "recipe_cables": {
        "title": "Copper Cable (2x)",
        "time": 0.5,
        "consumes": {
            "copper_plate": 1
        },
        "produces": {
            "copper_cable": 2
        }
    },
    "recipe_steel": {
        "title": "Steel Plate",
        "time": 16.0,
        "consumes": {
            "iron_plate": 5
        },
        "produces": {
            "steel_plate": 1
        }
    },
    "recipe_circuit": {
        "title": "Electric Circuit",
        "time": 1.5,
        "consumes": {
            "iron_plate": 1,
            "copper_cable": 3
        },
        "produces": {
            "electric_circuit": 1
        }
    },
    "recipe_engine_block": {
        "title": "Engine Block",
        "time": 10.0,
        "consumes": {
            "steel_plate": 1,
            "iron_gear": 1,
            "pipe": 2
        },
        "produces": {
            "engine_block": 1
        }
    },
    "recipe_elec_engine": {
        "title": "Electric Engine",
        "time": 10.0,
        "consumes": {
            "electric_circuit": 2,
            "engine_block": 1,
            "lubricant": 15
        },
        "produces": {
            "electric_engine": 1
        }
    }
}

class TestRecipes(unittest.TestCase):

    def setUp(self):
        self.recipes = Recipes(recipe_file)


    def test_load_recipes(self):
        self.assertTrue(recipe_file.endswith(".json") or recipe_file.endswith(".JSON"))
        self.assertTrue(os.path.isfile(recipe_file))
        self.assertEqual(self.recipes.load_recipes(recipe_file), expected_recipe_list)

    def test_get_recipe_name(self):
        self.assertEqual(self.recipes.get_recipe_name("electric_engine"), "recipe_elec_engine")
        self.assertEqual(self.recipes.get_recipe_name("lubricant"), "")

    def test_get_consumes(self):
        self.assertEqual(self.recipes.get_consumes("recipe_elec_engine"), expected_recipe_list["recipe_elec_engine"]["consumes"].items())
        self.assertEqual(self.recipes.get_consumes("recipe_lubricant"), {})

    def test_get_produce_qty(self):
        self.assertEqual(self.recipes.get_produce_qty("recipe_elec_engine"), 1)
        self.assertEqual(self.recipes.get_produce_qty("recipe_cables"), 2)
        self.assertEqual(self.recipes.get_produce_qty("recipe_lubricant"), 0)

    def test_get_time(self):
        self.assertEqual(self.recipes.get_time("recipe_elec_engine"), 10.0)
        self.assertEqual(self.recipes.get_time("recipe_cables"), 0.5)
        self.assertEqual(self.recipes.get_time("recipe_lubricant"), 0)
