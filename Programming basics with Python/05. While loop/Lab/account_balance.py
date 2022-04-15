balance = 0

while True:
    numbers = input()

    if numbers == "NoMoreMoney":
        break
    elif float(numbers) < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {float(numbers):.2f}")
    balance += float(numbers)


print(f"Total: {balance:.2f}")