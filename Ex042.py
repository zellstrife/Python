a = float(input('Digite o valor do lado do trinagulo: '))
b = float(input('Digite o valor do lado do trinagulo: '))
c = float(input('Digite o valor do lado do trinagulo: '))

if(b-c < a and a < b+c and a-c < b and b < a+c and a-b < c and c < a+c):

        if b == c and c == a and a == b:
            print('Com os lados inseridos é possivel ser criado um triangulo'
                '\nEsse é um triangulo EQUILATERO')
        elif a == b or a == c and b == c or b == a and a == b or a == c:
            print('Com os lados inseridos é possivel ser criado um triangulo'
                '\n Esse é um triangulo ISOCELES')
        elif a != b and b != c and c != a:
            print('Com os lados inseridos é possivel ser criado um triangulo'
                '\n Esse é um triangulo ESCALENO')
else:
    print('Com os lados inseridos não é possivel ser criado um triangulo')