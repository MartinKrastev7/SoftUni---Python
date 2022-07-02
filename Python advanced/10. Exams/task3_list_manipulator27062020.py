from collections import deque


def list_manipulator(numbers, *args):
    command_first = args[0]
    command_second = args[1]
    other_numbers = list(args[2:])

    if command_first == "add":
        if command_second == "end":
            numbers.extend(other_numbers)
            return numbers
        elif command_second == "beginning":
            other_numbers.extend(numbers)
            return other_numbers

    elif command_first == "remove":
        if command_second == "end":
            if other_numbers:
                for i in range(*other_numbers):
                    numbers.pop()
                return numbers
            else:
                numbers.pop()
                return numbers
        elif command_second == "beginning":
            numbers = deque(numbers)
            if other_numbers:
                for i in range(*other_numbers):
                    numbers.popleft()
                return list(numbers)
            else:
                numbers.popleft()
                return list(numbers)


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))




