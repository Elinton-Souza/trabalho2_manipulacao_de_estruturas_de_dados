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

# função que trás o top 10 dos veículos mais vendidos no ano escolhido, trazendo
# a comparação por fabricante.

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


# top 10 dos veículos mais vendidos por fabricante.
def top_veiculos_mais_vendidos():

    grupos = {}
    for veiculo in veiculos:
        chave = (veiculo["Make"], veiculo["Model"])
        grupos[chave] = grupos.get(chave, 0) + 1

    titulo("Top 10 Veículos Mais Vendidos por Marca")

    grupos_ord = dict(sorted(grupos.items(), key=lambda grupo: grupo[1], reverse=True))

    print(f"{'Nº' :<4}{'Fabricante':<15}{'Veiculo':<30}{'Qtd. veiculos vendidos':>15}")
    print("-" * 60)
    for posicao, ((fabricante, modelo), qtd) in enumerate(grupos_ord.items(), start=1):
        print(f"{posicao:<4}{fabricante:<15}{modelo:<22}{qtd:>15}")
        if posicao == 10:
            break


# top 10 cidades com mais veículos vendidos.
def top_cidades_com_mais_veiculos_vendidos():
    grupos = {}
    for veiculo in veiculos:
        cidade = veiculo["City"]
        grupos[cidade] = grupos.get(cidade, 0) + 1

    titulo("Top 10 Cidades com Mais Veículos Vendidos")

    grupos_ord = dict(sorted(grupos.items(), key=lambda grupo: grupo[1], reverse=True))

    print(f"{'Nº' :<4}{'Cidade':<22}{'Qtd. veiculos vendidos':>15}")
    print("-" * 60)
    for posicao, (cidade, qtd) in enumerate(grupos_ord.items(), start=1):
        print(f"{posicao:<4}{cidade:<22}{qtd:>15}")
        if posicao == 10:
            break

    
#  top 10 veículos elétricos mais vendidos
def top_eletricos_mais_vendidos():
    grupos = {}
    
    TIPO_ELETRICO = "Battery Electric Vehicle (BEV)"

    for veiculo in veiculos:
        if veiculo["Electric Vehicle Type"] == TIPO_ELETRICO:
            chave = (veiculo["Make"], veiculo["Model"])
            grupos[chave] = grupos.get(chave, 0) + 1

    titulo("Top 10 Veículos Elétricos Mais Vendidos")

    grupos_ord = dict(sorted(grupos.items(), key=lambda grupo: grupo[1], reverse=True))

    print(f"{'Nº':<4}{'Fabricante':<15}{'Veiculo':<30}{'Qtd. veiculos':<15}")
    print('-' * 60)
    for posicao, ((fabricante, modelo), qtd) in enumerate(grupos_ord.items(), start=1):
        print(f"{posicao:<4}{fabricante:<15}{modelo:<30}{qtd:<15}")
        if posicao == 10:
            break


#  top 10 veículos híbridos mais vendidos
def top_hibridos_mais_vendidos():
    grupos = {}
    
    TIPO_HIBRIDO = "Plug-in Hybrid Electric Vehicle (PHEV)"

    for veiculo in veiculos:
        if veiculo["Electric Vehicle Type"] == TIPO_HIBRIDO:
            chave = (veiculo["Make"], veiculo["Model"])
            grupos[chave] = grupos.get(chave, 0) + 1

    titulo("Top 10 Veículos Híbridos Mais Vendidos")

    grupos_ord = dict(sorted(grupos.items(), key=lambda grupo: grupo[1], reverse=True))

    print(f"{'Nº':<4}{'Fabricante':<15}{'Veiculo':<30}{'Qtd. veiculos':<15}")
    print('-' * 60)
    for posicao, ((fabricante, modelo), qtd) in enumerate(grupos_ord.items(), start=1):
        print(f"{posicao:<4}{fabricante:<15}{modelo:<30}{qtd:<15}")
        if posicao == 10:
            break


# Top 10 modelos mais vendidos
def top_modelos_mais_vendidos():
    grupos = {}
    for veiculo in veiculos:
        modelo = veiculo["Model"]
        grupos[modelo] = grupos.get (modelo, 0) + 1

    titulo("Top 10 Modelos Mais Vendidos")

    grupos_ord = dict(sorted(grupos.items(), key=lambda grupo:grupo[1], reverse=True))

    print(f"{'Nº':<4}{'Modelo':<22}{'Qtd. veiculos':<15}")
    print('-' * 60)
    for posicao, (modelo, qtd) in enumerate(grupos_ord.items(), start=1):
        print(f"{posicao:<4}{modelo:<22}{qtd:<15}")
        if posicao == 10:
            break


# Menu
while True:
    titulo("População de Veículos Elétricos", "=")
    print("1. Top 10 Fabricantes por Ano")
    print("2. Top 10 Veículos Mais Vendidos")
    print("3. Top 10 Cidades com Mais Veículos Vendidos")
    print("4. Top Elétricos Mais Vendidos")
    print("5. Top Hibridos Mais Vendidos")
    print("6. Top 10 Modelos Mais Vendidos")
    print("0. Finalizar")
    opcao = input("Opção: ")

    if opcao == "1":
        top_fabricantes_por_ano()
    elif opcao =="2":
        top_veiculos_mais_vendidos()
    elif opcao =="3":
        top_cidades_com_mais_veiculos_vendidos()
    elif opcao =="4":
        top_eletricos_mais_vendidos()
    elif opcao =="5":
        top_hibridos_mais_vendidos()
    elif opcao =="6":
        top_modelos_mais_vendidos()
    elif opcao == "0":
        print("\nEncerrando o programa. Até mais!")
        break
    else:
        print()
        print("Opção inválida!")
        print("Escolha 0 para Saír ou de 1 a 7 para verificar.")
        print("=" * 60)