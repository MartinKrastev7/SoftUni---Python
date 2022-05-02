number = int(input())
new_list = [0 for x in range(number)]
command = input()

while command != "End":
    current_command = command.split(" ")

    if current_command[0] == "add":
        action = int(current_command[1])
        new_list[-1] = new_list[-1] + action

    elif current_command[0] == "insert":
        index = int(current_command[1])
        action = int(current_command[2])
        new_list[index] = new_list[index] + action

    elif current_command[0] == "leave":
        index = int(current_command[1])
        action = int(current_command[2])
        new_list[index] = new_list[index] - action

    command = input()

print(new_list)

#izvajdane na elementi ot dva lista
a = [2, 2, 2]
b = [1, 1, 1]
result = [a[i] - b[i] for i in range(len(a))]
#ili s lambda
a = [2, 2, 2]
b = [1, 1, 1]
result = list(map(lambda x, y: x - y, a, b))

#izvajdane na opredelena st-st ot vseki element ot list
numbers = [1, 2, 3]
numbers[:] = [number - 1 for number in numbers]
print(numbers)

#vtori nachin
num_wagons = int(input())
train = [0 for i in range(num_wagons)]
command = input()

while command != "End":
    explode = command.split(" ")
    current = explode[0]
    if current == "add":
        num_people = int(explode[1])
        train[-1] += num_people

    if current == "insert":
        position = int(explode[1])
        num_people = int(explode[2])
        train[position] += num_people

    if current == "leave":
        position = int(explode[1])
        num_people = int(explode[2])
        train[position] -= num_people

    command = input()
print(train)