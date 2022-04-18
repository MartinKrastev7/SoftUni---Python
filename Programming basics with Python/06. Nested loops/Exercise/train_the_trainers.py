average_grade = 0
is_finished = False
count = 0
number_in_jury = int(input())
while True:

    presentation_name = input()
    if presentation_name == "Finish":
        is_finished = True
        break
    number_grade = 1
    average_current_grade = 0
    while number_grade <= number_in_jury:
        current_grade = float(input())
        count += 1
        number_grade += 1

        average_grade += current_grade
        average_current_grade += current_grade
    average_current_grade /= number_in_jury
    print(f"{presentation_name} - {average_current_grade:.2f}.")


average_grade /= count
if is_finished:
    print(f"Student's final assessment is {average_grade:.2f}.")




