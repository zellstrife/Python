cliente = str(input('Digite o nome do cliente: '))
km = float(input('Digite quantos quilometros foram rodados: '))
dias= int(input('Digite quantos dias o carro foi: '))
cKm = 0.15
cDias = 60
tcKm= km*cKm
tcDias = dias*cDias

print('o Cliente: {}'
      '\nAlugou o carro x por: {} dias'
      '\nE percorreu por: {} Km'
      '\nCusto por dia RS {} total cobrado RS {}'
      '\nCusto por Km R$ {} total cobrado R$ {}'
      '\n Total a ser pago pelo cliente: R$ {}'.format(cliente,dias,km,cDias,tcDias,cKm,tcKm,tcKm+tcDias))