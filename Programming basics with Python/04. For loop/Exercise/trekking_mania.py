group_number = int(input())
row1 = 0
row2 = 0
row3 = 0
row4 = 0
row5 = 0
total_people = 0

for i in range(group_number):
    people_in_group = int(input())
    total_people += people_in_group
    if people_in_group <= 5:
        row1 += people_in_group
    elif people_in_group < 13:
        row2 += people_in_group
    elif people_in_group < 26:
        row3 += people_in_group
    elif people_in_group < 41:
        row4 += people_in_group
    else:
        row5 += people_in_group

row1 = row1 / total_people * 100
row2 = row2 / total_people * 100
row3 = row3 / total_people * 100
row4 = row4 / total_people * 100
row5 = row5 / total_people * 100

print(f"{row1:.2f}%")
print(f"{row2:.2f}%")
print(f"{row3:.2f}%")
print(f"{row4:.2f}%")
print(f"{row5:.2f}%")
