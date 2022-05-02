to_do = [0] * 10

while True:
    command = input()

    if command == "End":
        break
    token = command.split("-")
    priority = int(token[0]) - 1
    note = token[1]
    to_do.pop(priority)
    to_do.insert(priority, note)

result = [element for element in to_do if element != 0]
print(result)

# vtori nachin
todo = ["" for i in range(11)]

command = input()

while command != "End":
    explode = command.split("-")
    priority = int(explode[0])
    task = explode[1]
    todo[priority] = task


    command = input()

final_todo = [task for task in todo if task != ""]

print(final_todo)