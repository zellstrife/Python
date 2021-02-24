nome = str(input('Digite o nome da pessoa a ser analisada: '))
peso = float(input('Digite o peso em Kg de {}: '.format(nome)))
altura = float(input('Digite a altura de {}: '.format(nome)))

imc = peso / (altura * altura)

if imc < 18.5:
    print('Nome: {}'
          '\nPeso: {}Kg'
          '\nAltura: {}M'
          '\nVocê esta abaixo do peso ideal'.format(nome, peso, altura))
elif imc <= 25:
    print('Nome: {}'
          '\nPeso: {}Kg'
          '\nAltura: {}M'
          '\nVocê esta no seu peso ideal'.format(nome, peso, altura))
elif imc <= 30:
    print('Nome: {}'
          '\nPeso: {}Kg'
          '\nAltura: {}M'
          '\nVocê esta com sobrepeso'.format(nome, peso, altura))
elif imc <= 40:
    print('Nome: {}'
          '\nPeso: {}Kg'
          '\nAltura: {}M'
          '\nVocê esta obeso'.format(nome, peso, altura))
elif imc < 0:
    print('Nome: {}'
          '\nPeso: {}Kg'
          '\nAltura: {}M'
          '\nAlgo esta errado com as informações'.format(nome, peso, altura))
else:
    print('Nome: {}'
          '\nPeso: {}Kg'
          '\nAltura: {}M'
          '\nVocê esta com obesidade morbita, se cuide'.format(nome, peso, altura))