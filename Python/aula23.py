# pessoa = {
#     "Nome": "Igor",
#     "Sobrenome": "Ferreira"
# }
# dados_pessoa = {
#     "Idade": 16,
#     "Altura": 1.81
# }
# pessoa_completa = {**pessoa, **dados_pessoa}

# print(pessoa_completa)

def mostra_pessoa(*args, **kwargs):
    for k, v in kwargs.items():
        print(k, v)

mostra_pessoa(nome= "Igor", sobrenome= "Ferreira")