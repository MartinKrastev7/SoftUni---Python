number_lines = int(input())
first_numbers = []
filtered = []

for i in range(1, number_lines + 1):
    current_number = int(input())
    first_numbers.append(current_number)

command = input()

for number in first_numbers:
    if command == "even":
        if number % 2 == 0:
           filtered.append(number)

    elif command == "odd":
        if number % 2 != 0:
            filtered.append(number)

    elif command == "negative":
        if number < 0:
            filtered.append(number)
    elif command == "positive":
        if number >= 0:
            filtered.append(number)

print(filtered)

# vtori nachin
positive = list()
negative = list()
odd = list()
even = list()

for i in range(number_lines):
    current_number = int(input())
    if current_number % 2 == 0:
        even.append(current_number)
    else:
        odd.append(current_number)
    if current_number >= 0:
        positive.append(current_number)
    else:
        negative.append(current_number)

filter_word = input()
if filter_word == "even":
    print(positive)
if filter_word == "odd":
    print(odd)
if filter_word == "positive":
    print(positive)
if filter_word == "negative":
    print(negative)
# vmestp 4 if proverki za filter_word
print(eval(filter_word))

