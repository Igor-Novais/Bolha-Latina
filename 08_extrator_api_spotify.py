import spotipy
# <-- ATENÇÃO: Mudamos o import aqui em cima!
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
from datetime import datetime

print("Iniciando conexão com a API do Spotify...")

# 1. Coloque suas chaves aqui (entre as aspas)
CLIENT_ID = '23c1be28cf594ba58b68ac66b97f3f18'
CLIENT_SECRET = 'c42f4c8827a348cf849f098a46bf4b81'

# 2. Nova Autenticação (OAuth 2.0) <-- ENTRA EXATAMENTE AQUI!
auth_manager = SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri='https://github.com/Igor-Novais',
    scope='playlist-read-private'
)
sp = spotipy.Spotify(auth_manager=auth_manager)

# 3. Dicionário com os IDs das Playlists "Top 50" oficiais
playlists_top50 = {
    'Global': '3TPOHO65mDHJaSqfGk30TB',

    # América do Norte
    'US': '7dBPj6kPiJtHJ0KAlstRqT',
    'CA': '7g0SD9agIIaITp9cuBjhDk',
    'MX': '5sbcMkGFQKTwETQBbfW7Ux',

    # América do Sul
    'BR': '1l2LjALk6J9zD8SYq6KGaR',
    'AR': '1D1BIxj1T4nm7LNxLITOb1',
    'CL': '6lJaFvYb8YPpNUbaJhYBrt',
    'CO': '7sPEmWkrwkCUJE2M2c6s7y',
    'PE': '6qqDge5cOnVHVKlngSFbzh',

    # Europa
    'PT': '3z9XGd6YmqOSQ6StU0WKH5',
    'ES': '1lEpOGTs4UizGHf3fmTCPV',
    'FR': '7fo2koMufl8PNYR4Qdh6g9',
    'IT': '2DBnIfLjodgdi3waAQF7UK',
    'GB': '2TZFq7ss4fXl8kGLOtBF3G',
    'DE': '4ELQ87LlPxLUS6VHSfUXU4',
    'NL': '5YPFL7sATKDAVPAtY7L8uj',
    'SE': '6MGTENVmbL3nmEoyp2Dgdg',
    'CH': '1vHc8pP7XD97lCJN7EiP1H',

    # Ásia e Oceania
    'JP': '5tLE3UkMxusrJqT7i3pcwD',
    'AU': '50zaFHVmgh4oJj2dqHFCqJ',
    'IN': '4R641hiNtaZkAcoCsMZD6E',
    'PH': '5hxVt7LbeYo8ke4RhQNH3N',
    'ID': '4mJBPEDXGQthhQVyPpv1em'
}

dados_extraidos = []
data_hoje = datetime.now().strftime('%Y-%m-%d')

for country, playlist_id in playlists_top50.items():
    print(f"Buscando as 50 músicas mais tocadas em: {country}...")

    # Busca as faixas da playlist
    results = sp.playlist_tracks(playlist_id)

    musicas_validas = []
    ids_validos = []

    for item in results['items']:
        # O filtro inteligente: aceita tanto 'track' quanto 'item'
        musica = item.get('track') or item.get('item')

        if musica and isinstance(musica, dict) and musica.get('id'):
            if musica.get('type') == 'track':
                musicas_validas.append(musica)
                ids_validos.append(musica['id'])

    if not ids_validos:
        print(f"⚠️ Nenhuma música encontrada em {country}. Pulando...")
        continue

    # Monta as linhas da nossa tabela final apenas com os dados permitidos
    for track in musicas_validas:
        artistas = ", ".join([artist['name'] for artist in track['artists']])

        dados_extraidos.append({
            'name': track['name'],
            'artists': artistas,
            'country': country,
            'snapshot_date': data_hoje,
            'popularity': track.get('popularity', 0),
            # Preenchemos com None (Nulo) para manter a estrutura do Power BI intacta
            'danceability': None,
            'energy': None,
            'valence': None,
            'tempo': None
        })

# Transformação e Exportação
print("Organizando os dados limpos...")
df_hoje = pd.DataFrame(dados_extraidos)

caminho_saida = r'C:\Users\Igor\Documents\Portifólio Spotify\spotify_hoje.csv'
df_hoje.to_csv(caminho_saida, index=False, encoding='utf-8')

print("-" * 50)
print(f"✅ Extração via API concluída! Arquivo salvo em: {caminho_saida}")
