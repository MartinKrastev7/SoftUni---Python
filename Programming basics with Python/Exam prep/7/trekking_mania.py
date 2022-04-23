number_groups = int(input())
group_1 = 0
group_2 = 0
group_3 = 0
group_4 = 0
group_5 = 0
total_people = 0
percent_1 = 0
percent_2 = 0
percent_3 = 0
percent_4 = 0
percent_5 = 0

for group in range(1,number_groups + 1):
    number_people = int(input())
    total_people += number_people
    if number_people <= 5:
        group_1 += number_people
    elif number_people < 13:
        group_2 += number_people
    elif number_people < 26:
        group_3 += number_people
    elif number_people < 41:
        group_4 += number_people
    elif number_people >= 41:
        group_5 += number_people
percent_1 = group_1 * 100 / total_people
percent_2 = group_2 * 100 / total_people
percent_3 = group_3 * 100 / total_people
percent_4 = group_4 * 100 / total_people
percent_5 = group_5 * 100 / total_people
print(f"{percent_1:.2f}%")
print(f"{percent_2:.2f}%")
print(f"{percent_3:.2f}%")
print(f"{percent_4:.2f}%")
print(f"{percent_5:.2f}%")


