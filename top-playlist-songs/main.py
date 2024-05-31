from bs4 import BeautifulSoup
import requests
import os ,dotenv

import spotipy
from spotipy.oauth2 import SpotifyOAuth


dotenv.load_dotenv()


date=input('which year do you want to travel to? Type the date in format YYYY-MM-DD: ')

response=requests.get(f'https://www.billboard.com/charts/hot-100/{date}')

soup=BeautifulSoup(response.text,'html.parser')
top_songs=soup.find_all('h3',attrs={'id':'title-of-a-story','class':['a-no-trucate',' lrv-u-font-size-18@tablet',' lrv-u-font-size-16',' u-line-height-125', ' u-line-height-normal@mobile-max',' a-truncate-ellipsis u-max-width-330',' u-max-width-230@tablet-only']})

song_names=[song.getText().strip() for song in top_songs]



sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.getenv('SPOTIFY_CLIENT_ID'),
                                               client_secret=os.getenv('SPOTIFY_CLIENT_SECRET'),
                                               redirect_uri=os.getenv('SPOTIPY_REDIRECT_URI'),
                                               scope="playlist-modify-private",
                                               cache_path='.cache',
                                               username='Jayanth Kumar K',
                                               show_dialog=True))
user_id=(sp.current_user()['id'])  
year=date.split('-')[0]
song_uri=[]

for song in song_names:
    result=sp.search(q=f'track:{song} year:{year}',type='track')
    try:
        uri=result['tracks']['items'][0]['uri']
        song_uri.append(uri)
    except IndexError:
        print(f'{song} is not available in spotify.')


playlist=sp.user_playlist_create(user_id,name=f'{date} Billboard 100',public=False)


new_playlist=sp.playlist_add_items(playlist_id=playlist['id'],items=song_uri)

       