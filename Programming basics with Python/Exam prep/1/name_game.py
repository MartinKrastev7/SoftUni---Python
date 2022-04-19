is_name_stop = False
points = 0
while True:
    name = input()
    if name == "Stop":
        is_name_stop = True
        break
    for ch in range(1, len(name) + 1):
        number = int(input())
        name = ord(name)
        if number == name:
            points += 10

