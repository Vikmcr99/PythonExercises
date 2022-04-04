import random
for c in range(1,5):
    input('Nome do {} aluno:'.format(c))
alunos = [c]
escolhido = random.choice(alunos)
print(escolhido)