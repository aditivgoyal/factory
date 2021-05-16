from lib.Inventory import Inventory
from lib.Recipes import Recipes
import math

class Builder(Inventory, Recipes):
    """
    This checks all the sub-components required for the product to be built
    and try to build it
    """
    def __init__(self, recipe_file, inventory_file, out_inventory_file, enable_display = True):
        Recipes.__init__(self, recipe_file)
        Inventory.__init__(self, inventory_file, out_inventory_file, enable_display)
        self.manufacture_time = 0

    def __add_item_to_dict(self,dictionary,itm,qty):
        if (isinstance(dictionary,dict) and isinstance(itm,str)):
            if(itm in dictionary.keys()):
                dictionary[itm] += qty
            else:
                dictionary[itm] = qty

    def __get_sub_component(self, desired_produce, produce_itm, produce_qty, spaces):
        # Check if item is available in the inventory
        if(self.check_item(produce_itm,produce_qty)):
            return 0

        # Get recipe name
        recipe_name = self.get_recipe_name(produce_itm)
        if (recipe_name == ""):
            return -1.0

        # Tab spaces calculation
        new_space = spaces + "  "

        # Total time for all the sub-components
        component_time = 0.0

        # Desired quantity of the product
        desired_qty = produce_qty
        if (produce_itm in self.get_items_list() and desired_produce[produce_itm] > self.get_item_quantity(produce_itm)):
            desired_qty = desired_produce[produce_itm] - self.get_item_quantity(produce_itm)
        desired_qty = int(math.ceil(desired_qty / self.get_produce_qty(recipe_name)))

        # Calculation for each sub-component recipe time and resources
        for i in range(desired_qty):
            recipe_time = 0.0
            # Recursively calculate sub-sub component recipe
            for consume_itm,consume_qty in self.get_consumes(recipe_name):
                self.__add_item_to_dict(desired_produce,consume_itm,consume_qty)
                consumes_recipe_time = self.__get_sub_component(desired_produce,consume_itm,desired_produce[consume_itm],new_space)

                # Recipe doesnt exists. Ignore for raw material
                if (consumes_recipe_time < 0.0):
                    return -1.0
                # Calculate recipe time
                else:
                    recipe_time += consumes_recipe_time
                    component_time += consumes_recipe_time

            # Remove the produce item as it is being manufactured from its raw materials
            desired_produce[produce_itm] -= self.get_produce_qty(recipe_name)

            # Updating all the respective times for current produce manufacturing
            consumes_time = self.get_time(recipe_name)
            self.manufacture_time += consumes_time
            recipe_time += consumes_time
            component_time += consumes_time

            # Initialise the inventory list for a new produce item
            if (produce_itm not in self.get_items_list()):
                self.add_item(produce_itm, 0)

            print(spaces + "> building recipe '"+recipe_name+"' in "+str(consumes_time)+" s ("+str(recipe_time)+"s total)")

        return component_time

    def __manufacture(self, order_itm, order_qty):
        if (not isinstance(order_itm, str) or not isinstance(order_qty, int)):
            return False
        for i in range(order_qty):
            count = 0

            # Check if the order item is in the inventory list
            # and get the count available
            if (order_itm in self.get_items_list()):
                count = self.get_item_quantity(order_itm)

            # Set the item to 0
            self.set_item_quantity(order_itm, 0)
            self.manufacture_time = 0

            # Desired list of produce
            desired_produce = {order_itm:1}

            # If sufficient resources not found, then print inventory and return
            if (self.__get_sub_component(desired_produce,order_itm,1,"  ") < 0.0):
                print("Insufficient resources to build: " + order_itm)
                self.set_item_quantity(order_itm, count)
                return False

            # Display manufacturing time for an ordered item
            print("Built "+order_itm+" in "+str(self.manufacture_time)+" seconds\n")
            #print(desired_produce)

            # Update inventory list by removing the items needed for the manufacturing
            for inventory_itm in self.get_items_list():
                if (inventory_itm in desired_produce.keys() and self.get_item_quantity(inventory_itm) >= desired_produce[inventory_itm]):
                    self.remove_item(inventory_itm,desired_produce[inventory_itm])
                    desired_produce[inventory_itm] = 0

            # Add the ordered item to the inventory
            self.set_item_quantity(order_itm,(count+1))
        return True

    def manufacture(self,complete_order):
        if (isinstance(complete_order,list)):
            for order in complete_order:
                if (len(list(order.keys())) == 1 and
                    not self.__manufacture(list(order.keys())[0], list(order.values())[0])):
                    break

        return self.get_inventory()
