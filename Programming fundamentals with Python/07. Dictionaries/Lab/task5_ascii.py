characters = input().split(", ")
char_dict = {char: ord(char) for char in characters} # vmesto dolniq for

for char in characters:
    char_dict[char] = ord(char)

print(char_dict)