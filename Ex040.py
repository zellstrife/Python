aluno = str(input('Digite o nome do aluno: '))
p1 = float(input('Digite a nota da P1 do aluno {}: '.format(aluno)))
p2 = float(input('Digite a nota da P2 do aluno {}: '.format(aluno)))
p3 = float(input('Digite a nota da P3 do aluno {}: '.format(aluno)))
p4 = float(input('Digite a nota da P4 do aluno {}: '.format(aluno)))

media = (p1+p2+p3+p4)/4

if media >= 0 and media < 5:
    print('Aluno: {}'
          '\n Você esta REPROVADO com a média final de: {}'.format(aluno, media))
elif media >= 5 and media < 7:
    print('Aluno: {}'
          '\n Você esta RECUPERAÇÃO com a média final de: {}'
          '\nEstude mais e você conseguirá !!!'.format(aluno, media))
elif media >= 7 and media <= 10:
    print('Aluno: {}'
          '\n Você esta APROVADO com a média final de: {}'
          '\n Parabens, vejo você no proximo ano'.format(aluno, media))
else:
    print('Analise novamente as notas, os valores estão errados')