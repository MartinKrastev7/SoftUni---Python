number = int(input())
combination = 0

for n1 in range(number + 1):
    for n2 in range(number + 1):
        for n3 in range(number + 1):
            if n1 + n2 + n3 == number:
                combination += 1
print(combination)