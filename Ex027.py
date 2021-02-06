nome = str(input('Digite seu nome completo: '))

n = nome.split()

print('O nome escolhido foi: {}'
      '\nO primeiro nome é: {}'
      '\nO ultimo nome é: {}'.format(nome, n[0], n[len(n)-1]))