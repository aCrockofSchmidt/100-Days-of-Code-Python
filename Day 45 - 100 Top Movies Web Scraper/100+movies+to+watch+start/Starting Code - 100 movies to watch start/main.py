import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# obtain data from website

response = requests.get(URL)
movie_data = response.text

# import to Beautiful Soup object

soup = BeautifulSoup(movie_data, "html.parser")

# create list of movie titles

top_100_movies = []

for movie in soup.find_all(name="h3", class_="title"):
    top_100_movies.insert(0, movie.getText())

# create txt file of all movies

with open("movies.txt", "w", encoding="utf-8") as file:
    for film in top_100_movies:
        file.write(f"{film}\n")
