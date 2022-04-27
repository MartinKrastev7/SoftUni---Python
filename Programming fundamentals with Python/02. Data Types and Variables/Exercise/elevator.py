import math

number_people_n = int(input())
capacity_p = int(input())

result = number_people_n / capacity_p

result = math.ceil(result)

print(result)