movie_name = input()
days = int(input())
number_tickets = int(input())
ticket_price = float(input())
percent_cinema = int(input())

sum_from_tickets = number_tickets * ticket_price
income_for_whole_period = days * sum_from_tickets
income_cinema = (percent_cinema * income_for_whole_period) / 100
profit = income_for_whole_period - income_cinema
print(f"The profit from the movie {movie_name} is {profit:.2f} lv.")
