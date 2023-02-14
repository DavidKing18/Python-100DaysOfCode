##############################################
#   100 Movies that You Must Watch Project
##############################################

import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
empire_website = response.text

soup = BeautifulSoup(empire_website, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")
movies = [movie.string for movie in all_movies]
movies.reverse()

with open("movies.txt", "w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")
