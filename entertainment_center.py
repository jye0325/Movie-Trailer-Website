import fresh_tomatoes
import media


# The first instance, terminator_2, instantiated with arguments:
# movie_title, poster_image, and trailer_youtube
terminator_2 = media.Movie(
    "Terminator 2",
    "https://upload.wikimedia.org/wikipedia/en/8/85/Terminator2poster.jpg",
    "https://www.youtube.com/watch?v=VVZQ39i5G1s")

# The second instance, inception, instantiated with arguments:
# movie_title, poster_image, and trailer_youtube
inception = media.Movie(
    "Inception",
    "https://upload.wikimedia.org/wikipedia/en/2/2e/" +
    "Inception_%282010%29_theatrical_poster.jpg",
    "https://www.youtube.com/watch?v=W7OTkEY1tMI")

# The third instance, batman, instantiated with arguments:
# movie_title, poster_image, and trailer_youtube
batman = media.Movie(
    "The Dark Knight",
    "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
    "https://www.youtube.com/watch?v=_PZpmTj1Q8Q")

# An array that holds location the the three instances in memory.
movies = [terminator_2, inception, batman]

# This function call passes a list of movie instances called "movies" as input
# to generate an HTML file. This file is then opened in your default web
# browser, and can be re-accessed in the future.
fresh_tomatoes.open_movies_page(movies)
