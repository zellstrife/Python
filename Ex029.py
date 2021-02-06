import random
km = int(random.randint(1,240))

if(km <= 80 ):
    print('Siga bem a sua viagem !!')
else:
    print('Você ultrapassou o limite de velocidade'
          '\n Velocidade permitida: 80Km'
          '\n Sua velocidade: {}'
          '\n Será enviado uma multa no valor de: {} reais'.format(km,(km-80)*7))