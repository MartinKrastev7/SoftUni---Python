movie_name = input()
room_type = input()
number_tickets = int(input())
income = 0
ticket_price = 0

if room_type == "normal":
    if movie_name == "A Star Is Born":
        ticket_price = 7.50
        income = ticket_price * number_tickets
    elif movie_name == "Bohemian Rhapsody":
        ticket_price = 7.35
        income = ticket_price * number_tickets
    elif movie_name == "Green Book":
        ticket_price = 8.15
        income = ticket_price * number_tickets
    elif movie_name == "The Favourite":
        ticket_price = 8.75
        income = ticket_price * number_tickets
elif room_type == "luxury":
    if movie_name == "A Star Is Born":
        ticket_price = 10.50
        income = ticket_price * number_tickets
    elif movie_name == "Bohemian Rhapsody":
        ticket_price = 9.45
        income = ticket_price * number_tickets
    elif movie_name == "Green Book":
        ticket_price = 10.25
        income = ticket_price * number_tickets
    elif movie_name == "The Favourite":
        ticket_price = 11.55
        income = ticket_price * number_tickets
elif room_type == "ultra luxury":
    if movie_name == "A Star Is Born":
        ticket_price = 13.50
        income = ticket_price * number_tickets
    elif movie_name == "Bohemian Rhapsody":
        ticket_price = 12.75
        income = ticket_price * number_tickets
    elif movie_name == "Green Book":
        ticket_price = 13.25
        income = ticket_price * number_tickets
    elif movie_name == "The Favourite":
        ticket_price = 11.95
        income = ticket_price * number_tickets

print(f"{movie_name} -> {income:.2f} lv.")

