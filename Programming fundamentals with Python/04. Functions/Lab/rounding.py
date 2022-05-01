numbers = input().split(" ")
new_list = []

for i in numbers:
    new_item = float(i)
    new_item = round(new_item)
    new_list.append(new_item)

print(new_list)

# vtori nachin s funkciq
def convert_list_to_round(base_list):
    final_list = list()
    for n in base_list:
        final_n = round(float(n))
        final_list.append(final_n)
    return final_list


input_list = input().split(" ")
print(convert_list_to_round(input_list))