##### Garden Simulator #####
'''
This is a text-based game where you can grow and manage virtual plants in a garden.
'''

import random

# Defining classes
class Plant:

    """
    A plant is a living thing that can be grown in a garden. A plant has a name, a number of days to mature, a maximum harvest yield, a list of growth stages, a current growth stage, a harvestable status, and a harvest yield.
    """

    def __init__(self, name, harvest_yield):
        self.name = name
        self.harvest_yield = harvest_yield
        self.growth_stages = ["seed", "sprout", "mature", "blooming", "fruiting", "harvest-ready"]
        self.current_growth_stage = self.growth_stages[0]
        self.harvestable = False
    
    def grow(self):
        """
        Grow the plant. Increments current_growth_stage by 1 and sets harvestable to True if current_growth_stage is "harvest-ready".
        """
        self.current_growth_stage = self.growth_stages[self.growth_stages.index(self.current_growth_stage) + 1]
        if self.current_growth_stage == "harvest-ready":
            self.harvestable = True
            print(f"Your {self.name} is ready to harvest!")

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
 
    def harvest(self):
        """
        Harvest a plant. Updates gardener's inventory, removes plant from planted plants, and returns True if successful, False if not.
        """
        plant = select_item(player.planted_plants)
        if plant.harvest():
            if plant.name in self.inventory:
               self.inventory[plant.name] += plant.harvest_yield
            else:
                self.inventory[plant.name] = plant.harvest_yield
            print(f"You harvested {plant.harvest_yield} {plant.name}(s)!")
            self.planted_plants.remove(plant)
            return True
        else:
            print("You don't have any harvestable plants!")
            return False
    
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

def select_item(inventory):
    """
    Select an item from a list or dictionary. 
    Takes a dictionary or list of items. Returns the item the player selects.
    """
    
    # Display items for the user to select
    if type(inventory) == dict:
        items = list(inventory.keys())
        for i in range(len(items)):
            print(f"{i + 1}. {items[i]}")
    elif type(inventory) == list:
        for i in range(len(inventory)):
            print(f"{i + 1}. {inventory[i].name}")
    else:
        print("Unsupported inventory type.")
        return None

    while True:
        item_number = input("Select an item by its position number: ")
        try:
            item_number = int(item_number)
            
            # Check if the selected number is within the valid range
            if 1 <= item_number <= len(inventory):
                if type(inventory) == dict:
                    return items[item_number - 1]
                else:
                    return inventory[item_number - 1]
            else:
                print("Invalid selection. Please enter a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

plant_list = ["tomato", "carrot", "sunflower", "radish"
              ]
## Begin game logic ##
# Get player name
player_name = input("What is your name? ")
player = Gardener(player_name)

# list actions player can take
actions = ["plant", "tend", "harvest", "forage", "help", "quit"]

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
        elif action == "help":
            print("****Actions****")
            for action in actions:
                print(action)
        elif action == "quit" or action == "exit":
            break
    else:
        print("That is not a valid action. Type 'help' for a list of actions you can take.")