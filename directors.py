class Director ():

    unique_directors = 0
    def __init__(self,name):
        self.name = name
        self.movies = []
        self.ratings = 0
        self.average = 0

        self.__class__.unique_directors += 1

    def add_movie(self,movie_name):
        self.movies.append(movie_name)

    def get_average(self):
        return (self.ratings/len(self.movies))/2

    def add_rating(self,rating):
        self.ratings += int(rating)

    def __str__(self):
        return self.name

    def __len__(self):
        return self.__class__.unique_directors

    def get_director_name(self):
        return self.name

    def __iter__(self):
        for movie in self.movies:
            yield movie
