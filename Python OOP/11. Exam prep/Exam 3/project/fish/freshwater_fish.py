from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    def __init__(self, name, species, price):
        super().__init__(name=name, species=species, size=3, price=price)
        self.allowed_aquarium = "FreshwaterAquarium"

    def eat(self):
        self.size += 3
