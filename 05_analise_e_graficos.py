import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Carregamento e Preparação da Base
caminho_arquivo = r'C:\Users\Igor\Documents\Portifólio Spotify\universal_top_spotify_songs.csv'
df = pd.read_csv(caminho_arquivo)
df['country'] = df['country'].fillna('Global')

# Definindo a Identidade da Música e o Mercado
artistas_latinos = [
    'Rosalía', 'Bad Bunny', 'J Balvin', 'Zion & Lennox', 'Karol G', 'Peso Pluma', 'Natanael Cano', 'Tito Double P', 'Jowell & Randy', 'Wisin & Yandel', 'Nio Garcia', 'Arcangel', 'Farruko',
    'Camilo', 'Yandel', 'Daddy Yankee', 'Jhay Cortez', 'Anuel AA', 'Ozuna', 'Maluma', 'Don Omar', 'Grupo Frontera', 'Beéle', 'Juanchito', 'Julio Lv'
    'Shakira', 'Feid', 'Rauw Alejandro', 'Maluma', 'Bizarrap', 'Manuel Turizo', 'DEKKO', 'Fuerza Regida', 'Nacho', 'CNCO', 'Nicky Jam', 'Anuel AA', 'Calle 24',
    'Becky G', 'Myke Towers', 'Ozuna', 'Anitta', 'Rauw Alejandro', 'Sech', 'Natti Natasha', 'Junior H', 'Neton Vega', 'Greeicy', 'Ovvy on the Drums', 'Danny Ocean', 'Lunay', 'Cazzu', 'Tini',
]
padrao_busca = '|'.join(artistas_latinos)
df['is_latin_song'] = df['artists'].str.contains(
    padrao_busca, case=False, na=False)

paises_latinos = ['AR', 'BO', 'BR', 'CL', 'CO', 'CR', 'DO', 'EC','ES', 'GT', 'HN', 'MX', 'NI', 'PA', 'PE', 'PY', 'SV', 'UY', 'VE']
df['is_latin_market'] = df['country'].isin(paises_latinos)
df['global_expansion'] = (df['is_latin_song'] == True) & (
    df['is_latin_market'] == False)

# ==========================================
# PARTE 1: A MATEMÁTICA DOS ATRIBUTOS
# ==========================================
print("Calculando as médias dos atributos musicais...")

# Criando uma coluna amigável para o gráfico
df['Categoria'] = df['is_latin_song'].apply(
    lambda x: 'Música Latina' if x else 'Resto do Mundo')

# Selecionamos os atributos: dançabilidade, energia e valência (positividade)
colunas_audio = ['danceability', 'energy', 'valence']
medias = df.groupby('Categoria')[colunas_audio].mean().reset_index()

print("\nMédias Matemáticas:")
print(medias)

# ==========================================
# PARTE 2: A VISUALIZAÇÃO GRÁFICA
# ==========================================
# Configurando o estilo visual dos gráficos (deixa mais bonito e limpo)
sns.set_theme(style="whitegrid")

# GRÁFICO 1: O Ritmo (Música Latina vs Resto do Mundo)
plt.figure(figsize=(10, 6))
# Derretendo a tabela para o formato que o seaborn gosta
medias_melted = medias.melt(
    id_vars='Categoria', var_name='Atributo Musical', value_name='Média (0 a 1)')

sns.barplot(data=medias_melted, x='Atributo Musical',
            y='Média (0 a 1)', hue='Categoria', palette=['#1DB954', '#535353'])
plt.title('A Fórmula do Sucesso: Música Latina vs Resto do Mundo',
          fontsize=14, fontweight='bold')
# Exibe a primeira janela (você precisa fechar ela para o código continuar)
plt.show()

# GRÁFICO 2: A Expansão Global (Onde a música latina mais estourou fora da bolha)
plt.figure(figsize=(12, 6))
expansao_df = df[df['global_expansion'] == True]
top_paises = expansao_df['country'].value_counts().head(10).reset_index()
top_paises.columns = ['País / Mercado', 'Acessos no Ranking']

sns.barplot(data=top_paises, x='País / Mercado',
            y='Acessos no Ranking', palette='magma')
plt.title('Expansão Global: Top 10 Mercados Fora da Bolha Consumindo Artistas Latinos',
          fontsize=14, fontweight='bold')
# Exibe a segunda janela
plt.show()
