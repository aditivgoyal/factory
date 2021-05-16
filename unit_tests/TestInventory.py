import unittest
import json
from Inventory import Inventory

base_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

class TestInventory(unittest.TestCase, Inventory):

    # def setUp(self):
    #     self.inventory_list = Inventory()

    @patch("builtins.open", new_callback=mock_open,
        read_data=json.dumps(
                {
                    "iron_plate": 40,
                    "iron_gear": 5,
                    "copper_plate": 20,
                    "copper_cable": 10,
                    "lubricant": 100
                }))
    def test_load_inventory(self):
        expected_output = {
                "iron_plate": 40,
                "iron_gear": 5,
                "copper_plate": 20,
                "copper_cable": 10,
                "lubricant": 100
            }
        actual_output = load_inventory()

        # Assert
        self.assertEqual(expected_output,actual_output)
        