import csv
# import plotly.express as px

veiculos = []

with open("Electric_Vehicle_Population_Data.csv", mode ="r") as arq:
    dados_csv = csv.DictReader(arq)
    for linha in dados_csv:
        veiculos.append(linha)

def titulo(texto, traco="-"):
    print()
    print(texto.upper())
    print(traco * 60)