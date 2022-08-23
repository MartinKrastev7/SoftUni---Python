import os

from project.utils.validators import validate_non_empty_string, validate_greater_than_value


class User:
  #  MIN_USERNAME_LENGTH = 1
    MIN_AGE = 6

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
        self.__validate_username(value)
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__validate_age(value)
        self.__age = value

    @staticmethod
    def __validate_username(username):
        validate_non_empty_string(username, "Invalid username!")
     #   if username is not str or len(username) < self.MIN_USERNAME_LENGTH:
      #      raise ValueError("Invalid username!")

    def __validate_age(self, age):
        validate_greater_than_value(age, self.MIN_AGE, f"Users under the age of {self.MIN_AGE} are not allowed!" )
        #if age is not int or age < self.MIN_AGE:
         #   raise ValueError("Users under the age of 6 are not allowed!")



    def __str__(self):
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


