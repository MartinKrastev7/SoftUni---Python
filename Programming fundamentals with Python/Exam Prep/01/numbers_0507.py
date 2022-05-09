numbers = list(map(int, input().split(" ")))
sum_numbers = sum(numbers)
average = sum_numbers / len(numbers)
new_numbers = []
is_true = False
for i in numbers:
    if i > average:

        new_numbers.append(i)
        is_true = True


new_numbers.sort(reverse=True)
while len(new_numbers) > 5:
    new_numbers.pop()

if is_true:
    print(*new_numbers)
else:
    print("No")