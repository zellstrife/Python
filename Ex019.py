import random

al1 = str(input('Digite o nome do aluno: '))
al2 = str(input('Digite o nome do aluno: '))
al3 = str(input('Digite o nome do aluno: '))
al4 = str(input('Digite o nome do aluno: '))

esc = random.choice([al1,al2,al3,al4])

print('O aluno escolhido foi: {}'.format(esc))