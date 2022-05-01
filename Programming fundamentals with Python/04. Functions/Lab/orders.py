product = input()
quantity = int(input())


def calculate(a, b):
    result = 0
    if a == "coffee":
        result = 1.50 * b
    elif a == "coke":
        result = 1.40 * b
    elif a == "water":
        result = 1.00 * b
    elif a == "snacks":
        result = 2.00 * b
    return result


print(f"{calculate(product,quantity):.2f}")