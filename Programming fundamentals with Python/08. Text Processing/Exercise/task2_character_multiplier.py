strings = input().split(" ")

char1 = strings[0]
char2 = strings[1]
total = 0

for i in range(0, len(char1) + len(char2)):
    if i < len(char1) and i < len(char2):
        total += ord(char1[i]) * ord(char2[i])

    elif i < len(char1) and i >= len(char2):
        total += ord(char1[i])

    elif i >= len(char1) and i < len(char2):
        total += ord(char2[i])

print(total)

#vtori nachin
def sum_func(first_word, second_word):
    total_sum = 0

    for i in range(len(first_word)):
        if i < len(second_word):
            total_sum += ord(first_word[i]) * ord(second_word[i])
        else:
            total_sum += ord(first_word[i])

    return total_sum


def char_multiplier(first_word, second_word):
    result = 0
    if len(first_word) > len(second_word):
        result = sum_func(first_word, second_word)
    else:
        result = sum_func(first_word, second_word)

    print(result)


data = input().split(" ")
char_multiplier(data[0], data[1])