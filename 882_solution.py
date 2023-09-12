##### Garden Simulator #####
'''
This is a text-based game where you can grow and manage virtual plants in a garden.
'''

import random
from datetime import datetime

# Creating a logging decorator
def log(func):
    def wrapper(*args, **kwargs):
        print(f"{datetime.now()}: {func.__name__} was called with arguments {args} and keyword arguments {kwargs}")
        return func(*args, **kwargs)
    return wrapper

# Defining classes
class Plant:

    """
    A plant is a living thing that can be grown in a garden. A plant has a name, a number of days to mature, a maximum harvest yield, a list of growth stages, a current growth stage, a harvestable status, and a harvest yield.
    """

    def __init__(self, name, max_harvest_yield):
        self.name = name
        self.max_harvest_yield = max_harvest_yield
        self.growth_stages = ["seed", "sprout", "mature", "blooming", "fruiting", "harvest-ready"]
        self.current_growth_stage = self.growth_stages[0]
        self.harvestable = False
        self._harvest_yield = random.randint(1, self.max_harvest_yield)
    
    @log
    def grow(self):
        """
        Grow the plant. Increments current_growth_stage by 1 and sets harvestable to True if current_growth_stage is "harvest-ready".
        """
        self.current_growth_stage = self.growth_stages[self.growth_stages.index(self.current_growth_stage) + 1]
        if self.current_growth_stage == "harvest-ready":
            self.harvestable = True
            print(f"Your {self.name} is ready to harvest!")

    @log
    def harvest(self):
        """
        Harvest the plant. Sets harvestable to False, sets current_growth_stage to "seed", and sets current_age to 0.
        """
        if self.harvestable:
            self.harvestable = False
            self.current_growth_stage = self.growth_stages[0]
            return True
        else:
            return False
       
class Tomato(Plant): 
    """
    A tomato is a plant that has a name, a number of days to mature, a maximum harvest yield, a list of growth stages, a current growth stage, a harvestable status, and a harvest yield.
    """

    def __init__(self):
        super().__init__("tomato", 10)

class Carrot(Plant):
    """
    A carrot is a plant that has a name, a number of days to mature, a maximum harvest yield, a list of growth stages, a current growth stage, a harvestable status, and a harvest yield.
    """

    def __init__(self):
        super().__init__("carrot", 2)
        self.growth_stages = ["seed", "sprout", "mature", "harvest-ready"]

class Sunflower(Plant):
    """
    A sunflower is a plant that has a name, a number of days to mature, a maximum harvest yield, a list of growth stages, a current growth stage, a harvestable status, and a harvest yield.
    """

    def __init__(self):
        super().__init__("sunflower", 100)
        self.growth_stages = ["seed", "sprout", "mature", "blooming", "harvest-ready"]

class Radish(Plant):
    """
    A radish is a plant that has a name, a number of days to mature, a maximum harvest yield, a list of growth stages, a current growth stage, a harvestable status, and a harvest yield.
    """

    def __init__(self):
        super().__init__("radish", 5)
        self.growth_stages = ["seed", "sprout", "mature", "harvest-ready"]

class Gardener:

    """
    A gardener is a person who tends to a garden. A gardener has a name and an inventory of seeds and harvested plants.
    """

    plant_dict = {"tomato": Tomato, "carrot": Carrot, "sunflower": Sunflower, "radish": Radish}

    def __init__(self, name):
        self.name = name
        self.inventory = {}
        self.planted_plants = []

    @log
    def get_inventory(self):
        """
        Get gardener's inventory. Returns a dictionary of gardener's inventory.
        """
        print("****Inventory****")
        for item in self.inventory:
            try:
                name = item.name
                print(f"{name}: {self.inventory[item]}")
            except:
                print(f"{item}: {self.inventory[item]}")
    
    @log
    def plant(self):
        """
        Plant a plant. Returns True if successful updates gardener's inventory, False if not.
        """
        plant_name = select_item(self.inventory)
        if plant_name in self.inventory and self.inventory[plant_name] > 0:
            self.inventory[plant_name] -= 1
            if self.inventory[plant_name] == 0:
                del self.inventory[plant_name]
            
            # Use the dictionary to create an instance of the desired plant
            new_plant = self.plant_dict[plant_name]()
            self.planted_plants.append(new_plant)
            
            print(f"Planted a {plant_name}.")
        else:
            print(f"No {plant_name}s available in the inventory to plant.")


    @log
    def tend(self):
        """
        Tend to plants. Returns True if successful, False if not.
        """
        if len(self.planted_plants) > 0:
            for plant in self.planted_plants:
                if plant.current_growth_stage == "harvest-ready":
                    print(f"Your {plant.name} is ready to harvest!")
                else:
                    plant.grow()
                    print(f"You tended to the {plant.name}. It is now {plant.current_growth_stage}.")
            return True
        else:
            print("You don't have any plants to tend to!")
            return False

    @log  
    def harvest(self):
        """
        Harvest a plant. Updates gardener's inventory, removes plant from planted plants, and returns True if successful, False if not.
        """
        plant = select_item(player.planted_plants)
        if plant.harvest():
            if plant.name in self.inventory:
               self.inventory[plant.name] += plant._harvest_yield
            else:
                self.inventory[plant.name] = plant._harvest_yield
            print(f"You harvested {plant._harvest_yield} {plant.name}(s)!")
            self.planted_plants.remove(plant)
            return True
        else:
            print("You don't have any harvestable plants!")
            return False
    
    @log
    def forage_for_seeds(self):
        """
        Forage for seeds. Takes a list of plants and adds a random plant to the gardener's inventory.
        """
        plant = random.choice(plant_list)

        if plant in self.inventory:
            self.inventory[plant] += 1
        else:
            self.inventory[plant] = 1
        print(f"You found a {plant} seed!")

    def current_plants(self):
        """
        Get gardener's current plants. Returns a list of gardener's current plants.
        """
        for plant in self.planted_plants:
            print(f"{plant.name} is currently {plant.current_growth_stage}.")

def select_item(inventory):
    """
    Select an item from a list. Takes a dictionary of items. Returns the item the player selects.
    """
    # Display the items for the user to select.
    if type(inventory) == dict:
        for item in inventory:
            print(f"{list(inventory.keys()).index(item) + 1}. {item}")

        item_number = input("Select an item by a position number: ")
        try:
            item_number = int(item_number)
            return list(inventory.keys())[item_number - 1]
        except:
            print("Invalid selection. Please enter a number from the list.")
    elif type(inventory) == list:
        for item in inventory:
            print(f"{inventory.index(item) + 1}. {item.name}")

        item_number = input("Select an item by a position number: ")
        try:
            item_number = int(item_number)
            return inventory[item_number - 1]
        except:
            print("Invalid selection. Please enter a number from the list.")

plant_list = ["tomato", "carrot", "sunflower", "radish"
              ]
## Begin game logic ##
# Get player name
player_name = input("What is your name? ")
player = Gardener(player_name)

# list actions player can take
actions = ["plant", "tend", "harvest", "forage", "inventory", "help", "planted", "quit"]

print(f"Welcome to the garden, {player.name}!")
print("Type 'help' for a list of actions you can take.")

# Main game loop
while True:
    action = input("What would you like to do? ").lower()
    if action in actions:
        if action == "plant":
            player.plant()
        elif action == "tend":
            player.tend()
        elif action == "harvest":
            player.harvest()
        elif action == "forage":
            player.forage_for_seeds()
        elif action == "inventory":
            print(player.get_inventory())
        elif action == "help":
            print("****Actions****")
            for action in actions:
                print(action)
        elif action == "planted":
            player.current_plants()
        elif action == "quit" or action == "exit":
            break
    else:
        print("That is not a valid action. Type 'help' for a list of actions you can take.")