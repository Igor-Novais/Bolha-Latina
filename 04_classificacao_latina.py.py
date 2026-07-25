import pandas as pd

# Mantenha o caminho exato do seu arquivo
caminho_arquivo = r'C:\Users\Igor\Documents\Portifólio Spotify\universal_top_spotify_songs.csv'
df = pd.read_csv(caminho_arquivo)
# Substitui os campos vazios (NaN) na coluna country pela palavra 'Global'
df['country'] = df['country'].fillna('Global')

print("Aplicando rotulagem de artistas latinos...")

# 1. Definição dos nossos "gatilhos"
artistas_latinos = [
    'Rosalía', 'Bad Bunny', 'J Balvin', 'Zion & Lennox', 'Karol G', 'Peso Pluma', 'Natanael Cano', 'Tito Double P', 'Jowell & Randy', 'Wisin & Yandel', 'Nio Garcia', 'Arcangel', 'Farruko',
    'Camilo', 'Yandel', 'Daddy Yankee', 'Jhay Cortez', 'Anuel AA', 'Ozuna', 'Maluma', 'Don Omar', 'Grupo Frontera', 'Beéle', 'Juanchito', 'Julio Lv'
    'Shakira', 'Feid', 'Rauw Alejandro', 'Maluma', 'Bizarrap', 'Manuel Turizo', 'DEKKO', 'Fuerza Regida', 'Nacho', 'CNCO', 'Nicky Jam', 'Anuel AA', 'Calle 24',
    'Becky G', 'Myke Towers', 'Ozuna', 'Anitta', 'Rauw Alejandro', 'Sech', 'Natti Natasha', 'Junior H', 'Neton Vega', 'Greeicy', 'Ovvy on the Drums', 'Danny Ocean', 'Lunay', 'Cazzu', 'Tini',
]
padrao_busca = '|'.join(artistas_latinos)
df['is_latin_song'] = df['artists'].str.contains(
    padrao_busca, case=False, na=False)


# 2. Definindo o Mercado (Onde está tocando)
# Extraído da sua lista de 72 países, isolando o ecossistema latino/ibérico
paises_latinos = [
    'AR', 'BO', 'BR', 'CL', 'CO', 'CR', 'DO', 'EC', 'ES',
    'GT', 'HN', 'MX', 'NI', 'PA', 'PE', 'PY', 'SV', 'UY', 'VE'
]
df['is_latin_market'] = df['country'].isin(paises_latinos)

# 3. Expansão Global
# Músicas latinas que estão fazendo sucesso FORA do mercado latino
df['global_expansion'] = (df['is_latin_song'] == True) & (
    df['is_latin_market'] == False)

# --- VISUALIZANDO OS RESULTADOS ---

# Total de streams mapeados
total_latin_streams = len(df[df['is_latin_song'] == True])
expansao_streams = len(df[df['global_expansion'] == True])


# --- VISUALIZANDO OS RESULTADOS ---
print(
    f"Total de registros de músicas latinas nos charts: {total_latin_streams}")
print(
    f"Desse total, registros fora do mercado latino (Expansão Global): {expansao_streams}")

# Mostrando uma amostra das músicas latinas invadindo o mundo
amostra_expansao = df[df['global_expansion'] == True][[
    'name', 'artists', 'country']].drop_duplicates().head(10)
print("\nAmostra de músicas latinas estourando em outros países:")
print(amostra_expansao)
