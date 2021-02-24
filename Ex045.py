import random

player = int(input('1 - PAPEL'
                   '\n2 - PEDRA'
                   '\n3 - TESOURA'
                   '\nEscolha e tente ganhar do pc: '))
pc = ['TESOURA','PEDRA','PAPEL']
esc = random.choice(pc)

if esc == 'PAPEL' and player == 1:
    print('Player: PAPEL'
          '\nPC: {}'
          '\n Resultado: Empate'.format(esc))
elif esc == 'PAPEL' and player == 2:
    print('Player: PEDRA'
          '\nPC: {}'
          '\n Resultado: PC ganhou'.format(esc))
elif esc == 'PAPEL' and player == 3:
    print('Player: TESOURA'
          '\nPC: {}'
          '\n Resultado: Player Ganhou'.format(esc))
elif esc == 'TESOURA' and player == 2:
    print('Player: PEDRA'
          '\nPC: {}'
          '\n Resultado: Player ganhou'.format(esc))
elif esc == 'TESOURA' and player == 3:
    print('Player: TESOURA'
          '\nPC: {}'
          '\n Resultado: Empate'.format(esc))
elif esc == 'TESOURA' and player == 1:
    print('Player: PAPEL'
          '\nPC: {}'
          '\n Resultado: PC ganhou'.format(esc))
elif esc == 'PEDRA' and player == 2:
    print('Player: PEDRA'
          '\nPC: {}'
          '\n Resultado: Empate'.format(esc))
elif esc == 'PEDRA' and player == 3:
    print('Player: TESOURA'
          '\nPC: {}'
          '\n Resultado: PC Ganhou'.format(esc))
elif esc == 'PEDRA' and player == 1:
    print('Player: PAPEL'
          '\nPC: {}'
          '\n Resultado: Player ganhou'.format(esc))
else:
    print('Você apostou errado parceiro')
