#string_f = input()

new_list = map(int, input().split(", "))

#lst_non0 = [x for x in new_list if x != 0]
#lst_0 = [x for x in new_list if x == 0]

#lst_zero_at_end = lst_non0 + lst_0
#print(lst_zero_at_end)

lst_non0 = []
lst_0 = []

for x in new_list:
    if x != 0:
        lst_non0.append(x)
    elif x == 0:
        lst_0.append(x)

lst_zero_at_end = lst_non0 + lst_0

print(lst_zero_at_end)