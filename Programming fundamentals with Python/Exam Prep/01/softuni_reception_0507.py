employee_number_first = int(input())
employee_number_second = int(input())
employee_number_third = int(input())
students_count = int(input())

all_answers_per_hour = employee_number_first + employee_number_second + employee_number_third
#all_answered = False
hours_count = 0

while students_count > 0:
    hours_count += 1
    if hours_count % 4 == 0:
        continue
    students_count -= all_answers_per_hour
  #  if students_count <= 0:
   #     all_answered = True
    #    break


print(f"Time needed: {hours_count}h.")