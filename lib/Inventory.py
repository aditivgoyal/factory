import json
import os

class Inventory:
    """
    This contains all the details about the inventory we are provided
    """

    # Constructor
    def __init__(self, inventory_file, out_inventory_file, enable_display = True):
        self.__display = isinstance(enable_display, bool) and enable_display
        self.__inventory_list = {}
        self.__inventory_list = self.load_inventory(inventory_file)
        self.__out_inventory_file = ""
        if (isinstance(out_inventory_file, str) and (out_inventory_file.endswith(".json") or out_inventory_file.endswith(".JSON"))):
            self.__out_inventory_file = out_inventory_file

    # Deleting (Calling destructor)
    def __del__(self):
        self.__print_inventory()
        if (isinstance(self.__out_inventory_file, str) and (self.__out_inventory_file.endswith(".json") or self.__out_inventory_file.endswith(".JSON"))):
            with open(self.__out_inventory_file,'w') as outfile:
                json.dump(self.__inventory_list, outfile, indent=4)

    def __print_inventory(self):
        if (not self.__display):
            return
        print ("\nINVENTORY: \n")
        for item, count in self.get_inventory().items():
            print(" * " + item + ": "+str(count))
        print("")

    def get_inventory(self):
        return self.__inventory_list

    def load_inventory(self, inventory_file):
        self.__inventory_list = {}
        if (isinstance(inventory_file, str) and (inventory_file.endswith(".json") or inventory_file.endswith(".JSON")) and os.path.isfile(inventory_file)):
            with open(inventory_file) as f:
                self.__inventory_list = json.load(f)
        self.__print_inventory()
        return self.get_inventory()

    def add_item(self, item, qty):
        if (isinstance(item, str) and isinstance(qty, int) and qty >= 0):
            if(item in self.get_items_list()):
                self.__inventory_list[item] += qty
            else:
                self.__inventory_list[item] = qty
            return True
        return False

    def remove_item(self, item,qty):
        if(self.check_item(item, qty)):
            self.__inventory_list[item] -= qty
            return True
        return False

    def set_item_quantity(self, item, qty):
        if(isinstance(item, str) and isinstance(qty, int)):
            self.__inventory_list[item] = qty
            return True
        return False

    def get_item_quantity(self, item):
        if(isinstance(item, str) and item in self.get_items_list()):
            return self.__inventory_list[item]
        return 0

    def get_items_list(self):
        return self.__inventory_list.keys()

    def check_item(self, item, qty):
        return (isinstance(item, str) and isinstance(qty, int) and item in self.get_items_list() and self.get_item_quantity(item) >= qty)
