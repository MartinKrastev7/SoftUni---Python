n = int(input())
sum_of_letter = 0

for i in range(1, n + 1):
    letter = input()
    sum_of_letter += ord(letter)

print(f"The sum equals: {sum_of_letter}")