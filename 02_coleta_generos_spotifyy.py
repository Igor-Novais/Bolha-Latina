import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint

CLIENT_ID = '91643fe777be4a128c85f686c4918374'
CLIENT_SECRET = 'cc026efd392e42c2b095df1dbcb89669'

auth_manager = SpotifyClientCredentials(
    client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Em vez de fazer uma busca por texto, vamos bater direto no endpoint
# do perfil completo usando o ID que você acabou de descobrir
id_lady_gaga = '1HY2Jd0NmPuamShAr6KMms'
artista_completo = sp.artist(id_lady_gaga)

print("Estrutura do Perfil Completo:")
pprint.pprint(artista_completo)
