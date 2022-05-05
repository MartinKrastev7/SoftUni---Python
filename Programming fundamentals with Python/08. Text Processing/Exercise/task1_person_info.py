lines_strings = int(input())
name = ""
age = ""

for i in range(1, lines_strings + 1):
    strings = input()
    name_index_first = strings.index("@")
    name_index_last = strings.index("|")

    name = strings[name_index_first + 1:name_index_last]

    age_index_first = strings.index("#")
    age_index_last = strings.index("*")

    age = strings[age_index_first + 1:age_index_last]

    print(f"{name} is {age} years old.")