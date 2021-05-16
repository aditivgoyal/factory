import unittest
import json
import sys
import os
from unittest.mock import patch, mock_open

from lib.Builder import Builder

recipe_file = "json/recipes.json"
inventory_file  = "json/inventory.json"
output_file = "json/output.json"
expected_output = {
    "iron_plate": 1,
    "iron_gear": 1,
    "copper_plate": 8,
    "copper_cable": 1,
    "lubricant": 40,
    "electric_circuit": 3,
    "steel_plate": 0,
    "pipe": 0,
    "engine_block": 0,
    "electric_engine": 4
}

expected_output2 = {
    "iron_plate": 4,
    "iron_gear": 1,
    "copper_plate": 13,
    "copper_cable": 0,
    "lubricant": 40,
    "electric_circuit": 0,
    "steel_plate": 0,
    "pipe": 0,
    "engine_block": 0,
    "electric_engine": 4
}

class TestRecipes(unittest.TestCase):

    def setUp(self):
        self.builder = Builder(recipe_file, inventory_file, output_file, False)

    def test_manufacture(self):
        self.assertEqual(self.builder.manufacture([{"electric_engine": 3},{"electric_circuit": 5},{"electric_engine": 3}]), expected_output)
        #self.builder.load_inventory(inventory_file)
        #self.assertEqual(self.builder.manufacture([{"electric_engine": 5}]), expected_output2)
