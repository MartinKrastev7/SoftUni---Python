information = input()
students_dict = {}

while information != "end":
    information = information.split(" : ")
    course_name = information[0]
    student_name = information[1]

    if course_name not in students_dict.keys():
        students_dict[course_name] = [student_name]
    else:
        students_dict[course_name].append(student_name)

    information = input()

for key, item in students_dict.items():
    print(f"{key}: {len(item)}")

    for student_name in item:
        print(f"-- {student_name}")