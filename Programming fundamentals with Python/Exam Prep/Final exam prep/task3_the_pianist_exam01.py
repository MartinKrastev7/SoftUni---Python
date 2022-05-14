number_of_pieces = int(input())
pieces_dict = {}


for i in range(number_of_pieces):
    pieces = input().split("|")
    current_pieces = pieces[0]
    composer = pieces[1]
    key = pieces[2]

    current_pieces_dict = {}
    current_pieces_dict["composer"] = composer
    current_pieces_dict["key"] = key
    pieces_dict[current_pieces] = current_pieces_dict

command = input()

while command != "Stop":
    command = command.split("|")
    current_command = command[0]

    if current_command == "Add":
        piece = command[1]
        composer = command[2]
        key = command[3]

        if piece not in pieces_dict:
            pieces_dict[piece] = {"composer": composer, "key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    elif current_command == "Remove":
        piece = command[1]

        if piece in pieces_dict:
            pieces_dict.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif current_command == "ChangeKey":
        piece = command[1]
        new_key = command[2]

        if piece in pieces_dict:
            pieces_dict[piece]["key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    command = input()

for key in pieces_dict:
    print(f"{key} -> Composer: {pieces_dict[key]['composer']}, Key: {pieces_dict[key]['key']}")