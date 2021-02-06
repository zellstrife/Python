import random

al1 = str(input('Digite o nome do aluno: '))
al2 = str(input('Digite o nome do aluno: '))
al3 = str(input('Digite o nome do aluno: '))
al4 = str(input('Digite o nome do aluno: '))

list = [al1,al2,al3,al4]
random.shuffle(list)

print('A ordem de apresentação será: {}'.format(list))