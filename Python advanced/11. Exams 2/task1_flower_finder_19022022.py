from collections import deque

vowels = deque(input().split(" "))
consonants = input().split(" ")

words_dict = {
    "rose": "rose",
    "tulip": "tulip",
    "lotus": "lotus",
    "daffodil": "daffodil"
}

word = ""
is_found = False
while vowels and consonants:
    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()

    for key in words_dict.keys():
        words_dict[key] = words_dict[key].replace(current_vowel, "")
        words_dict[key] = words_dict[key].replace(current_consonant, "")
        if words_dict[key] == "":
            word = key
            is_found = True
            break

    if is_found:
        break

if is_found:
    print(f"Word found: {word}")
else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")