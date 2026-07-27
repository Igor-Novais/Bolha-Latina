# Global Latin Music Expansion & Recommendation System
**Um projeto End-to-End de Engenharia e Ciência de Dados focado na "Bolha Latina" no mercado fonográfico global.**

## Sobre o Projeto
Sempre tive a curiosidade de entender se a expansão da música latina pelo mundo foi apenas um fenômeno passageiro de 2023 ou se o gênero realmente se consolidou em novos mercados globais (como Europa e Ásia). Para responder a essa hipótese de negócio na prática, construí esta esteira analítica completa consumindo dados ao vivo da API do Spotify.

Além da engenharia de dados e análise geográfica, aproveitei meus estudos em Ciência de Dados e Inteligência Artificial para implementar um módulo de recomendação musical baseado nos padrões de consumo que identifiquei durante o processamento.

## Tecnologias Utilizadas
* **Linguagens e Bibliotecas:** Python (Pandas, Requests, Machine Learning básico).
* **Engenharia de Dados:** Spotify Web API (Extração de dados via OAuth 2.0).
* **Visualização e BI:** Power BI (Modelagem DAX, transição de contexto e UI/UX).

## Arquitetura do Pipeline
Para garantir que o código fosse escalável e organizado, modularizei o projeto em etapas:

* `01_exploracao` a `05_analise`: Scripts de limpeza, enriquecimento com gêneros musicais, aplicação de filtros geográficos rigorosos e análise exploratória.
* `06_sistema_recomendacao.py`: Implementação do sistema de recomendação (RecSys).
* `07_exportacao_para_bi.py`: Estruturação dos dados formatada especificamente para o modelo semântico do Power BI.
* `08_extrator_api_spotify.py`: Motor principal de raspagem ética e autenticação contínua na API.

## Desafios Técnicos Superados
Durante o desenvolvimento, lidei com gargalos reais de engenharia e versionamento. Um dos principais desafios foi estruturar o versionamento no Git contornando limites pesados de *Large File Storage* (LFS), exigindo a limpeza de histórico de cache e configuração estrita de arquivos `.gitignore` via terminal para arquivos CSV massivos. 

No lado de BI, o desafio foi impedir a inflação da base de dados empilhada. A solução foi modelar o DAX com medidas de "Contagem Distinta" (`Count Distinct`), substituindo a visão de "volume de streams" pelo real "alcance de países únicos".

## Visualização Final
O output deste pipeline Python alimenta um dashboard interativo (construído com metodologias de Data Storytelling e modos Claro/Escuro), permitindo que qualquer pessoa filtre o desempenho global dos artistas:

![Dashboard Light]() 
<img width="1433" height="804" alt="Light Mode BI 2" src="https://github.com/user-attachments/assets/5aa49655-ef43-4aec-bfee-0a352934b9ee" />
<img width="1443" height="811" alt="Light Mode BI" src="https://github.com/user-attachments/assets/378941aa-13a2-45f0-9b81-d4c4768dff67" />


![Dashboard Dark]()
<img width="1432" height="805" alt="Dark Mode BI 2" src="https://github.com/user-attachments/assets/67fd99b4-5f72-4ea1-b7fa-591e8c64731a" />
<img width="1444" height="811" alt="Dark Mode BI" src="https://github.com/user-attachments/assets/2731a33e-e43e-47bd-b26d-abe0a03b6d16" />

---
*Desenvolvido por Igor Novais Ribeiro Santos*
