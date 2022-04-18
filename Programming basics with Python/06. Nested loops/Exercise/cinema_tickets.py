is_finished = False
percent1 = 0
percent2 = 0
percent3 = 0
total = 0
count = 0
student_count = 0
kid_count = 0
standard_count = 0
left_spaces = 0
free_spaces = 0

while True:
    movie_name = input()
    if movie_name == "Finish":
        is_finished = True
        break

    free_spaces = int(input())
    left_spaces = 0
    while free_spaces > left_spaces:

        ticket_type = input()

        if ticket_type == "End":
            break
        count += 1
        left_spaces += 1
        if ticket_type == "student":
            student_count += 1

        elif ticket_type == "standard":
            standard_count += 1

        elif ticket_type == "kid":
            kid_count += 1

        percent1 = student_count * 100 / count
        percent2 = standard_count * 100 / count
        percent3 = kid_count * 100 / count
        total = left_spaces * 100 / free_spaces
    print(f"{movie_name} - {total:.2f}% full.")
if is_finished:
    print(f"Total tickets: {count}")
    print(f"{percent1:.2f}% student tickets.")
    print(f"{percent2:.2f}% standard tickets.")
    print(f"{percent3:.2f}% kids tickets.")
