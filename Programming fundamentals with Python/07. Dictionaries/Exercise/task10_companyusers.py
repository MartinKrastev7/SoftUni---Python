employees_dict = {}

while True:
    command = input()

    if command == "End":
        break

    command = command.split(" -> ")
    company = command[0]
    name = command[1]

    if company not in employees_dict.keys():
        employees_dict[company] = [name]
    else:
        if name not in employees_dict[company]:
            employees_dict[company].append(name)

for key, value in employees_dict.items():
    print(f"{key}")

    for id in value:
        print(f"-- {id}")