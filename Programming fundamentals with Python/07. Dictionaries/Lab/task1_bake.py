elements = input().split(" ")
bakery = {}

for i in range(0, len(elements), 2):
    key = elements[i]
    value = elements[i + 1]
    bakery[key] = int(value)

print(bakery)

#vtori nachin
data = input().split(" ")
bakery = {}

for i in range(0, len(data), 2):
    food = data[i]
    quantity = data[i + 1]
    bakery[food] = quantity