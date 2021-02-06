import random

n1 = random.randint(1,10000)
n2 = random.randint(1,10000)
n3 = random.randint(1,10000)

maior = int(0)
menor = int(0)

if(n1 > n2 and n1 > n3):
    maior = n1
elif(n2 > n1 and n2 > n3):
    maior = n2
else:
    maior = n3

if(n1 < n2 and n1 < n3):
    menor = n1
elif(n2 < n1 and n2 < n3):
    menor = n2
else:
    menor = n3

print('Os numeros escolhido foram: {} , {} , {}'
      '\n O maior numero é: {}'
      '\n O menor numero é: {}'.format(n1,n2,n3,maior,menor))