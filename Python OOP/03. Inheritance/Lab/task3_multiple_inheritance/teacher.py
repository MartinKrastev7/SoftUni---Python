from task3_multiple_inheritance.employee import Employee
from task3_multiple_inheritance.person import Person


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."