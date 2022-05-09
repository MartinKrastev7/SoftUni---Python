sequence = input().split(" ")
counter = 0

while True:
    command = input()
    if command == "end":
        break
    counter += 1
    string = command.split(" ")
    left = int(string[0])
    right = int(string[1])
    if left == right or 0 > left or left >= len(sequence) or 0 > right or right >= len(sequence):
        print(f"Invalid input! Adding additional elements to the board")
        mid_point = len(sequence) // 2
        sequence.insert(mid_point, f"-{counter}a")
        sequence.insert(mid_point, f"-{counter}a")
    else:
        if sequence[left] == sequence[right]:
            left_item_to_remove = sequence[left]
            sequence.remove(left_item_to_remove)
            sequence.remove(left_item_to_remove)
            print(f"Congrats! You have found matching elements - {left_item_to_remove}!")
        else:
            print(f"Try again!")
    if len(sequence) == 0:
        print(f"You have won in {counter} turns!")
        break

if len(sequence) > 0:
    print(f"Sorry you lose :(")
    print(*sequence)

#vtori nachin
sequence_of_elements = input().split()
count_moves = 0
command = input()
while not command == "end":
    count_moves += 1
    index1 = int(command.split()[0])
    index2 = int(command.split()[1])
    if index1 == index2 or index1 < 0 or index2 < 0 or index1 >= len(sequence_of_elements) or index2 >= len(sequence_of_elements):
        sequence_of_elements.insert(int(len(sequence_of_elements) / 2), f"-{str(count_moves)}a")
        sequence_of_elements.insert(int(len(sequence_of_elements) / 2), f"-{str(count_moves)}a")
        print("Invalid input! Adding additional elements to the board")
    elif sequence_of_elements[index1] == sequence_of_elements[index2]:
        print(f"Congrats! You have found matching elements - {sequence_of_elements[index1]}!")
        x = sequence_of_elements.pop(index1)
        sequence_of_elements.remove(x)
    elif sequence_of_elements[index1] != sequence_of_elements[index2]:
        print("Try again!")
    if len(sequence_of_elements) == 0:
        print(f"You have won in {count_moves} turns!")
        break
    command = input()
if command == "end":
    print("Sorry you lose :(\n"
          f"{' '.join(sequence_of_elements)}")