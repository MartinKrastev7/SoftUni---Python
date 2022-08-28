from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        consumption = sum([room.expenses + room.room_cost for room in self.rooms])
        return f"Monthly consumption: {consumption:.2f}$."

    def pay(self):
        result = []
        for room in self.rooms:
            total_expenses = room.expenses + room.room_cost
            if room.budget >= total_expenses:
                room.budget -= total_expenses
                result.append(f"{room.family_name} paid {total_expenses:.2f}$ and have {room.budget:.2f}$ left.")
            else:
                result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                self.rooms.remove(room)
        return '\n'.join(result)

    def status(self):
        result = ""
        all_people = sum([room.members_count for room in self.rooms])
        result += f"Total population: {all_people}\n"
        for room in self.rooms:
            result += f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$\n"
            num = 0
            for child in room.children:
                num += 1
                result += f"--- Child {num} monthly cost: {child.cost * 30:.2f}$\n"
            appliances_cost = sum([app.get_monthly_expense() for app in room.appliances])
            result += f"--- Appliances monthly cost: {appliances_cost:.2f}$\n"

        return result



