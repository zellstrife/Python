import math

catOp = float(input('Digite o valor do cateto oposto: '))
catAdj = float(input('Digite o valor do cateto adjacente: '))

print('O cateto Oposto é: {}'
      '\nO cateto adjascente é: {}'
      '\nA hipotenusa é: {}'.format(catOp,catAdj,math.hypot(catOp, catAdj)))