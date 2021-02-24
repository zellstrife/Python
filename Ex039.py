nome = str(input('Escreva seu nome: '))
idade = int(input('Escreva a sua idade: '))
sexo = input('Escolha seu sexo (M ou F): ')
tAlis =  18 - idade
if sexo.upper() == 'M':
    if idade == 18:
        print('{} esta na hora de você se alistas !'.format(nome))
    elif idade > 18:
        print('{} você já passou da idade de se alistar, vá se alistar o mais rapido possivel !!'.format(nome))
    else:
        print('{}, Você ainda não tem idade para se alistar, espere mais {} anos'.format(nome, tAlis))
elif sexo.upper() == 'F':
 cert = str(input('Você irá querer entrar para o exercicito ? (Sim ou não): '))

if cert.upper() == 'SIM' and idade == 18:
    print('{} esta na hora de você se alistas !'.format(nome))
elif cert.upper() == 'SIM' and idade > 18:
    print('{} você já passou da idade de se alistar, vá se alistar o mais rapido possivel !!'.format(nome))
elif cert.upper() == 'SIM' and idade < 18:
    print('{}, Você ainda não tem idade para se alistar, espere mais {} anos'.format(nome, tAlis))
else:
    print('Sua escolha é opcional, Você não deseja participar do exercito')
