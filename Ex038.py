n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))

if n1 > n2:
    print('O numero {:.2f} é maior que o numero {:.2f}'.format(n1,n2))
elif n2 > n1:
    print('O numero {:.2f} é maior que o numero {:.2f}'.format(n2,n1))
elif n1 == n2 or n2 == n1:
    print('Os numeros {} e {} são iguais'.format(n1,n2))
else:
    print('Você não digitou um numero valido')