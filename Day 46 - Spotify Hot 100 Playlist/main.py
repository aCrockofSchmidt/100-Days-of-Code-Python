import requests
from bs4 import BeautifulSoup
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from prettyprinter import pprint

SPOTIPY_CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")
SPOTIPY_URI_REDIRECT = "http://example.com"

URL = "https://www.billboard.com/charts/hot-100"
chosen_date = input("What year would you like to travel to? Type the date in this format (YYYY-MM-DD): ")

response = requests.get(url=f"{URL}/{chosen_date}/")
billboard_data = response.text

soup = BeautifulSoup(billboard_data, "html.parser")

song_position = soup.find_all(name="span", class_=["c-label a-font-primary-bold-l u-font-size-32@tablet u-letter-spacing-0080@tablet", "c-label a-font-primary-bold-l u-font-size-32@tablet u-letter-spacing-0080@tablet"])
song_title = soup.find_all(name="h3", class_=["c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet", "c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only"])
song_artist = soup.find_all(name="span", class_=["c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only u-font-size-20@tablet", "c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only"])

positions = [position.getText().strip() for position in song_position]
titles = [song.getText().strip() for song in song_title]
artists = [artist.getText().strip() for artist in song_artist]
first_names = [artist.getText().strip().split("Featuring")[0] for artist in song_artist]

final_list = [f"#{i} - " + f"{j} by " + f"{k}" for i, j, k in zip(positions, titles, artists)]

# print(positions)
# print(titles)
# print(artists)
# print(first_names)
# print(final_list)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_URI_REDIRECT,
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

uri_list = []

for i in range(0, len(titles)):
    try:
        result = sp.search(q=f"track: {titles[i]} artist: {first_names[i]}", type="track", limit=1)
        uri_list.append(result["tracks"]["items"][-1]["uri"])
    except IndexError:
        print(f"The song '{titles[i]}' is not on Spotify. Song skipped.")

playlist_ID = sp.user_playlist_create(user=user_id, name=f"{chosen_date} Billboard 100", public=False, collaborative=False, description="Top 100 Songs on Wedding Day")["id"]

sp.playlist_add_items(playlist_id=playlist_ID, items=uri_list)

