import webbrowser


class Movie():
    def __init__(self, movie_title, poster_image,
                 trailer_youtube):
        """This class is designed to take the arguments movie_title,
poster_image, and trailer_youtube as properties for it's
        corresponding instances.
        """
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """This class also defines the show_trailer function that allows users
        to display the trailer of its corresponding movie that was clicked on.
        """
        webbrowser.open(self.trailer_youtube_url)
