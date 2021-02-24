import datetime
nome = str(input('Qual o nome do atleta: '))
ano = int(input('Qual o ano de nascimento do atleta: '))
teste = int(datetime.datetime.today().year)
idade = teste - ano

if idade < 0:
    print('Inesxistente ou você veio do futuro')
elif idade >= 0 and idade <= 9:
    print('Atleta: {}'
          '\nIdade: {}'
          '\nClasse: Mirim'.format(nome,idade))
elif idade <= 14:
    print('Atleta: {}'
          '\nIdade: {}'
          '\nClasse: Infantil'.format(nome,idade))
elif idade <= 19:
    print('Atleta: {}'
          '\nIdade: {}'
          '\nClasse: Junior'.format(nome,idade))
elif idade == 20:
    print('Atleta: {}'
          '\nIdade: {}'
          '\nClasse: Senior'.format(nome,idade))
elif idade > 120:
    print('Volta pro museu, mumia')
else:
    print('Atleta: {}'
          '\nIdade: {}'
          '\nClasse: Master'.format(nome,idade))