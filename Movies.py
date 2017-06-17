import media
import json
import webbrowser
import urllib
import fresh_tomatoes


# Bad way to link movies with trailers
# should have used something like pairs in C++
list_of_movies = ['Martyrs',
                  'The Wolf Of Wall Street',
                  'The Dictator',
                  'The Godfather',
                  'Black Hawk Down',
                  'Hitman',
                  'The Godfather 2',
                  'The Godfather 3']
# Video links weren't there in the API response
# Ended up hard coding them instead
list_of_trailers = ['https://www.youtube.com/watch?v=-7Qx2dT-lUw',
                    'https://youtu.be/iszwuX1AK6A',
                    'https://youtu.be/cYplvwBvGA4',
                    'https://youtu.be/sY1S34973zA',
                    'https://youtu.be/tnV6wM-vd9s',
                    'https://youtu.be/xK3IzUrTTwk',
                    'https://youtu.be/OA1ij0alE0w',
                    'https://youtu.be/z8h3LVb8cl8']
# Using MoviesDB API! shoutout to the documentation it was well written
movie_objects_array = []

for x in range(0, 8):
    response = urllib.urlopen('https://api.themoviedb.org/3/search/movie?query=' + list_of_movies[x] + '&api_key=da172efbcdb23fcce45bf6bac42231fc')  # noqa
    # literally spent an hour figuring out why my response wouldn't show up
    #  Ended up learning a different way of digging through the response
    temp = media.Movie(json.loads(response.read()), list_of_trailers[x])  # noqa
    movie_objects_array.append(temp)

fresh_tomatoes.open_movies_page(movie_objects_array)
