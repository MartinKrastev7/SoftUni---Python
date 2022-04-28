number_lines = int(input())
positive_numbers = []
negative_numbers = []

positive_count = 0
negative_sum = 0

for i in range(number_lines):
    current_number = int(input())

    if current_number >= 0:
        positive_count += 1
        positive_numbers.append(current_number)
    else:
        negative_sum += current_number
        negative_numbers.append(current_number)

print(positive_numbers)
print(negative_numbers)
print(f"Count of positives: {positive_count}")
print(f"Sum of negatives: {negative_sum}")
# vtori nachin za count i sum bez broqch i promenliva
#print(f"Count of positives:{len(positive_numbers)}. Sum of negatives: {sum(negative_numbers)}}
