junior_number = int(input())
senior_number = int(input())
trace = input()
tax = 0

if trace == "trail":
    tax = (5.50 * junior_number) + (7 * senior_number)
elif trace == "cross-country":
    tax = (8 * junior_number) + (9.50 * senior_number)
    total_participants = junior_number + senior_number
    if total_participants >= 50:
        tax = tax - (tax * 0.25)
elif trace == "downhill":
    tax = (12.25 * junior_number) + (13.75 * senior_number)
elif trace == "road":
    tax = (20 * junior_number) + (21.50 * senior_number)

expense = tax * 0.05
diff = tax - expense

print(f"{diff:.2f}")