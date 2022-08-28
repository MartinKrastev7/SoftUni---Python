from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "" or value == " ":
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type, name, price):
        food_exists = [f for f in self.food_menu if f.name == name]
        if food_exists:
            raise Exception(f"{food_type} {name} is already in the menu!")

        food = ""
        if food_type == "Bread":
            food = Bread(name, price)
        elif food_type == "Cake":
            food = Cake(name, price)

        self.food_menu.append(food)
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type, name, portion, brand):
        drink_exists = [d for d in self.drinks_menu if d.name == name]
        if drink_exists:
            raise Exception("{drink_type} {name} is already in the menu!")

        drink = ""
        if drink_type == "Tea":
            drink = Tea(name, portion, brand)
        elif drink_type == "Water":
            drink = Water(name, portion, brand)

        self.drinks_menu.append(drink)
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type, table_number, capacity):
        table_exists = [t for t in self.tables_repository if t.table_number == table_number]
        if table_exists:
            raise ValueError(f"Table {table_number} is already in the bakery!")

        table = ""
        if table_type == "InsideTable":
            table = InsideTable(table_number, capacity)
        elif table_type == "OutsideTable":
            table = OutsideTable(table_number, capacity)

        self.tables_repository.append(table)
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people):
        table = [t for t in self.tables_repository if (not t.is_reserved) and (t.capacity >= number_of_people)]
        if table:
            table[0].reserve(number_of_people)
            return f"Table {table[0].table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number, *food_names):
        table = [t for t in self.tables_repository if t.table_number == table_number]
        if not table:
            return f"Could not find table {table_number}"

        food_in_menu = []
        food_not_in_menu = []

        for food in food_names:
            food_exists = [f for f in self.food_menu if f.name == food]
            if food_exists:
                food_exists = food_exists[0]
                table[0].order_food(food_exists)
                food_in_menu.append(food_exists)
            else:
                food_not_in_menu.append(food)

        result = ""
        if food_in_menu:
            result = f"Table {table[0].table_number} ordered:\n"
            for f in food_in_menu:
                result += f"{f}\n"

        if food_not_in_menu:
            result += f"{self.name} does not have in the menu:\n"
            for name in food_not_in_menu:
                result += name + '\n'
        return result.strip()

    def order_drink(self, table_number, *drinks_name):
        table = [t for t in self.tables_repository if t.table_number == table_number]
        if not table:
            return f"Could not find table {table_number}"

        drink_in_menu = []
        drink_not_in_menu = []

        for drink in drinks_name:
            drink_exists = [d for d in self.drinks_menu if d.name == drink]
            if drink_exists:
                drink_exists = drink_exists[0]
                table[0].order_drink(drink_exists)
                drink_in_menu.append(drink_exists)
            else:
                drink_not_in_menu.append(drink)

        result = ""
        if drink_in_menu:
            result = f"Table {table[0].table_number} ordered:\n"
            for f in drink_in_menu:
                result += f"{f}\n"

        if drink_not_in_menu:
            result += f"{self.name} does not have in the menu:\n"
            for name in drink_not_in_menu:
                result += name + '\n'
        return result.rstrip()

    def leave_table(self, table_number):
        table = [t for t in self.tables_repository if t.table_number == table_number]
        if table:
            bill = table[0].get_bill()
            self.total_income += bill
            table[0].clear()
            return f"Table: {table_number}\nBill: {bill:.2f}"

    def get_free_tables_info(self):
        result = ""
        for table in self.tables_repository:
            if table.free_table_info():
                result += f"{table.free_table_info()}\n"
        return result

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"



