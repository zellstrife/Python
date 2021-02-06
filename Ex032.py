from datetime import date
ano = int(input('Qual é o ano [Coloque 0 para analisar o ano atual: '))


if(ano == 0 ):
    ano = date.today().year


if(ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 ):
    print('Ano: {}'
          '\nO ano é Bissexto'.format(ano))
else:
    print('Ano: {}'
          '\nO ano não é Bissexto'.format(ano))