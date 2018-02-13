#!/usr/local/bin/python
import movies
import fresh_tomatoes

"""
Favorite movies object with 4 args each:
title (movie's title)
year (year movie was released)
poster_url (url to poster image)
"""

jurassic_park = movies.Movie("Jurassic park",
                            "15 April 1994",
                            "https://upload.wikimedia.org/wikipedia/"
                            "en/e/e7/Jurassic_Park_poster.jpg",
                            "https://www.youtube.com/watch?v=_IesovZQR4g")

time_bandits = movies.Movie("Time Bandits",
			    "10 July 1981",
			    "http://goo.gl/yndMxB",
			    "https://www.youtube.com/watch?v=JwnjENpIyq0")

fight_club = movies.Movie("Fight Club",
			  "21 Sep 1999",
			  "http://goo.gl/BR5nIh",
		          "https://www.youtube.com/watch?v=SUXWAEX2jlg")

interstellar = movies.Movie("Interstellar",
                            "7 Nov 2014",
                            "https://upload.wikimedia.org/wikipedia/"
                            "en/b/bc/Interstellar_film_poster.jpg",
                            "https://www.youtube.com/watch?v=zSWdZVtXT7E")

lego_movie = movies.Movie("The Lego Movie",
                         "7 Feb 2014",
                         "https://upload.wikimedia.org/wikipedia/"
                         "en/1/10/The_Lego_Movie_poster.jpg",
                         "https://www.youtube.com/watch?v=fZ_JOBCLF-I")

grudge_match = movies.Movie("Grudge Match",
                           "25 Dec 2013",
                           "http://upload.wikimedia.org/wikipedia/"
                           "en/4/4a/Grudge_Match_Poster.jpg",
                           "https://www.youtube.com/watch?v=1bQSOBJCPQE")

#Create list of favourite movies 
movies_list = [jurassic_park, time_bandits, fight_club, interstellar, lego_movie, grudge_match];

#Call movie trailer page method and pass movies list
fresh_tomatoes.open_movies_page(movies_list);


