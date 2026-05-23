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


def top_fabricantes_por_ano():
    ano = input("Digite o ano (Model Year) que deseja analisar: ")

    grupos = {}
    for veiculo in veiculos:
        if veiculo["Model Year"] == ano:
            fabricante = veiculo["Make"]
            grupos[fabricante] = grupos.get(fabricante, 0) + 1

    if not grupos:
        print(f"Nenhum veículo encontrado para o ano {ano}.")
        return

    titulo(f"Top 10 Fabricantes em {ano}")

    grupos_ord = dict(sorted(grupos.items(),
                             key=lambda grupo: grupo[1], reverse=True))

    print(f"{'Nº':<4}{'Fabricante':<22}{'Qtd. veículos':>15}")
    print("-" * 60)
    for posicao, (fabricante, qtd) in enumerate(grupos_ord.items(), start=1):
        print(f"{posicao:<4}{fabricante:<22}{qtd:>15}")
        if posicao == 10:
            break


# Menu
while True:
    titulo("População de Veículos Elétricos", "=")
    print("1. Top 10 Fabricantes por Ano")
    print("10. Finalizar")
    opcao = input("Opção: ")

    if opcao == "1":
        top_fabricantes_por_ano()
    elif opcao == "10":
        print("\nEncerrando o programa. Até mais!")
        break
    else:
        print("Opção inválida! Escolha 1 ou 10.")