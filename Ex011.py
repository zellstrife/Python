alt = float(input('Quantos metros de altura tem a parede: '))
larg = float(input('Quantos metros de largura tem a parede: '))
area = alt * larg

print('A largura da parede é: {}'
      '\nA altura da parede é: {}'
      '\nA Area total é: {}'
      '\n Será necessario {} litros de tinta para pintar a parede'.format(larg,alt,area,area/2))