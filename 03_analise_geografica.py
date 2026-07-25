import pandas as pd

# Mantenha o caminho exato do seu arquivo
caminho_arquivo = r'C:\Users\Igor\Documents\Portifólio Spotify\universal_top_spotify_songs.csv'
df = pd.read_csv(caminho_arquivo)

print("Verificando a estrutura geográfica da base...")

# Procura se a coluna de país chama 'country', 'region' ou algo similar
colunas = df.columns
print(f"\nTodas as colunas: {colunas}")

# Se existir uma coluna chamada 'country', vamos listar os países
if 'country' in df.columns:
    paises = df['country'].dropna().unique()
    print(f"\nTotal de países rastreados: {len(paises)}")
    print(paises)
else:
    print("\nNão encontrei a coluna 'country'. Tente identificar qual dessas colunas acima guarda o país!")
