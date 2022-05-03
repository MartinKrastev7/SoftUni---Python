class Inventory:
    def __init__(self, __capacity):
        self.capacity = __capacity
        self.items = []
        self.left = self.capacity

    def add_item(self, item):
        if self.capacity >= len(self.items):
            self.items.append(item)
            self.capacity -= 1
        else:
            return f"not enough room in the inventory"

    def get_capacity(self):
        return self.left

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.capacity}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)

#vtori nachin
class Inventory:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.items = []

    def add_item(self, item: str):
        if self.__capacity > len(self.items):
            self.items.append(item)
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        current_capacity = len(self.items) - self.__capacity
        return f"Items: {', '.join(self.items)}.\nCapacity left: {current_capacity}"