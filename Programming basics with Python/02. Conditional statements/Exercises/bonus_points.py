number = int(input())
bonus = 0

if number < 100:
    bonus = 5
elif number > 1000:
    bonus = number * 10 / 100
else:
    bonus = number * 20 / 100

if number % 2 == 0:
    bonus = bonus + 1
elif number % 10 == 5:
    bonus = bonus + 2

print(bonus)
print(bonus + number)
