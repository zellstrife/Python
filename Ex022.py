nome = str(input('Escreva o nome da pessoa a ser analisada: '))

lNome = nome.split()

print('O nome a ser analisado é: {}'
      '\nNome todo em maisculo: {}'
      '\nNome todo em minisculo: {}'
      '\nQuantas letras tem no nome: {}'
      '\nQuantas letras tem o primeiro nome: {}'.format(nome,nome.upper(),nome.lower(),len(nome)-nome.count(" "),len(lNome[0])))