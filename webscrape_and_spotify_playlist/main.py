from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

user_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
year = user_date.split("-")[0]
url = f"https://www.billboard.com/charts/hot-100/{user_date}/"

song_list_webpage = requests.get(url).text

soup = BeautifulSoup(song_list_webpage, "html.parser")

titles_html = soup.find_all("h3", class_="a-font-primary-bold-s")
titles = [title.getText().strip() for title in titles_html][3:]

# login to spotify via spotipy
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="xxxxxxxxxxxxxx",
                                               client_secret="xxxxxxxxxxx",
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private"))

user_id = sp.current_user()["id"]
song_uris = []

for title in titles:
    result = sp.search(q=f"track:{title} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{title} doesn't exist in Spotify. Skipped.")

print("creating a playlist..")
playlist_id = sp.user_playlist_create(user_id, f"{user_date} Billboard 100", public=False)["id"]

print(sp.playlist_add_items(playlist_id=playlist_id, items=song_uris))

