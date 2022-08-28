from collections import deque

from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.suitable_astronauts = []
        self.completed_missions = 0
        self.uncompleted_missions = 0

    def add_astronaut(self, astronaut_type, name):
        if astronaut_type not in ["Biologist", "Geodesist", "Meteorologist"]:
            raise Exception("Astronaut type is not valid!")

        astronaut_exists = [a for a in self.astronaut_repository.astronauts if a.name == name]
        if astronaut_exists:
            return f"{name} is already added."

        astronaut = None
        if astronaut_type == "Biologist":
            astronaut = Biologist(name)
        elif astronaut_type == "Geodesist":
            astronaut = Geodesist(name)
        elif astronaut_type == "Meteorologist":
            astronaut = Meteorologist(name)

        self.astronaut_repository.astronauts.append(astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name, *items):
        planet_exists = [p for p in self.planet_repository.planets if p.name == name]
        if planet_exists:
            return f"{name} is already added."
        #items_joined = []
        #for item in items:
       #     items_joined.append(item)
      #  items_joined = [i.split(", ") for i in items_joined]

        planet = Planet(name)
        for item in items:
            planet.items.append(str(item))
        self.planet_repository.add(planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name):
        astronaut_exists = [a for a in self.astronaut_repository.astronauts if a.name == name]
        if not astronaut_exists:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.astronauts.remove(astronaut_exists[0])
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for a in self.astronaut_repository.astronauts:
            a.increase_oxygen(10)

    def send_on_mission(self, planet_name):
        planet_exists = [a for a in self.planet_repository.planets if a.name == planet_name]
        if not planet_exists:
            raise Exception(f"Invalid planet name!")

        count_astr = 0
        for a in self.astronaut_repository.astronauts:
            if a.oxygen > 30 and count_astr < 5:
                self.suitable_astronauts.append(a)
                count_astr += 1

        if len(self.suitable_astronauts) == 0:
            raise Exception("You need at least one astronaut to explore the planet!")

        self.suitable_astronauts.sort(key=lambda a: a.oxygen, reverse=True)

        astronauts_participated = 0
        sorted_astronauts = deque(self.suitable_astronauts)
        planet_items_reversed = deque(planet_exists[0].items)

        while True:
            astronaut = sorted_astronauts.popleft()
            astronauts_participated += 1

            while planet_items_reversed:
                item = planet_items_reversed.pop()
                astronaut.breathe()
                astronaut.backpack.append(item)

                if astronaut.oxygen <= 0:
                    break

            if len(sorted_astronauts) > 0 and len(planet_items_reversed) > 0:
                continue

            elif not planet_items_reversed:
                self.completed_missions += 1
                return f"Planet: {planet_name} was explored. {astronauts_participated} astronauts participated in collecting items."
            elif planet_items_reversed:
                self.uncompleted_missions += 1
                return "Mission is not completed."

    def report(self):
        result = f"{self.completed_missions} successful missions!\n"
        result += f"{self.uncompleted_missions} missions were not completed!\n"
        result += f"Astronauts' info:\n"
        for a in self.astronaut_repository.astronauts:
            result += f"Name: {a.name}\n"
            result += f"Oxygen: {a.oxygen}\n"
            if a.backpack:
               # items = ', '.join(a.backpack)
                result += f"Backpack items: {a.backpack}\n"
            else:
                result += f'Backpack items: "none"\n'

        return result
