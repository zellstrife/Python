import random

n = random.randint(0,1000)
m = n%2

if(m == 0):
    print('Numero: {}'
          '\n Este numero é PAR'.format(n))
else:
    print('Numero: {}'
          '\n Este numero é IMPAR'.format(n))