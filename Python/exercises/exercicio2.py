# Exercício - sistema de perguntas e respostas

quant_acertos = 0
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ["1", "3", "4", "5"],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

try:
    for pergunta in perguntas:
        print(pergunta['Pergunta'])
        
        for k, v in enumerate(pergunta['Opções']):
            print(f"{k}) {v}")
        
        o = int(input("Escolha uma opção: "))
        
        if pergunta['Opções'][o] == pergunta['Resposta']:
            print("ACERTOU!!!")
            quant_acertos += 1

        else:
            print("ERROU!!!")
        
        print("-" * 30)

except IndexError:
    print("Digite somente os números pedidos")
except ValueError:
    print("Digite apenas números")

print(f"Você acertou {quant_acertos} de {len(pergunta)}")


