from pprint import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

scope = "playlist-modify-private"
SPOTIPY_CLIENT_ID = 'a99b8925dea6481bbaa19a635d014365'
SPOTIPY_CLIENT_SECRET = os.environ["SPOTIPY_CLIENT_SECRET"]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri="http://example.com", scope=scope))

query = "track: safweqwdfqf year: 2000"

song = sp.search(q=query, type=["track"], limit=1)
track_url = song['tracks']['items'][0]['external_urls']['spotify']
pprint(track_url)
