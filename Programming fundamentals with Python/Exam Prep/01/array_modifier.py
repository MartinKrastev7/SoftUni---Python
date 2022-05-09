elements = [int(x) for x in input().split(" ")]
command = input()

while command != "end":
    list_comand = command.split(" ")
    new_command = list_comand[0]
    if len(list_comand) > 1:
        first = int(list_comand[1])
        second = int(list_comand[2])

    if new_command == "swap":
        elements[first], elements[second] = elements[second], elements[first]

    elif new_command == "multiply":
        result = elements[first] * elements[second]
        elements[first] = result

    elif new_command == "decrease":
        elements = [x - 1 for x in elements]

    command = input()

elements = [str(x) for x in elements]

print(", ".join(elements))

#vtoro reshenie
numbers = input().split(" ")
numbers = list(map(int, numbers))

line = input()
while line != "end":

    if line == "decrease":
        numbers = list(map(lambda n: n - 1, numbers))

    else:
        explode = line.split(" ")
        command = explode[0]
        index1 = int(explode[1])
        index2 = int(explode[2])

        if command == "swap":
            numbers[index1], numbers[index2] = numbers[index2], numbers[index1]

        elif command == "multiply":
            numbers[index1] = numbers[index1] * numbers[index2]

    line = input()

numbers = list(map(str, numbers))
output = ", ".join(numbers)
print(output)
