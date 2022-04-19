busy_places = 0
student_tickets = 0
standard_tickets = 0
kids_tickets = 0
percent1 = 0
percent2 = 0
percent3 = 0
is_finished = False
total_tickets = 0
total_percent = 0

while True:
    movie_name = input()
    if movie_name == "Finish":
        is_finished = True
        break
    free_spaces = int(input())
    busy_places = 0
    while free_spaces > busy_places:
        ticket_type = input()
        if ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kids_tickets += 1
        elif ticket_type == "End":
            break
        busy_places += 1
        total_tickets += 1
    total_percent = busy_places * 100 / free_spaces
    print(f"{movie_name} - {total_percent:.2f}% full.")

percent1 = student_tickets * 100 / total_tickets
percent2 = standard_tickets * 100 / total_tickets
percent3 = kids_tickets * 100 / total_tickets
if is_finished:
    print(f"Total tickets: {total_tickets}")
    print(f"{percent1:.2f}% student tickets.")
    print(f"{percent2:.2f}% standard tickets.")
    print(f"{percent3:.2f}% kids tickets.")

