import random
km = random.randint(1,2000)

if(km <= 200):
    print('Sua viagem foi de {}Km'
          '\n O total a pagar é de {} Reais: '.format(km,km*0.50))
else:
    print('Sua viagem foi de {}Km'
          '\n O total a pagar é de {} Reais: '.format(km, ((km-(km-200)) * 0.50) + ((km - 200)*0.45)))