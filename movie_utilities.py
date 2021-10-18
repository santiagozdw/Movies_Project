class Movie:
    def __init__(self, movie_id, title, poster_url):
        self.movie_id = movie_id
        self.title = title
        self.poster_url = poster_url
    def __repr__(self):
        return f'Movie({self.movie_id}, {self.title}, {self.poster_url})'

class Genre:
    def __init__(self, genre):
        self.id = genre['id']
        self.name = genre['name']
    def __repr__(self):
        return f'Genre({self.id}, {self.name})'
    
class MovieDetail:
    def __init__(self, title, tagline, poster_url, overview, budget, genres):
        genre_list = []
        self.title = title
        self.tagline = tagline
        self.poster_url = poster_url
        self.overview = overview
        self.budget = budget
        for item in genres:
            genre_list.append(Genre(item))
        self.genres = genre_list

class Actor:
    def __init__(self, actor_id, name, character, profile_path):
        self.actor_id = actor_id
        self.name = name
        self.character = character
        self.profile_path = profile_path
    def __repr__(self):
        return f'Actor({self.name})'

def get_movie_info(movie):
    return Movie(movie['id'], movie['original_title'], movie['poster_path'])

def get_movie_detail(movie):
    return MovieDetail(movie['title'], movie['tagline'], movie['backdrop_path'], movie['overview'],
                      movie['budget'], movie['genres'])

def get_movie_cast(movie_cast):
    actors = []
    for actor in movie_cast:
        actors.append(Actor(actor['id'], actor['name'], actor['character'], actor['profile_path']))
    return actors
