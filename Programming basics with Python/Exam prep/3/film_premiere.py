movie_name = input()
movie_packet = input()
tickets_number = int(input())

price = 0

if movie_name == "John Wick":
    if movie_packet == "Drink":
        price = 12 * tickets_number
    elif movie_packet == "Popcorn":
        price = 15 * tickets_number
    elif movie_packet == "Menu":
        price = 19 * tickets_number
elif movie_name == "Star Wars":
    if movie_packet == "Drink":
        price = 18 * tickets_number
    elif movie_packet == "Popcorn":
        price = 25 * tickets_number
    elif movie_packet == "Menu":
        price = 30 * tickets_number
    if tickets_number >= 4:
        price *= 0.70
elif movie_name == "Jumanji":
    if movie_packet == "Drink":
        price = 9 * tickets_number
    elif movie_packet == "Popcorn":
        price = 11 * tickets_number
    elif movie_packet == "Menu":
        price = 14 * tickets_number
    if tickets_number == 2:
        price *= 0.85
print(f"Your bill is {price:.2f} leva.")

