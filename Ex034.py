nome = str(input('Escreva o nome do funcionario: '))
sal = float(input('Qual o salario de {} :'.format(nome)))

aSal = sal
if(sal >= 1250):
    print('Funcionario {}'
      '\nSalario atual: R${}'
      '\nSalario atualizado: R${}'.format(nome, sal, (sal+(sal * 0.10))))
else:
    print('Funcionario {}'
              '\nSalario atual: R${}'
              '\nSalario atualizado: R${}'.format(nome, sal, (sal + (sal * 0.15))))