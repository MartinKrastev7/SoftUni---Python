people_phone = []
while len(people_phone) > 2:
    inp = input()
    if inp == "":
        break
    people_phone.append(inp)



phone_book = {}

for i in range(0, len(people_phone), 2):
    name = people_phone[i]
    phone = people_phone[i + 1]
    phone_book[name] = phone

count = int(input())
for i in range(1, count + 1):
    name = input()
    if name in phone_book:
        for key, value in phone_book.items():
            print(f"{key} -> {value}")
    else:
        print(f"Contact {name} does not exist.")


#vtori nachin
def phone_book_information(number_of_lines, phone_book):
    for x in range(number_of_lines):
        name = input()
        if name not in phone_book:
            print(f"Contact {name} does not exist.")
        else:
            print(f"{name} -> {phone_book[name]}")

    return True


def phonebook_info():
    phone_book = {}
    condition = False

    while True:
        contact_information = input().split("-")

        if contact_information[0].isdigit():
            condition = phone_book_information(int(contact_information[0]), phone_book)
        else:
            phone_book[contact_information[0]] = contact_information[1]

        if condition:
            break


phonebook_info()