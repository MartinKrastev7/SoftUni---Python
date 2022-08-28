from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username, age):
        for user in self.users_collection:
            if user.username == username:
                raise Exception("User already exists!")
        user_made = User(username, age)
        self.users_collection.append(user_made)
        return f"{username} registered successfully."

    def upload_movie(self, username, movie: Movie):
        user_registered = [u for u in self.users_collection if u.username == username]
        if not user_registered:
            raise Exception("This user does not exist!")
        user_registered = user_registered[0]
        if user_registered.username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        movie_exists = [m for m in self.movies_collection if m.title == movie.title]
        if movie_exists:
            raise Exception(f"Movie already added to the collection!")
        self.movies_collection.append(movie)
        user_registered.movies_owned.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username, movie: Movie, **kwargs):
        user_registered = [u for u in self.users_collection if u.username == username]
        user_registered = user_registered[0]
        if user_registered.username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        movie_exists = [m for m in self.movies_collection if m.title == movie.title]
        if not movie_exists:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        for key, value in kwargs.items():
            if key == "title":
                movie.title = value
            elif key == "year":
                movie.year = value
            elif key == "age_restriction":
                movie.age_restriction = value
        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username, movie: Movie):
        user_registered = [u for u in self.users_collection if u.username == username]
        user_registered = user_registered[0]
        if user_registered.username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        movie_exists = [m for m in self.movies_collection if m.title == movie.title]
        if not movie_exists:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        #for film in self.movies_collection:
          #  if film.title == movie.title:
         #       self.movies_collection.remove(film)
        #for film in user_registered.movies_owned:
          #  if film.title == movie.title:
         #       user_registered.movies_owned.remove(film)
        self.movies_collection.remove(movie)
        user_registered.movies_owned.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username, movie: Movie):
        user_registered = [u for u in self.users_collection if u.username == username]
        user_registered = user_registered[0]
        if user_registered.username == movie.owner.username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        for film in user_registered.movies_liked:
            if film.title == movie.title:
                raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        user_registered.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username, movie: Movie):
        user_registered = [u for u in self.users_collection if u.username == username]
        user_registered = user_registered[0]

        movie_liked = [m for m in user_registered.movies_liked if m.title == movie.title]
        if not movie_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")
        movie_liked = movie_liked[0]

        movie.likes -= 1
        #user_registered.movies_liked.remove(movie_liked)
        user_registered.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        #sorted_elements = list(sorted(self.movies_collection, key=lambda a: (-a.year, a.title)))
        #self.movies_collection.sort(key=lambda a: (-a.year, a.title))
        result = ""
        if len(self.movies_collection) == 0:
            return "No movies found."
           # result += "No movies found."
        else:
            result_str = []
            for movie in sorted(self.movies_collection, key=lambda x: (-x.year, x.title)):
                result_str.append(movie.details())
            return '\n'.join(result_str)
            #for movie in sorted(self.movies_collection, key=lambda a: (-a.year, a.title)):
             #   result += movie.details() + '\n'
            #return result

    def __str__(self):
        result = ""
        if self.users_collection:
            all_users = []
            for user in self.users_collection:
                all_users.append(user.username)
            result += f"All users: {', '.join(all_users)}\n"
        else:
            result += "All users: No users.\n"

        if self.movies_collection:
            all_movies = []
            for movie in self.movies_collection:
                all_movies.append(movie.title)
            result += f"All movies: {', '.join(all_movies)}"
        else:
            result += "All movies: No movies."

        return result.strip()



