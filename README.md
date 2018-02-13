# Movie-Trailer-Project 

A simple movie trailer website project for Udacity's full-stack [nanodegree program](https://www.udacity.com/nanodegree). The project demonstrates the use of a Movie object class in Python to generate a static webpage, which displays a listing of favorite movies and links each movie to its trailers video on YouTube. The project also includes some CSS and jQuery involved in the display of the webpage. 

## Table of contents

- [Download](#download)
- [Quick start](#quick-start)
- [Documentation](#documentation)


## Download

The files for the project, may be [downloaded here](https://github.com/vishalverma007/udacity-movie-website).

## Quick Start

After downloading the project files, a movie trailer page can be created by importing [movies.py](https://github.com/vishalverma007/udacity-movie-website/blob/master/movies.py) and [fresh_tomatoes.py](https://github.com/vishalverma007/udacity-movie-website/blob/master/fresh_tomatoes.py) at the start of your Python script. Then create idividual Movie objects by calling movies.Movie() and supplying it with four arguments -- title, year, poster_url, and trailer_url. Lastly, to generate the movie trailers page, call fresh_tomatoes.open_movies_page() and supply it with an array of the movie objects you created. 

```
import media
import fresh_tomatoes

#information for object arguments
title = "Jurassic park"
year = 1994
poster_url = "https://upload.wikimedia.org/wikipedia/en/e/e7/Jurassic_Park_poster.jpg"
trailer = "https://www.youtube.com/watch?v=_IesovZQR4g"

# Create Movie object
jurassic_park = movies.Movie(title, year, poster_image_url, trailer_youtube_url)

# Create movie trailer page with array of one movie
fresh_tomatoes.open_movies_page([jurassic_park])

```

A more detailed example with multiple movie objects, which is used for the [demo](https://github.com/vishalverma007/udacity-movie-website/blob/master/fresh_tomatoes.html), can be found in [entertainment_center.py](https://github.com/vishalverma007/udacity-movie-website/blob/master/entertainment_center.py) 


### What's included

Within the download you'll find the following directories and files:

```
udacity-movie-website-master.zip/
├── entertainment_center.py
├── fresh_tomatoes.html
├── fresh_tomatoes.py
├── movies.py
└── README.md
```

## Documentation

### Movie object class

The Movie object class consists of four class variables, a simple constructor method, and a class method for playing a Movie object's movie trailer. The code is located in [movies.py](https://github.com/vishalverma007/udacity-movie-website/blob/master/movies.py). 

##### constructor method

The constructor method is called when a new Movie object is created and must include four arguments -- [title](#movietitle), [year](#movieyear), [poster_image_url](#movieposter_url), and [trailer_youtube_url](#movietrailer_url). Each of these arguments is discussed further below.

```
import media

#information for object arguments
title = "Jurassic park"
year = 1994
poster_url = "https://upload.wikimedia.org/wikipedia/en/e/e7/Jurassic_Park_poster.jpg"
trailer = "https://www.youtube.com/watch?v=_IesovZQR4g"

# Create Movie object
jurassic_park = movies.Movie(title, year, poster_url, trailer_url)
```

###### movie.title

movie.title is any string used to identify the movie object.

###### movie.year

movie.year is an string representing the year the movie was released. 

###### movie.poster_image_url

movie.poster_image_url is a string containing a URL linking to an image which will be used to represent the Movie object, such as a movie poster or DVD box cover. The movie trailer page portion of this project displays these images with a width of 188px and a height of 292px. So, images with a ratio of 1:1.5 will work best. 

###### movie.trailer_youtube_url

movie.trailer_youtube_url is a string containing a URL linking to the movie trailer on YouTube.com. The movie trailer page portion of the this project extracts the YouTube id from the URL, so while links to other video services are valid in the Movie class object, they will not work with the movie trailers page. 

##### show_trailer method

show_trailer can be called on any Movie class object to launch that object's movie trailer in a webpage. This method is useful for testing but is not used by the script that generates the finished movie trailers page.

### Movie Trailer Page Functions 

The functions used to create the final movie trailers page are located in [fresh_tomatoes.py](https://github.com/vishalverma007/udacity-movie-website/blob/master/movies.py), along with HTML template variables used by these functions. This file must be imported to access the functions described below.

#### open_movies_page function

To create the static movie trailers page the open_movies_page function must be called and supplied with one required argument (an array of Movie class objects).
```
# Create movie trailer page with array of Movie class objects
fresh_tomatoes.open_movies_page([movie1, movie2, movie3])


#### create_movie_tiles_content

The create_movie_tiles_content function is called by the open_movies_page function. It takes the array of Movie class objects as an argument and iterates through each Movie object and applies the object's data to the portion of the HTML template for each movie. While iterating through each object's class variables, it extracts the YouTube id from movie.trailer_url.





