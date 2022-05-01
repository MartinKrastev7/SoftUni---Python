numbers = input().split(" ")
new_list = []
for i in numbers:
    new_num = float(i)
    new_num = abs(new_num)
    new_list.append(new_num)

print(new_list)