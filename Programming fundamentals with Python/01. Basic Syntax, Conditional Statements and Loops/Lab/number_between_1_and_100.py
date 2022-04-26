n = float(input())
is_valid = False

while not is_valid:
    if 1 <= n <= 100:
        is_valid = True
        break
    n = float(input())

if is_valid:
    print(f"The number {n} is between 1 and 100")

#vtoro reshenie
while number < 1 or number > 100:
    number = float(input())
print(number)