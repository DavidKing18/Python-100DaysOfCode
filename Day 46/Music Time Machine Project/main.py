import requests
from bs4 import BeautifulSoup
import re
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

scope = "playlist-modify-private"
SPOTIPY_CLIENT_ID = 'a99b8925dea6481bbaa19a635d014365'
SPOTIPY_CLIENT_SECRET = os.environ["SPOTIPY_CLIENT_SECRET"]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri="http://example.com", scope=scope, show_dialog=True,
                                               cache_path="./token.txt"))

USER_ID = sp.current_user()['id']

BASE_URL = "https://www.billboard.com/charts/hot-100/"

print("Welcome to my Music Time Machine!")
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD, abeg 🤲: ")

pattern = r"[0-9]{4}-[0-9]{2}-[0-9]{2}"

while not re.match(pattern, date):
    print("You've entered an invalid date format. Try Again!")
    date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD 😐: ")

URL = f"{BASE_URL}{date}/"

response = requests.get(URL)
billboard_website = response.text

soup = BeautifulSoup(billboard_website, 'html.parser')
top_100_songs = soup.select(selector="ul li #title-of-a-story")

spotify_song_urls = []
year = date[0:4]
num = 1
print(f"Here's {date} Billboard Top 100:-\n")
for song in top_100_songs:
    track = song.string.strip()
    print(f"{num}.) {track}")
    num += 1
    query = f"track: {track} year: {year}"
    try:
        song = sp.search(q=query, type=["track"], limit=1)
        track_url = song['tracks']['items'][0]['external_urls']['spotify']
    except IndexError:
        pass
    else:
        spotify_song_urls.append(track_url)

new_playlist = sp.user_playlist_create(user=USER_ID, name=f"{date} Billboard 100", public=False, collaborative=False,
                                       description=f"Created this {date} playlist using Python 🥴")

new_playlist_id = new_playlist['id']
sp.playlist_add_items(playlist_id=new_playlist_id, items=spotify_song_urls)
