import requests
from bs4 import BeautifulSoup
import re
import spotipy
from spotipy import oauth2
import os


SPOTIPY_CLIENT_ID = 'a99b8925dea6481bbaa19a635d014365'
SPOTIPY_CLIENT_SECRET = os.environ["SPOTIPY_CLIENT_SECRET"]
SPOTIPY_REDIRECT_URI = 'http://mysite.com/callback/'
SCOPE = "playlist-modify-private"
CACHE = '.spotipyoauthcache'

sp_oauth = oauth2.SpotifyOAuth(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI, scope=SCOPE, cache_path=CACHE)


BASE_URL = "https://www.billboard.com/charts/hot-100/"

year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

pattern = r"[0-9]{4}-[0-9]{2}-[0-9]{2}"

if not re.match(pattern, year):
    print("You've entered an invalid date format. Try Again!")
    year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

URL = f"{BASE_URL}{year}/"

response = requests.get(URL)
billboard_website = response.text

soup = BeautifulSoup(billboard_website, 'html.parser')
top_100_songs = soup.select(selector="ul li #title-of-a-story")


for song in top_100_songs:
    print(song.string.strip())
