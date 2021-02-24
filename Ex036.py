salario = float(input('Digite o seu slario: '))
vCasa = float(input('Digite o valor da casa: '))
anos = float(input('Quantos anos irá ser parcelado:  '))

vMensal = vCasa / (anos * 12)
pSal = salario * 0.30

if pSal < vMensal:
    print('Senho cliente'
          '\nSeu salario é de: {}'
          '\nO valor da casa é de: R${}'
          '\nVocê escolheu pagar em até: {} anos'
          '\nNão será possivel liberar o empréstimo'.format(salario,vCasa,anos))
else:
    print('Senho cliente'
          '\nSeu salario é de: {}'
          '\nO valor da casa é de: R${}'
          '\nVocê escolheu pagar em até: {} anos'
          '\nParabens o emprestimo irá ser liberado'.format(salario,vCasa,anos))