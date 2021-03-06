"""
This module contains the code for creating Movie instances.
They are then added to a list and passed to open_movies_page() function
to create the html file and open it in a browser.
"""
import media
import fresh_tomatoes

# Create few instances of Movie class, which will be used by the website.
baahubali = media.Movie("Baahubali",
                        "The story of a man who discovers his past",
                        "https://i.ytimg.com/vi/pcl1r2qTla8/maxresdefault.jpg",
                        "https://www.youtube.com/watch?v=3NQRhE772b0")

inception = media.Movie("Inception",
                        "A con artist tries to create a dream within a dream within a dream!",
                        "https://trailers.apple.com/trailers/wb/inception/images/poster-large.jpg",
                        "https://www.youtube.com/watch?v=YoHD9XEInc0")

shawshank_redemption = media.Movie("Shawshank Redemption",
                                   "A prisonser escapes from a prison and"
                                   " fills hope in a friend in the process",
                                   "http://ia.media-imdb.com/images/M/MV5BNjQ2NDA3MDcxMF5BMl5BanBnXkFtZTgwMjE5NTU0NzE@._V1_.jpg",  # NOQA
                                   "https://www.youtube.com/watch?v=6hB3S9bIaco")

oceans_eleven = media.Movie("Ocean's Eleven",
                            "A group of eleven people plan and rob a casino",
                            "https://images-na.ssl-images-amazon.com/images/I/51HNXQS7Q1L._SY300_.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=imm6OR605UI")

toy_story = media.Movie("Toy Story",
                        "The story of a young boy and his toys",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

# Add all the above movie instances to a list.
movies_list = [baahubali,
               inception,
               shawshank_redemption,
               oceans_eleven,
               toy_story,
               avatar]

# Pass the movies list as an argument to open_movies_page function in the fresh_tomatoes module.
fresh_tomatoes.open_movies_page(movies_list)
