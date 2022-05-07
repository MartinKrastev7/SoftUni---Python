import re

participants = input().split(",")
no_spaces = [x.replace(" ", "") for x in participants]
participants_dict = {}

while True:
    info = input()

    if info == "end of race":
        break
    names = ""
    distances = ""
    name = r"[A-Za-z]+"
    distance = r"[0-9]"

    result_names = re.findall(name, info)
    result_distance = re.findall(distance, info)

    names += "".join(result_names)
    distances = sum(map(int, result_distance))

    if names in no_spaces:
        if names not in participants_dict.keys():
            participants_dict[names] = distances
        else:
            participants_dict[names] += distances


ordered_values = sorted(participants_dict.items(), key=lambda cp: -cp[1])

ordered_list = [x[0] for x in ordered_values]
print(f"1st place: {ordered_list[0]}")
print(f"2nd place: {ordered_list[1]}")
print(f"3rd place: {ordered_list[2]}")