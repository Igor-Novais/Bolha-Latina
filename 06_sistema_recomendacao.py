import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity

caminho_arquivo = r'C:\Users\Igor\Documents\Portifólio Spotify\universal_top_spotify_songs.csv'
df = pd.read_csv(caminho_arquivo)


print("Iniciando o Sistema Preditivo de Recomendação...")


# 2. Limpeza Essencial para o Modelo
# Como o ranking é diário, removemos as duplicatas para manter apenas uma versão de cada música
df_catalogo = df.drop_duplicates(subset=['spotify_id']).copy()
df_catalogo.reset_index(drop=True, inplace=True)
print(f"Catálogo reduzido para {len(df_catalogo)} faixas únicas.")

# 3. Engenharia de Recursos (Feature Engineering)
# Selecionamos os atributos matemáticvos que vão definir a "vibe" da música
features = ['danceability', 'energy', 'valence', 'tempo', 'acousticness']

# Padronizando os dados (colocando todos na mesma escala de grandeza)
scaler = StandardScaler()
matriz_features_padronizada = scaler.fit_transform(df_catalogo[features])

# 4. Função da inteligência Artificial


# 4. A Função de Inteligência Artificial (Corrigida)
def recomendar_musica(nome_musica, nome_artista=None, top_n=5):
    # Tenta encontrar a música usando busca literal (regex=False) para evitar bugs com RegEx
    if nome_artista:
        musica_alvo = df_catalogo[(df_catalogo['name'].str.contains(nome_musica, case=False, na=False, regex=False)) &
                                  (df_catalogo['artists'].str.contains(nome_artista, case=False, na=False, regex=False))]
    else:
        musica_alvo = df_catalogo[df_catalogo['name'].str.contains(
            nome_musica, case=False, na=False, regex=False)]

    if musica_alvo.empty:
        return "Música não encontrada no catálogo."

    # Pega o índice (posição) da música encontrada
    indice_alvo = musica_alvo.index[0]

    # Isola o vetor matemático dessa música
    vetor_alvo = matriz_features_padronizada[indice_alvo].reshape(1, -1)

    # A MÁGICA: Calcula a similaridade (distância) desta música contra o catálogo inteiro
    similaridades = cosine_similarity(vetor_alvo, matriz_features_padronizada)

    # Pega os índices das músicas mais similares (ignorando a posição 0, que é a própria música)
    indices_similares = similaridades[0].argsort()[-(top_n + 1):-1][::-1]

    # Formata a resposta com as recomendações, usando .copy() para evitar o alerta do Pandas
    recomendacoes = df_catalogo.iloc[indices_similares][[
        'name', 'artists']].copy()
    recomendacoes['Similaridade'] = similaridades[0][indices_similares]

    # Formatação limpa da similaridade para porcentagem
    recomendacoes['Similaridade'] = (
        recomendacoes['Similaridade'] * 100).round(2).astype(str) + '%'

    musica_escolhida = df_catalogo.iloc[indice_alvo]
    print(
        f"\n🎧 Porque você ouviu: {musica_escolhida['name']} ({musica_escolhida['artists']})")
    print("-" * 50)
    print("O algoritmo recomenda as seguintes faixas pela proximidade do ritmo e energia:")
    print(recomendacoes.to_string(index=False))
    return "\nRecomendação concluída!"

# ==========================================
# 5. TESTANDO O MOTOR PREDITIVO NA PRÁTICA
# ==========================================


print("\n--- Teste 1: A Linha 0 (Onde o erro do RegEx acontecia) ---")
primeira_musica = df_catalogo.iloc[0]
print(recomendar_musica(primeira_musica['name'], primeira_musica['artists']))

print("\n--- Teste 2: A Vibe Latina (Karol G) ---")
print(recomendar_musica("Si Antes Te Hubiera Conocido", "KAROL G"))

print("\n--- Teste 3: A Vibe Latina (Bad Bunny) ---")
print(recomendar_musica("DtMF", "Bad Bunny"))
