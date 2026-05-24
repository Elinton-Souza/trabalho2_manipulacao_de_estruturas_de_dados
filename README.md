# Trabalho 2 — Manipulação de Estruturas de Dados

População de Veículos Elétricos: análise de um conjunto de dados de registros de veículos elétricos (BEV) e híbridos plug-in (PHEV) usando **listas, dicionários e conjuntos** em Python puro, com geração de gráficos via Plotly.

## Sobre o projeto

Programa de linha de comando que carrega um dataset de veículos elétricos e apresenta, através de um **menu interativo**, diversas análises sobre os dados. As contagens, agrupamentos e ordenações são feitos manualmente com estruturas de dados nativas do Python (sem bibliotecas de análise como pandas), com foco no aprendizado de manipulação de estruturas.

Disciplina: Algoritmos e Estruturas de Dados I.
Curso: Tecnologia em Análise e Desenvolvimento de Sistemas.
Professor: Edécio Fernando Iepsen.
Autor: Elinton Pereira de Souza Cunha.

## Sobre o dataset

O arquivo `Electric_Vehicle_Population_Data.csv` contém cerca de 150 mil registros de veículos elétricos. Os atributos utilizados nas análises são, entre outros:

- `Make` — fabricante (ex.: TESLA, NISSAN)
- `Model` — modelo (ex.: MODEL Y, LEAF)
- `Model Year` — ano do modelo
- `City` — cidade de registro
- `Electric Vehicle Type` — tipo do veículo:
  - `Battery Electric Vehicle (BEV)` — 100% elétrico
  - `Plug-in Hybrid Electric Vehicle (PHEV)` — híbrido plug-in

## Funcionalidades

O menu oferece as seguintes opções:

1. **Top 10 fabricantes por ano** — agrupa e ordena os fabricantes com mais veículos de um ano informado pelo usuário.
2. **Top 10 veículos mais vendidos** — ranking por fabricante + modelo.
3. **Top 10 cidades** — cidades com maior número de veículos.
4. **Top 10 veículos elétricos** — ranking apenas dos BEV.
5. **Top 10 veículos híbridos** — ranking apenas dos PHEV.
6. **Top 10 modelos mais vendidos** — ranking por nome do modelo.
7. **Proporção elétricos x híbridos** — contagem e percentual de cada tipo, com gráfico de pizza.
8. **Fabricantes: elétricos x híbridos (conjuntos)** — usa operações de conjunto (união, interseção e diferença) para comparar quais fabricantes produzem elétricos, híbridos ou ambos.

As opções de ranking (1 a 6) geram um **gráfico de barras** e a opção 7 gera um **gráfico de pizza**, abertos no navegador.

## Tecnologias

- Python 3
- Módulo `csv` (leitura do dataset)
- Estruturas nativas: `list`, `dict`, `set`, `tuple`
- [Plotly](https://plotly.com/python/) (gráficos)

## Como executar

1. Garanta que o `eletricworld.py` esteja na mesma pasta do `Electric_Vehicle_Population_Data.csv`.
2. Instale as dependências:

   ```bash
   pip install plotly pandas
   ```

3. Execute o programa:

   ```bash
   python eletricworld.py
   ```

4. Escolha uma opção do menu digitando o número correspondente. Os gráficos abrem automaticamente no navegador (arquivo `grafico.html`).

## Estrutura de branches

O projeto foi desenvolvido seguindo um fluxo de branches por funcionalidade:

- `main` — versão estável final.
- `dev` — branch de integração; cada funcionalidade finalizada é mesclada aqui.
- `feature/*` — uma branch por item do menu (ex.: `feature/top_fabricantes_por_ano`, `feature/graficos_plotly`, `feature/fabricantes_conjuntos`).

Cada funcionalidade foi commitada com [gitmoji](https://gitmoji.dev/), enviada para sua branch e mesclada na `dev` via Pull Request. Após todos os itens concluídos e testados, a `dev` foi promovida para a `main`.

## Estrutura dos arquivos

```
trabalho2_manipulacao_de_estruturas_de_dados/
├── eletricworld.py                       # programa principal
├── Electric_Vehicle_Population_Data.csv  # dataset
├── grafico.html                          # gráfico gerado (ignorado pelo Git)
├── .gitignore
└── README.md
```
