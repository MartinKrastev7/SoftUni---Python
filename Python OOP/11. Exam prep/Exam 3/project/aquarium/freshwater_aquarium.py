from project.aquarium.base_aquarium import BaseAquarium


class FreshwaterAquarium(BaseAquarium):
    def __init__(self, name):
        super().__init__(name= name, capacity=50)
        self.aquarium_fish_type = "FreshwaterFish"
