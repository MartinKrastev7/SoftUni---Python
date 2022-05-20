numbers_string = input()
numbers = [float(x) for x in numbers_string.split(" ")]
occurrences_count = {}

for number in numbers:
    #if number in occurrences_count:
     #   occurrences_count[number] += 1
    #else:
     #   occurrences_count[number] = 1
    if number not in occurrences_count:
        occurrences_count[number] = 0
    occurrences_count[number] += 1

for number, count in occurrences_count.items():
    print(f"{number:.1f} - {count} times")




