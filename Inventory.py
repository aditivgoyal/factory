import json

class Inventory:
    """
    This contains all the details about the inventory we are provided
    """

    def __init__(self):
        self.inventory_list = {}
        self.inventory_list = self.load_inventory()

    def load_inventory(self):
        with open('json/inventory.json') as f:
            self.inventory_list = json.load(f)
        return self.inventory_list

    def print_inventory(self):
        print ("\nINVENTORY: \n")
        for item, count in self.inventory_list.items():
            print("\t* " + item + ": "+str(count))

    def dump_inventory(self):
        with open('json/output.json','w') as outfile:
            json.dump(self.inventory_list, outfile, indent=4)

    def add_item(self, item, qty):
        if(item in self.inventory_list.keys()):
            self.inventory_list[item] += qty
        else:
            self.inventory_list[item] = qty

    def remove_item(self, item,qty):
        if(item in self.inventory_list.keys()):
            self.inventory_list[item] -= qty
            return True
        else:
            return False

    def is_item_available(self, item):
        if (item in self.inventory_list.keys()):
            return True
        else:
            return False

    def get_product_qty(self, recipe_name):
        return list(self.get_produces(recipe_name).values())[0]

    def check_item(self, item,qty):
        return (item in self.inventory_list.keys() and self.inventory_list[item] >= qty)
