from project.movie_specification.movie import Movie


class Thriller(Movie):
    def __init__(self, title, year, owner, age_restriction=16):
        super().__init__(title, year, owner, age_restriction)

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        if value < 16:
            raise ValueError("Thriller movies must be restricted for audience under 16 years!")
        self.__age_restriction = value

    @property
    def type(self):
        return "Thriller"