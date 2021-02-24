num = int(input('Escolha um numero inteiro:'))
conv = int(input('Digite a opção que você quer convertar o numero'
                 '\n 1 - Binario'
                 '\n 2 - Hexadecimal'
                 '\n 3 - Octal'
                 '\nEscolha: '))

if conv == 1:
    print('O numero {} em binário é: {}'.format(num, bin(num)[2:]))
elif conv == 2:
    print('O numero {} em Octal é: {}'.format(num, oct(num)[2:]))
elif conv == 3:
    print('O numero {} em Hexadecimal é: {}'.format(num, hex(num)[2:]))
else:
    print('O numero escolhido é um numero invalido')