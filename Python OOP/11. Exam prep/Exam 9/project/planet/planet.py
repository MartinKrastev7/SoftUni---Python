class Planet:
    def __init__(self, name):
        self.name = name
        #if len(items) > 0:
         #   self.items = items[0].split(", ")
        #else:
        self.items = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "" or value == " ":
            raise ValueError("Planet name cannot be empty string or whitespace!")
        self.__name = value

