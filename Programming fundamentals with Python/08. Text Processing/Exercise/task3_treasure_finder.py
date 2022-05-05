numbers = input().split(" ")
new_text = ""
count = 0
while True:
    command = input()
    new_text = ""
    count = 0
    if command == "find":
        break

    for i in range(len(command)):
        char = ord(command[i])
        if count + 1 > len(numbers):
            count = 0
        result = char - int(numbers[count])
        #new_text.append(chr(result))
        new_text += chr(result)
        count += 1

    type_first = new_text.split("&")[1].split("&")[0]
    coordinates = new_text.split("<")[1].split(">")[0]

    print(f"Found {type_first} at {coordinates}")





