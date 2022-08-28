import abc


class BaseDecoration(abc.ABC):
    @abc.abstractmethod
    def __init__(self, comfort, price):
        self.comfort = comfort
        self.price = price
