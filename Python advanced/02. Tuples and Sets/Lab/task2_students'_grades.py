number = int(input())
students_grades = {}
student_strings = [input() for _ in range(number)]


def avg(value):
    return sum(value) / len(value)


for student_string in student_strings:
    student, grade_string = student_string.split(' ')
    grade = float(grade_string)
    if student not in students_grades:
        students_grades[student] = []

    students_grades[student].append(grade)

for students, grades in students_grades.items():
    grades_formatted = " ".join(f"{grade:.2f}" for grade in grades)
    average_grade = avg(grades)
    grades_avg_formatted = f"{average_grade:.2f}"
    print(f"{students} -> {grades_formatted} (avg: {grades_avg_formatted})")