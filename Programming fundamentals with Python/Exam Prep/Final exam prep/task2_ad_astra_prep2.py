import re

lines = input()
pattern = r"(#|\|)(?P<name>[A-Za-z\s]+)\1(?P<year>\d{2,2}/\d{2,2}/\d{2,2})\1(?P<calories>\d{1,5})\1"

result = re.finditer(pattern, lines)
total_cal = 0
list_foods = []

for match in result:
    list_foods.append([match.group("name"), match.group("year"), match.group("calories")])
    total_cal += int(match.group("calories"))

days = total_cal // 2000
print(f"You have food to last you for: {days} days!")

for match in list_foods:
    print(f"Item: {match[0]}, Best before: {match[1]}, Nutrition: {match[2]}")

#vtori nachin
info = input()
pattern = r"\#([a-z A-Z]+)\#(\d{2}\/\d{2}\/\d{2})\#(\d+)\#|\|([a-z A-Z]+)\|(\d{2}\/\d{2}\/\d{2})\|(\d+)\|"

result = re.findall(pattern, info)
items = []
calories = 0

for item in result:
    current_item = [el for el in item if el != ""]
    items.append(current_item)
    calories += int(current_item[2])

number_of_days = int(calories / 2000)

print(f"you have food {number_of_days}")

for data in items:
    product = data[0]
    date = data[1]
    current_calories = data[2]
    print(f"Item: {product}, Best before {data}, Nutrition {current_calories}")