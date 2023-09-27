# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# lista = [1,42,65,2,45,6,4,2,14,5,9,10]
# lista.sort(reverse=True)
# print(lista)

# Função ordena
# def ordena(item):
#     return item["nome"]

def exibir(*lista):
    for item in lista:
        print(item)
    print()

# Aqui tem um metodo parecido com o sort() porem essé metodo sorted() de devolve uma copia so que você passou aqui no caso foi a variavel (lista) porem uma copia "rasa"
# Em seginda temos o lambda que age como se fosse uma função porem em uma linha só ao inves da def() que usa identação
l1 = sorted(lista, key=lambda item: item["nome"])
l2 = sorted(lista, key=lambda item: item["sobrenome"])

# Aqui a função ordena() é chamada é em seguida a função sort() também faz seu trabalho que e ordena a lista por orden alfabetica
# Na verdade a variavel (lista) recebe um metodo sort() que recebe como chave(key=) a funão acima ordena()
# lista.sort(key=ordena)

exibir(l1)
exibir(l2)


