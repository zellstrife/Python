a = float(input('Digite o valor do lado do trinagulo: '))
b = float(input('Digite o valor do lado do trinagulo: '))
c = float(input('Digite o valor do lado do trinagulo: '))

if(b-c < a and a < b+c and a-c < b and b < a+c and a-b < c and c < a+c):
    print('Com os lados inseridos é possivel ser criado um triangulo')
else:
    print('Com os lados inseridos não é possivel ser criado um triangulo')