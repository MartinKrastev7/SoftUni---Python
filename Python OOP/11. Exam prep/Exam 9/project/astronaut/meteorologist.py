from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    def __init__(self, name):
        super().__init__(name=name, oxygen=90)

    def breathe(self):
        self.oxygen -= 15
