import spotipy as sp
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

# 1. Autenticando na API
CLIENT_ID = '91643fe777be4a128c85f686c4918374'
CLIENT_SECRET = 'cc026efd392e42c2b095df1dbcb89669'

auth_manager = SpotifyClientCredentials(
    client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = sp.Spotify(auth_manager=auth_manager)

# 2. Carregando o dataset do Kaggle
df_kaggle = pd.read_csv(
    r'C:\Users\Igor\Documents\Portifólio Spotify\universal_top_spotify_songs.csv')

# Teste: Buscando as "audio features" de 'DESPECHÁ' da Rosalía
track_url = 'https://open.spotify.com/track/5ildzzuzolMie1cEqJGAto'
features = sp.audio_features(track_url)

print("Conexão bem-sucedida! Veja os atributos matemáticos da música:")
print(features)


# Mostra o nome de todas as colunas disponíveis no dataset
print(df_kaggle.columns)

# ver uma amostra dos dados reais para confirmar:
print(df_kaggle.head())
