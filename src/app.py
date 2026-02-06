import os
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import seaborn as sns
import spotipy as spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# load the .env file variables
load_dotenv()

# Get credential values
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

print (f'El client id es {client_id}')

id_artista = '4q3ewBCX7sLwd24euuV69X'

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

sp = spotipy.Spotify(auth_manager=auth_manager)

results = sp.artist_top_tracks(id_artista)

canciones = []

for tracks in results['tracks']:
    canciones.append({
        'name': tracks['name'],
        'popularity': tracks['popularity'],
        'duration_min': tracks['duration_ms'] / 60000  # Cambiado 'track' por 'tracks'
    })

tracks_df = pd.DataFrame(canciones)

print(tracks_df.head(3))

plt.scatter(tracks_df['duration_min'], tracks_df['popularity'])
plt.xlabel('Duration (minutes)')
plt.ylabel('Popularity')
plt.title('Relationship between duration and popularity')
plt.show()





