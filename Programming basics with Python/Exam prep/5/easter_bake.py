import math
import sys

kozunakis_number = int(input())
total_sugar_needed = 0
total_flour_needed = 0
max_flour_used = -sys.maxsize
max_sugar_used = -sys.maxsize
number_packages_sugar = 0
number_packages_flour = 0

for bake in range(1, kozunakis_number + 1):
    sugar_used = int(input())
    flour_used = int(input())
    if sugar_used > max_sugar_used:
        max_sugar_used = sugar_used
    if flour_used > max_flour_used:
        max_flour_used = flour_used
    total_sugar_needed += sugar_used
    total_flour_needed += flour_used

number_packages_sugar = total_sugar_needed / 950
number_packages_flour = total_flour_needed / 750
number_packages_sugar = math.ceil(number_packages_sugar)
number_packages_flour = math.ceil(number_packages_flour)

print(f"Sugar: {number_packages_sugar}")
print(f"Flour: {number_packages_flour}")
print(f"Max used flour is {max_flour_used} grams, max used sugar is {max_sugar_used} grams.")
