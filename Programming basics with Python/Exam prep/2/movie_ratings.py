import sys
movies_number = int(input())
average_rating = 0
max_rating = -sys.maxsize
min_rating = sys.maxsize
max_movie = ""
min_movie = ""
rating = 0
for _ in range(1, movies_number + 1):
    movie_name = input()
    movie_rating = float(input())
    average_rating += movie_rating
    if movie_rating > max_rating:
        max_rating = movie_rating
        max_movie = movie_name
    if movie_rating < min_rating:
        min_rating = movie_rating
        min_movie = movie_name
rating = average_rating / movies_number
print(f"{max_movie} is with highest rating: {max_rating:.1f}")
print(f"{min_movie} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {rating:.1f}")
