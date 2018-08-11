import csv
from collections import defaultdict, namedtuple, Counter

MOVIE_DATA = 'movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    directors = defaultdict(list)
    with open (MOVIE_DATA, encoding='utf8') as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue

            m = Movie(title=movie, year=year, score=score)
            directors[director].append(m)
    return directors
    '''Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)'''
    pass


def get_average_scores(directors):
    #create tuple with director, number of films & average score
    director_score = namedtuple('Director', 'number_of_films score')
    director_list = defaultdict(list)
    for director, movies in directors.items():
        number_of_films = 0
        total_score = 0
        for movies in movies:
            number_of_films += 1
            total_score += movies.score
        m = director_score(number_of_films=number_of_films, score=total_score)
        director_list[director].append(m)

    minimum_filter = 3
    print(director_list)
    for director, score in director_list.items():
        for item in score:
            if item.number_of_films > minimum_filter:
                print(director + str(item.score))





    '''Filter directors with < MIN_MOVIES and calculate averge score'''
    pass


def _calc_mean(movies):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    pass


def print_results(directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    fmt_director_entry = '{counter}. {director:<52} {avg}'
    fmt_movie_entry = '{year}] {title:<50} {score}'
    sep_line = '-' * 60


def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    directors = get_movies_by_director()
    directors = get_average_scores(directors)
    print_results(directors)


if __name__ == '__main__':
    main()
