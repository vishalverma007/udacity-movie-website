#!/usr/local/bin/python
import webbrowser
class Movie:
	"""This class provides a way to store movie related information."""
	def __init__(self,movie_title,movie_year,poster_image,trailer_youtube):
		""" Constructor for Movie class with arguments: 
		title = Movie's title
		year = Year of the movie's release
		poster_url = URL to the poster image
		trailer_url = Youtube URL of the movie's trailer
        	"""
		self.title = movie_title;
		self.year = movie_year;
		self.poster_image_url = poster_image;
		self.trailer_youtube_url = trailer_youtube;

	def show_trailer(self):
		"""Opens trailer in a web browser """
		webbrowser.open(self.trailer_youtube);


