from typing import List
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy import oauth2
import pprint
pp = pprint.PrettyPrinter(indent=4)


PORT_NUMBER = 8080
SPOTIPY_CLIENT_ID = 'f0e1fb34f6aa4b32bcb61d68cbc2d020'
SPOTIPY_CLIENT_SECRET = '52e04e1e7aab4245bab8a0bc2b6ac4b6'
SPOTIPY_REDIRECT_URI = 'http://example.com'
SCOPE = 'playlist-modify-private'
CACHE = '.spotipyoauthcache'

sp_oauth = oauth2.SpotifyOAuth( SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET,SPOTIPY_REDIRECT_URI,scope=SCOPE,cache_path=CACHE )


auth=sp_oauth.get_access_token( as_dict=True)


sp = spotipy.client.Spotify(auth=auth["access_token"])

id = sp.me()["id"]


 #Search for list of songs
date=input('What Year do you want to travel to?Type the date in this format YYYY-MM-DD: \n')



response=requests.get(f'https://www.billboard.com/charts/hot-100/{date}')
data=response.text

soup=BeautifulSoup(data,'lxml')
songsHeaders=soup.select('.chart-results-list li h3')

listOfSongs=[]
for songHeader in songsHeaders:
    listOfSongs.append(songHeader.getText().replace('\n',''))



#Merging together

song_uris = []
year = date.split("-")[0]

for song in listOfSongs:

    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlistId=sp.user_playlist_create(user=id,name=f'{date} Billboard 100',public=False)


sp.user_playlist_add_tracks(user=id, playlist_id=playlistId["id"], tracks=song_uris, position=None)