arq = open("arquivo.txt")
linhas = arq.readlines()

alunos = []
notas = []

def titulo(txt):
    tam = len(txt) + 4
    print("-" * tam)
    print(f"  {txt}")
    print("-" * tam)

# Tratativa
try: 
    # Laço principal
    for linha in linhas:

        # Quebra de linha e formatação
        linha = linha.strip()
        linha = linha.split(",")

        # Chamando itens
        alunos.append(linha[0])
        notas.append(float(linha[1]))
except:
    print("ERRO!!")
else: 
    dicionario = dict(zip(alunos, notas))
    # Soma das notas
    soma_notas = sum(dicionario.values())
    media = soma_notas / len(alunos)


    print(dicionario)
    titulo("↓↓↓ MEDIA DA SALA ↓↓↓")
    print(f"{media:.2f}")
    titulo("↓↓↓ ALUNOS NOTAS > 6 ↓↓↓")

    for nota in notas:
        if nota > 6:
            print(nota)



# soma_notas = 0
# for nota in notas:
#     soma_notas += nota
# print(soma_notas)

# for aluno in alunos:
#     print(len(alunos))
        