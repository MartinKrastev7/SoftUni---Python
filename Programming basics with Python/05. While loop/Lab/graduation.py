name = input()
grades = 1
sum_grades = 0.0
excluded = 0
grade = 0

while grades <= 12:
    grade = float(input())

    if grade < 4:
        excluded += 1
        if excluded > 1:
            print(f"{name} has been excluded at {grades} grade")
            break
        continue
    else:
        grades += 1
        sum_grades += grade
    if grades > 12:
        average = sum_grades / 12
        print(f"{name} graduated. Average grade: {average:.2f}")

