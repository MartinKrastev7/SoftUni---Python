import abc


class Car(abc.ABC):
    @abc.abstractmethod
    def __init__(self, model, speed_limit):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if len(value) < 4:
            raise ValueError(f"Model {value} is less than 4 symbols!")
        self.__model = value

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):

        if self.__class__.__name__ == "SportsCar":
            if value < 400 or value > 600:
                raise ValueError(f"Invalid speed limit! Must be between 400 and 600!")

        if self.__class__.__name__ == "MuscleCar":
            if value < 250 or value > 450:
                raise ValueError(f"Invalid speed limit! Must be between 250 and 450!")

        self.__speed_limit = value

