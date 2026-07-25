import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

# 1. Suas chaves de acesso
CLIENT_ID = '23c1be28cf594ba58b68ac66b97f3f18'
CLIENT_SECRET = 'c42f4c8827a348cf849f098a46bf4b81'

auth_manager = SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri='https://github.com/Igor-Novais',
    scope='playlist-read-private'
)
sp = spotipy.Spotify(auth_manager=auth_manager)

# 2. Coloque o ID da sua playlist "Top 50 GB" aqui:
playlist_id = '2TZFq7ss4fXl8kGLOtBF3G'

print("🕵️‍♂️ Iniciando Raio-X na API do Spotify...")
results = sp.playlist_tracks(playlist_id, limit=1)

if not results['items']:
    print("🚨 ALERTA: A API do Spotify diz que a playlist está VAZIA! (Zero músicas encontradas)")
else:
    print("✅ Item encontrado! Imprimindo o formato bruto (JSON) da primeira faixa:")
    print(json.dumps(results['items'][0], indent=2, ensure_ascii=False))
