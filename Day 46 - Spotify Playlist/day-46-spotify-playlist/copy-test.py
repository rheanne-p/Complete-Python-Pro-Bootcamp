from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

print("copy-test.py")
# TODO 1. Create Python List of Top 100 Songs
date = input("What year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{date}"
billboard_html = requests.get(url=URL).text
soup = BeautifulSoup(billboard_html, "html.parser")

songs = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")
songs_list = [song.getText().replace("\n", "").replace("\t", "") for song in songs]


# TODO 2. Authenticate Spotify
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="09501535ba304d71b4653d3626a44d33",
        client_secret="09b11fa2ca8844e684992b28d2866ece",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]