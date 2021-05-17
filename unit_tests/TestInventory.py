import unittest
import json
import sys
import os
from lib.Inventory import Inventory

inventory_file = 'json/inventory.json'
out_inventory_file = ''
expected_inventory_list = {
    "iron_plate": 40,
    "iron_gear": 5,
    "copper_plate": 20,
    "copper_cable": 10,
    "lubricant": 100
}

class TestInventory(unittest.TestCase):

    def setUp(self):
        self.inventory = Inventory(inventory_file, out_inventory_file, False)

    def test_load_inventory(self):
        self.assertTrue(inventory_file.endswith(".json") or inventory_file.endswith(".JSON"))
        self.assertTrue(os.path.isfile(inventory_file))
        self.assertEqual(self.inventory.load_inventory(inventory_file), expected_inventory_list)

    def test_add_item(self):
        self.assertFalse(self.inventory.add_item("iron_abc", "abc"))
        self.assertTrue(self.inventory.add_item("iron_gear", 1))
        self.assertEqual(self.inventory.get_item_quantity("iron_gear"), 6)

    def test_remove_item(self):
        self.assertTrue(self.inventory.remove_item("iron_gear", 1))
        self.assertFalse(self.inventory.remove_item("iron_gear", 10))
        self.assertFalse(self.inventory.remove_item("iron_iron", 1))
        self.assertEqual(self.inventory.get_item_quantity("iron_gear"), 4)

    def test_set_item_quantity(self):
        self.assertTrue(self.inventory.set_item_quantity("iron_gear", 1))
        self.assertTrue(self.inventory.set_item_quantity("iron_gear", 10))
        self.assertFalse(self.inventory.set_item_quantity("iron_abc", "abc"))
        self.assertEqual(self.inventory.get_item_quantity("iron_gear"), 10)

    def test_get_item_quantity(self):
        self.assertEqual(self.inventory.get_item_quantity("iron_gear"), 5)
        self.assertEqual(self.inventory.get_item_quantity("iron_abc"), 0)

    def test_check_item(self):
        self.assertTrue(self.inventory.check_item("iron_gear", 1))
        self.assertFalse(self.inventory.check_item("iron_gear", 10))
        self.assertFalse(self.inventory.check_item("iron_iron", 1))
