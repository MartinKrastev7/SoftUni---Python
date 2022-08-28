from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in ["FreshwaterAquarium", "SaltwaterAquarium"]:
            return "Invalid aquarium type."

        if aquarium_type == "FreshwaterAquarium":
            aquarium = FreshwaterAquarium(aquarium_name)
        elif aquarium_type == "SaltwaterAquarium":
            aquarium = SaltwaterAquarium(aquarium_name)

        self.aquariums.append(aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type not in ["Ornament", "Plant"]:
            return "Invalid decoration type."

        if decoration_type == "Ornament":
            decoration = Ornament()
        elif decoration_type == "Plant":
            decoration = Plant()

        self.decorations_repository.add(decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        aquarium_exists = [aq for aq in self.aquariums if aq.name == aquarium_name]
        decoration_exists = [d for d in self.decorations_repository.decorations if d.__class__.__name__ == decoration_type]

        if aquarium_exists and decoration_exists:
            aquarium = aquarium_exists[0]
            decoration = self.decorations_repository.find_by_type(decoration_type)
            aquarium.decorations.append(decoration)
            self.decorations_repository.decorations.remove(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."
        elif self.decorations_repository.find_by_type(decoration_type) == "None":
            return f"There isn't a decoration of type {decoration_type}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type not in ["FreshwaterFish", "SaltwaterFish"]:
            return f"There isn't a fish of type {fish_type}."

        fish_created = ""
        if fish_type == "FreshwaterFish":
            fish_created = FreshwaterFish(fish_name, "Freshwater", price)
        elif fish_type == "SaltwaterFish":
            fish_created = SaltwaterFish(fish_name, "Saltwater", price)

        aquarium_found = [aq for aq in self.aquariums if aq.name == aquarium_name]
        if aquarium_found:
            aquarium = aquarium_found[0]
            if len(aquarium.fish) >= aquarium.capacity:
                return "Not enough capacity."
            elif fish_type != aquarium.aquarium_fish_type:
                return "Water not suitable."
            aquarium.add_fish(fish_created)
            #ili s overridden na add methoda ot baseaquarium
            #msg = aquarium.add_fish(fish_created)
            #if not msg:
             #   return "Water not suitable"
            #return msg
            return f"Successfully added {fish_type} to {aquarium_name}."

    def feed_fish(self, aquarium_name: str):
        aquarium_found = [aq for aq in self.aquariums if aq.name == aquarium_name]
        if aquarium_found:
            aquarium_found[0].feed()
            return f"Fish fed: {len(aquarium_found[0].fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium_found = [aq for aq in self.aquariums if aq.name == aquarium_name]
        value = 0
        if aquarium_found:
            fish_sum = sum(f.price for f in aquarium_found[0].fish)
            decor_sum = sum(d.price for d in aquarium_found[0].decorations)
            value = fish_sum + decor_sum
        return f"The value of Aquarium {aquarium_name} is {value:.2f}."


    def report(self):
        result = ""
        for aq in self.aquariums:
            result += aq.__str__()
        return result.rstrip()