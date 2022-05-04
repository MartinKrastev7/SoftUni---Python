pair_of_rows = int(input())
students_dict = {}

for i in range(1, pair_of_rows + 1):
    name = input()
    grade = float(input())

    if name not in students_dict.keys():
        students_dict[name] = [grade]
    else:
        students_dict[name].append(grade)

for key, value in students_dict.items():
    students_dict[key] = sum(value) / len(value)

for name in students_dict:
    grade = students_dict[name]
    if grade >= 4.50:
        print(f"{name} -> {grade:.2f}")
