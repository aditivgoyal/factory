from lib.Inventory import Inventory
from lib.Recipes import Recipes
import math

class Builder(Inventory, Recipes):
    """
    This checks all the sub-components required for the product to be built
    and try to build it
    """
    def __init__(self):
        Inventory.__init__(self)
        Recipes.__init__(self)
        self.manufacture_time = 0

    def check_components(self, desired_consumer, produce_itm, produce_qty, spaces):
        # Check if item is available in the inventory
        if(self.check_item(produce_itm,produce_qty)):
            return 0

        recipe_name = self.get_recipe_name(produce_itm)
        if (recipe_name == ""):
            return -1.0

        new_space = spaces + "  "
        total_recipe_time = 0.0
        desired_qty = produce_qty
        if (produce_itm in self.inventory_list.keys() and desired_consumer[produce_itm] > self.inventory_list[produce_itm]):
            desired_qty = desired_consumer[produce_itm] - self.inventory_list[produce_itm]

        desired_qty = int(math.ceil(desired_qty / self.get_product_qty(recipe_name)))

        for i in range(desired_qty):
            recipe_time = 0.0
            for inventory_itm,inventory_qty in self.get_consumes(recipe_name).items():
                if(inventory_itm in desired_consumer.keys()):
                    desired_consumer[inventory_itm] += inventory_qty
                else:
                    desired_consumer[inventory_itm] = inventory_qty
                consumes_recipe_time = self.check_components(desired_consumer,inventory_itm,desired_consumer[inventory_itm],new_space)

                if (consumes_recipe_time < 0.0):
                    return -1.0
                else:
                    recipe_time += consumes_recipe_time
                    total_recipe_time += consumes_recipe_time

            desired_consumer[produce_itm] -= self.get_product_qty(recipe_name)

            consumes_time = self.get_time(recipe_name)
            self.manufacture_time += consumes_time
            recipe_time += consumes_time
            total_recipe_time += consumes_time

            if (produce_itm not in self.inventory_list.keys()):
                self.inventory_list[produce_itm] = 0

            print(spaces + "> building recipe '"+recipe_name+"' in "+str(consumes_time)+" s ("+str(recipe_time)+"s total)")

        return total_recipe_time

    def manufacture(self, order_itm, order_qty):
        for i in range(order_qty):
            count = 0

            # Check if the order item is in the inventory list
            # and get the count available
            if (order_itm in self.inventory_list.keys()):
                count = self.inventory_list[order_itm]

            # Set the item to 0
            self.inventory_list[order_itm] = 0
            self.manufacture_time = 0

            desired_consumer = {order_itm:1}
            print("desired_outcomes ---->",desired_consumer)
            if (self.check_components(desired_consumer,order_itm,1,"  ") < 0.0):
                print("Insufficient resources to build: " + order_itm)
                self.inventory_list[order_itm] = count
                self.print_inventory()
                return

            print("Built "+order_itm+" in "+str(self.manufacture_time)+" seconds\n")
            #print(desired_consumer)

            for inventory_itm, inventory_qty in self.inventory_list.items():
                if (inventory_itm in desired_consumer.keys() and inventory_qty >= desired_consumer[inventory_itm]):
                    self.remove_item(inventory_itm,desired_consumer[inventory_itm])
                    #self.inventory_list[inventory_itm] -= desired_consumer[inventory_itm]
                    desired_consumer[inventory_itm] = 0

            #self.inventory_list[order_itm] = count + 1
            self.add_item(order_itm,(count+1))
            #print(self.inventory_list)
            #print("")

