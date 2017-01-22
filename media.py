"""
This module defines the Movie class.
"""

import webbrowser

class Movie():
    """
    The movie class defines the instance variables and methods for each movie instance.
    """
    def __init__(self, title, storyline, poster_url, trailer_url):
        self.title = title
        self.storyline = storyline
        self.poster_url = poster_url
        self.trailer_url = trailer_url
