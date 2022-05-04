string = input()
count = 1
collect_dict = {}
key = ""
value = ""
while string != "stop":
    if count % 2 == 0:
        value = int(string)
        count += 1

    else:
        key = string
        count += 1
        string = input()
        continue

    if key in collect_dict:
        collect_dict[key] += value
    else:
        collect_dict[key] = value
    string = input()

for key, value in collect_dict.items():
    print(f"{key} -> {value}")

#vtori nachin
def miner_task():
    items = {}

    while True:
        resource = input()

        if resource == "stop":
            break

        quantity = int(input())

        if resource not in items:
            items[resource] = quantity
        else:
            items[resource] += quantity

    for key,value in items.items():
        print(f"{key} -> {value}")

miner_task()