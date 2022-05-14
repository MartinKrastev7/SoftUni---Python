price_rating = list(map(int, input().split(", ")))
entry_point = int(input())
type_of_items = input()

left_side = price_rating[:entry_point]
right_side = price_rating[entry_point + 1:]
sum_left = 0
sum_right = 0
left_numbers = []
right_numbers = []

if type_of_items == "cheap":
    for i in left_side:
        if i < price_rating[entry_point]:
            left_numbers.append(i)

    for i in right_side:
        if i < price_rating[entry_point]:
            right_numbers.append(i)

elif type_of_items == "expensive":
    for i in left_side:
        if i >= price_rating[entry_point]:
            left_numbers.append(i)

    for i in right_side:
        if i >= price_rating[entry_point]:
            right_numbers.append(i)


sum_left = sum(left_numbers)
sum_right = sum(right_numbers)

if sum_left > sum_right or sum_left == sum_right:
    print(f"Left - {sum_left}")
else:
    print(f"Right - {sum_right}")



