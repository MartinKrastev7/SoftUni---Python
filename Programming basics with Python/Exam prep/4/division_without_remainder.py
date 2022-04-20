n = int(input())
p1 = 0
p2 = 0
p3 = 0
count_2 = 0
count_3 = 0
count_4 = 0

for number in range(1, n + 1):
    number_in = int(input())

    if number_in % 2 == 0:
        count_2 += 1
    if number_in % 3 == 0:
        count_3 += 1
    if number_in % 4 == 0:
        count_4 += 1

p1 = count_2 * 100 / n
p2 = count_3 * 100 / n
p3 = count_4 * 100 / n

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")