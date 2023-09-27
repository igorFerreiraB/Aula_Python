# Closure e funçôes que retornam outra função
# Usando strings
def criar_saudcao(saudacao):
    def saudar(nome):
        return f"{saudacao}, {nome}"
    return saudar 

falar_bom_dia = criar_saudcao("Bom Dia!")
falar_boa_tarde = criar_saudcao("Boa Tarde!")
falar_boa_noite = criar_saudcao("Boa Noite!")


for nome in ["Igor", "Dulce", "Rodrigo"]:
    print(falar_bom_dia(nome))
    print(falar_boa_tarde(nome))
    print(falar_boa_noite(nome))

# Usando numéros inteiros
def multiplicar_numero(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = multiplicar_numero(2)
triplicar = multiplicar_numero(3)
quadruplicar = multiplicar_numero(4)


for numero in [2, 4, 5]:
    print(duplicar(numero))
    print(triplicar(numero))
    print(quadruplicar(numero))
