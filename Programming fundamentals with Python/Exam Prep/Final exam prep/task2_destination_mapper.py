import re

locations = input()
locations_pattern = r"(=|\/)(?P<destination>[A-Z][A-Za-z]{2,})\1"
result = re.finditer(locations_pattern, locations)
length = 0
list_destinations = []
for match in result:
    destinations = "".join(match.group('destination'))
    list_destinations.append(match.group('destination'))
    length += len(match.group('destination'))


print(f'Destinations: {", ".join(list_destinations)}')
print(f"Travel Points: {length}")

#vtori nachin
text = input()
regex = r"([=/\])([A-Z][A-Za-z]{2,})\1"

matches = re.finditer(regex, text)
locations = []
points = 0

for match in matches:
    city = match[2]
    locations.append(city)
    points += len(city)

output = ", ".join(locations)
print(f"Destinations: {output}")
print(f"Travel Points {points}")



