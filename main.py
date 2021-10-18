from flask import Flask, render_template, request
import requests
import tmdb_client
import movie_utilities
import random

app = Flask(__name__)

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}

@app.route('/')
def homepage():
    selected_list = request.args.get('selected_list', "popular")
    movies = []
    print(selected_list)
    movies_raw = tmdb_client.get_movies(selected_list, 20) 
    movie_lists = ['popular', 'top_rated', 'upcoming', 'now_playing']
    for movie in movies_raw:
        movies.append(movie_utilities.get_movie_info(movie))
    return render_template("filmy.html", movies = random.sample(movies, 8), movie_lists = movie_lists, current_list = selected_list)

@app.route('/film/<movie_id>')
def film(movie_id):
    movie = movie_utilities.get_movie_detail(tmdb_client.get_single_movie(movie_id))
    actors = movie_utilities.get_movie_cast(tmdb_client.get_single_movie_credits(movie_id)['cast'])
    pictures = tmdb_client.get_single_movie_images(movie_id)['backdrops']
    return render_template("film.html", movie = movie, actors = actors, picture = random.sample([picture['file_path'] for picture in pictures], 1)[0])

if __name__ == '__main__':
    app.run(debug=True)