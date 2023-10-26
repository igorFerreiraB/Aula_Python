# arq = open("Python/usuarios.txt")

# for usuario in arq:
#     print(usuario)

# Função para converter bytes em megabytes
def bytes_to_mb(bytes):
    return bytes / (1024 * 1024)

# Função para calcular o percentual de uso
def percentual_de_uso(espaco, total):
    return (espaco / total) * 100

# Lê o arquivo "usuarios.txt"
with open("python/usuarios.txt", "r") as arquivo:
    linhas = arquivo.readlines()

# Inicializa lista para armazenar os dados dos usuários
dados_usuarios = []

# Processa as linhas do arquivo
total_espaco_ocupado = 0
for linha in linhas:
    partes = linha.split()
    if len(partes) == 2:
        nome = partes[0]
        espaco_em_disco = int(partes[1])
        total_espaco_ocupado += espaco_em_disco
        dados_usuarios.append((nome, espaco_em_disco))

# Ordena a lista de dados de usuários pelo espaço ocupado em ordem decrescente
dados_usuarios.sort(key=lambda x: x[1], reverse=True)

# Abre o arquivo de relatório para escrita
with open("python/relatorio.txt", "w") as relatorio:
    relatorio.write("ACME Inc.               Uso do espaço em disco pelos usuários\n")
    relatorio.write("-" * 70 + "\n")
    relatorio.write(f"{'Nr.':<6}{'Usuário':<16}{'Espaço utilizado':<21}% do uso\n")
    relatorio.write("-" * 70 + "\n")

    for i, (nome, espaco_em_disco) in enumerate(dados_usuarios, start=1):
        espaco_mb = bytes_to_mb(espaco_em_disco)
        percentual = percentual_de_uso(espaco_em_disco, total_espaco_ocupado)
        relatorio.write(f"{i:<6}{nome:<16}{espaco_mb:.2f} MB{' ' * (20 - len(f'{espaco_mb:.2f} MB'))}{percentual:.2f}%\n")

    relatorio.write("-" * 70 + "\n")
    relatorio.write(f"Espaço total ocupado: {bytes_to_mb(total_espaco_ocupado):.2f} MB\n")
    relatorio.write(f"Espaço médio ocupado: {bytes_to_mb(total_espaco_ocupado / len(dados_usuarios)):.2f} MB\n")

print("Relatório gerado com sucesso em 'relatorio.txt'.")