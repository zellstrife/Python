import random
pc = random.randint(1,5)
player = int(input('Digite o numero de 1 a 5 e desafie o computador: '))

if(pc == player):
    print('Player: {}'
          '\nPC: {}'
          '\nParabens !!! Você ganhou do Pc'.format(player,pc))
else:
    print('Player: {}'
          '\nPC: {}'
          '\nTente novamente HUMANO !!!'.format(player, pc))