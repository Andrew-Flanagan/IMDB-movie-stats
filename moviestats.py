#!/bin/env python3
import sys
import csv
import re
from directors import *



RATING = 1
TITLE = 3
RUNTIME = 7
YEAR = 8
GENRE = 9
DIRECTOR = 12



def main():
    data = read_file()                                                          # reads input CSV file prints error if not provided, returns data in data var
    process_data(data)

# read file passed in from command line
# CSV file is obtained from exporting IMDB ratings
def read_file():
    if(len(sys.argv)<2):                                                        #if no file is provided, return None and print error
        print("missing csv file")
        return None

    try:
        enc = 'unicode_escape'                                                  # read file, store data in file var
        file = csv.reader(open('imdbstats.csv', 'r',encoding = enc))
    except FileNotFoundError:
        print("Unable to open '"+ file +"' for reading.")
        return None

    data = []

    for line in file:                                                           # strip line of only important information, append it to data
        line = [line[RATING],line[TITLE],line[RUNTIME],line[YEAR],line[GENRE],line[DIRECTOR]]
        data.append(line)

    return data

def process_data(data):
    list_directors = []
    director_objects = []

    for line in data[1:]:
        if line[-1] not in list_directors and line[-1] != "":                   # if the director is not in our list of directors, add it to list of directors
            list_directors.append(line[-1])
            new_director = Director(line[-1])                                   # create director object
            director_objects.append(new_director)                               # append object to list of director objects
            new_director.add_movie(line[1])                                     # add movie from this director to director object
            new_director.add_rating(line[0])                                    # add rating for the movie

        else:
            for director in director_objects:                                   # if director is already in our list
                if director.get_director_name() == line[-1]:
                    director.add_movie(line[1])                                 # add movie and rating
                    director.add_rating(line[0])

    for director in director_objects:
        average = director.get_average()                                        # get the average of all movies from this director
        if len(director.movies)>=3 and average >= 4.20:                         # only care about director if seen 3 or more films from them and the average is above 4.20 (max of 5)
            print("Director: \t\t\t",director)                                  # print director name, num of movies seen, average rating, and list of movies
            print("Number of movies watched:\t",len(director.movies))
            print("Average Rating: \t\t " + "{:.2f}".format(average))
            print("Movies: ")
            for movies in director:
                print('-',movies)
            print()
            print("............................................................")
            print()



    print('You have watched: '+str(len(director_objects))+' distinct directors and a total of '+str(len(data))+' movies.')





















if __name__ == "__main__":
    main()
