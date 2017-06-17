import json


class Movie:
    """ This clas contains basic info about movies """
    def __init__(self, response, youtube_url):
                self.title = str(response['results'][0]['title'])
                self.storyline = str(response['results'][0]['overview'])
                self.poster_image_url = 'http://image.tmdb.org/t/p/w342/' + str(str(response['results'][0]['poster_path']))  # noqa
                self.trailer_youtube_url = youtube_url
