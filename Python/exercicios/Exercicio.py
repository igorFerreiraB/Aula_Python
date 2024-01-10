import functools

class Turma:
    alunos = []
    def addAluno(self, aluno):
        self.alunos.append(aluno)

    def calcMedia(self):
        total = 0
        for a in self.alunos:
            total += a.nota
        return total / len(self.alunos)
    
    def maiorNota(self): 
        maior = Aluno('', -1)
        for a in self.alunos:
            if a.nota > maior.nota:
                maior = a
        return maior

class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

arq = open("python/arquivo.txt")
linhas = arq.readlines()
turma = Turma()

for l in linhas:
    l = l.strip().split(',')
    aluno = Aluno(l[0], float(l[1]))
    turma.addAluno(aluno)

print(turma.calcMedia())
alunoMaiorNota = turma.maiorNota()


print('Aluno maior nota nome: ', alunoMaiorNota.nome, 'Nota: ', alunoMaiorNota.nota)

