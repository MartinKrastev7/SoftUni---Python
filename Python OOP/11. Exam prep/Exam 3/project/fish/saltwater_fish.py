from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    def __init__(self, name, species, price):
        super().__init__(name=name, species=species, size=5, price=price)
        self.allowed_aquarium = "SaltwaterAquarium"

    def eat(self):
        self.size += 2
