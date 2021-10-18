import requests

api_key = '55d81b105352eeb4e7c14ecca6199eaa'
api_token = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NWQ4MWIxMDUzNTJlZWI0ZTdjMTRlY2NhNjE5OWVhYSIsInN1YiI6IjYxNjkzZjhiOTI0Y2U2MDAyNDdlMWEwYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.7T5vPcjeKNHUoMwDHPdLU16chkeptVNkXLTjEjD9Lnw'

def get_movies(list_name, how_many):
    data = get_listed_movies(list_name)
    return data["results"][:how_many]

def get_listed_movies(list_name):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_name}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_movie_info(movie):
    return Movie(movie['id'], movie['original_title'], movie['poster_path'])

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_single_movie_credits(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_single_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()