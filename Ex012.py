n=float(input('Digite o valor da compra: '))
desc=5
vDesc= n*(desc/100)
print('Valor da Compra é de : R${}'
      '\nO desconto foi de: {}%'
      '\nO desconto é de: R${}'
      '\n Valor atualizado: R${}'.format(n,desc,vDesc,n-vDesc))