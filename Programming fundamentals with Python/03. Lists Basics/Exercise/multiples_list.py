number_factor = int(input())
number_count = int(input())
my_list = []

#my_list.append(number_factor)
new_value = 0

for i in range(1, number_count + 1):
    new_value = number_factor * i
    my_list.append(new_value)

print(my_list)

#vtoro reshenie
num1 = int(input())
num2 = int(input())
new_list = []

for num in range(1, num2 + 1):
    new_list.append(num * num1)
print(new_list)
