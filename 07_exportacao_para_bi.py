import pandas as pd
import pycountry

print("Preparando os dados para o Business Intelligence...")

# 1. Carregamento da base bruta
caminho_arquivo = r'C:\Users\Igor\Documents\Portifólio Spotify\universal_top_spotify_songs.csv'
df = pd.read_csv(caminho_arquivo)
df['country'] = df['country'].fillna('Global')

# 2. Aplicando as suas regras de negócio (Heurísticas)
artistas_latinos = [
    'Rosalía', 'Bad Bunny', 'J Balvin', 'Zion & Lennox', 'Karol G', 'Peso Pluma', 'Natanael Cano', 'Tito Double P', 'Jowell & Randy', 'Wisin & Yandel', 'Nio Garcia', 'Arcangel', 'Farruko',
    'Camilo', 'Yandel', 'Daddy Yankee', 'Jhay Cortez', 'Anuel AA', 'Ozuna', 'Maluma', 'Don Omar', 'Grupo Frontera', 'Beéle', 'Juanchito', 'Julio Lv'
    'Shakira', 'Feid', 'Rauw Alejandro', 'Maluma', 'Bizarrap', 'Manuel Turizo', 'DEKKO', 'Fuerza Regida', 'Nacho', 'CNCO', 'Nicky Jam', 'Anuel AA', 'Calle 24',
    'Becky G', 'Myke Towers', 'Ozuna', 'Anitta', 'Rauw Alejandro', 'Sech', 'Natti Natasha', 'Junior H', 'Neton Vega', 'Greeicy', 'Ovvy on the Drums', 'Danny Ocean', 'Lunay', 'Cazzu', 'Tini',
]
padrao_busca = '|'.join(artistas_latinos)

df['is_latin_song'] = df['artists'].str.contains(
    padrao_busca, case=False, na=False, regex=True)

paises_latinos = ['AR', 'BO', 'BR', 'CL', 'CO', 'CR', 'DO', 'EC',
                  'ES', 'GT', 'HN', 'MX', 'NI', 'PA', 'PE', 'PY', 'SV', 'UY', 'VE']
df['is_latin_market'] = df['country'].isin(paises_latinos)

# A grande métrica para o BI
df['global_expansion'] = (df['is_latin_song'] == True) & (
    df['is_latin_market'] == False)

# Coluna categórica para os gráficos
df['Categoria'] = df['is_latin_song'].apply(
    lambda x: 'Música Latina' if x else 'Resto do Mundo')

# 3. Limpeza Final para o BI ficar rápido
# Selecionamos apenas as colunas que importam para o Dashboard visual
colunas_para_bi = [
    'name', 'artists', 'country', 'snapshot_date', 'popularity',
    'danceability', 'energy', 'valence', 'tempo', 'Categoria', 'global_expansion'
]
df_bi = df[colunas_para_bi].copy()

# Função para buscar o nome completo do país


def obter_nome_pais(sigla):
    if sigla == 'Global' or pd.isna(sigla):
        return sigla
    try:
        # O Spotify usa o padrão Alpha-2
        return pycountry.countries.get(alpha_2=sigla).name
    except:
        return sigla  # Se não achar, mantém a sigla


# Criamos uma nova coluna com os nomes completos
df['country_name'] = df['country'].apply(obter_nome_pais)

# Exportando para a sua pasta do projeto
caminho_saida = r'C:\Users\Igor\Documents\Portifólio Spotify\dataset_limpo_bi.csv'
df_bi.to_csv(caminho_saida, index=False, encoding='utf-8')

print("-" * 50)
print(f"✅ Pipeline concluído! Dataset para o BI gerado com sucesso.")
print(f"Arquivo salvo em: {caminho_saida}")
