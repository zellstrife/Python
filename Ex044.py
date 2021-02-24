tPag = int(input('Tipos de pagamentos'
             '\n1 - Pagamento a vista (Dinheiro ou cheque)'
             '\n2 - Pagemento no cartão'
             '\n3 - Pagamento no cartão em até 2x'
             '\n4 - Pagamento no cartão em até 3x ou mais'
             '\nEscolha a forma de pagamento: '))

preco = float(input('Digite o valor do produto: '))

if tPag == 1:
    print('Forma de pagamento: A vista'
          '\nPreço do produto: R${}'
          '\nTotal com o desconto a vista: {}'.format(preco,preco-(preco*0.10)))
elif tPag == 2:
    print('Forma de pagamento: No cartão'
          '\nPreço do produto: R${}'
          '\nTotal com o desconto a vista: {}'.format(preco,preco-(preco*0.05)))
elif tPag == 3:
    print('Forma de pagamento: No Cartão em 2x sem JUROS'
          '\nPreço do produto: R${}'.format(preco))
elif tPag == 4:
    print('Forma de pagamento: No Cartão em 3x ou mais'
          '\nPreço do produto: R${}'
          '\nTotal com o desconto a vista: {}'.format(preco,preco+(preco*0.20)))
else:
    print('Opção não existe')