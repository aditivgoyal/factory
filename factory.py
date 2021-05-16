
from lib.Inventory import Inventory
from lib.Recipes import Recipes
from lib.Builder import Builder



'''
2 * circuit -> 1.5
    1 iron plate
    3 copper cable -> 0.5
        .5 copper plate
1 * block -> 10.0
    1 steel plate -> 16.0
        5 iron plate
    1 iron gear -> 0.5
        2 iron plate
    2 pipe -> 0.5
        1 iron plate
15 * lubricant

'''


if __name__ == "__main__":

    inventory = Inventory()
    inventory.print_inventory()

    recipes = Recipes()


    total_time = 0

    b = Builder()
    b.manufacture("electric_engine", 3)
    b.manufacture("electric_circuit", 5)
    b.manufacture("electric_engine", 3)
    b.dump_inventory()
