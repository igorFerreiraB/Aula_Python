dados_cidades = []

for i in range(1, 2):
    cidade = {}
    cidade["codigo"] = int(input(f"Digite o código da cidade {i}: "))
    cidade["veiculos"] = int(input(f"Digite o número de veículos de passeio (em 1999) da cidade {i}: "))
    cidade["acidentes"] = int(input(f"Digite o número de acidentes de trânsito com vítimas (em 1999) da cidade {i}: "))
    dados_cidades.append(cidade)

maior_acidentes = max(dados_cidades, key=lambda x: x["acidentes"])
menor_acidentes = min(dados_cidades, key=lambda x: x["acidentes"])

print(f"A cidade com o maior índice de acidentes é a cidade {maior_acidentes['codigo']} com {maior_acidentes['acidentes']} acidentes.")
print(f"A cidade com o menor índice de acidentes é a cidade {menor_acidentes['codigo']} com {menor_acidentes['acidentes']} acidentes.")

total_veiculos = sum(cidade["veiculos"] for cidade in dados_cidades)
media_veiculos = total_veiculos / len(dados_cidades)

print(f"A média de veículos nas cinco cidades é: {media_veiculos}")

cidades_com_menos_veiculos = [cidade for cidade in dados_cidades if cidade["veiculos"] < 2000]

if cidades_com_menos_veiculos:
    total_acidentes_cidades_menos_veiculos = sum(cidade["acidentes"] for cidade in cidades_com_menos_veiculos)
    media_acidentes_cidades_menos_veiculos = total_acidentes_cidades_menos_veiculos / len(cidades_com_menos_veiculos)
    print(f"A média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio é: {media_acidentes_cidades_menos_veiculos}")
else:
    print("Não há cidades com menos de 2.000 veículos de passeio.")