pessoa = {
    "nome": "Igor",
    "sobrenome": "Ferreira",
    "idade": 16,
    "endereço": [
        {"rua1": "Rua Corronel Vicente Ferreira Carneiro", "numero": "23"},
        {"rua2": "Avenida Perimetral", "numero": "2370"},
    ]
}

# pessoa = dict(nome="Igor", sobrenome="Ferreira")

# print(pessoa, type(pessoa))

print(pessoa["nome"])
print(pessoa["sobrenome"])
print("-" * 25)
for chave in pessoa:
    print(chave, pessoa[chave])