fr = input('Digite uma frase: ').strip()

print('A frase escolhida foi: {}'
      '\nNesta frase tem: {} "A"s'
      '\nO primeiro A esta na posição: {}'
      '\nO ultimo A esta na posição: {}'.format(fr,fr.upper().count('A'), fr.upper().find('A')+1, fr.upper().rfind('A')+1))