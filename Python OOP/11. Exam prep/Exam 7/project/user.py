import os


class User:
    def __init__(self, username, age):
        self.username = username
        self.age = age
        self.movies_liked = []
        self.movies_owned = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if value == "":
            raise ValueError("Invalid username!")
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 6:
            raise ValueError("Users under the age of 6 are not allowed!")
        self.__age = value

    def __str__(self):
        #result = f"Username: {self.username}, Age: {self.age}\n"
        #result += f"Liked movies:\n"
        #if not self.movies_liked:
         #   result += "No movies liked.\n"
        #else:
          #  for liked in self.movies_liked:
         #       result += liked.details() + '\n'
        #if not self.movies_owned:
         #   result += "No movies owned.\n"
        #else:
        #    for owned in self.movies_owned:
       #         result += owned.details() + '\n'

      #  return result
        liked_movies = "No movies liked."
        if self.movies_liked:
            liked_movies = os.linesep.join(m.details() for m in self.movies_liked)

        owned_movies = "No movies owned."
        if self.movies_owned:
            owned_movies = os.linesep.join(m.details() for m in self.movies_owned)

        return f'''Username: {self.username}, Age: {self.age}
Liked movies: 
{liked_movies}  
Owned movies:
{owned_movies}'''