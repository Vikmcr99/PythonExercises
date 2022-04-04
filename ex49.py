from random import randint
from time import sleep
cont = 0
while True:
    parimpar = str(input('PAR OU IMPAR? ')).upper()
    if parimpar == 'PAR':
        num = int(input('Jogue um numero: '))
        computador = randint(0, 10)
        print('O computador jogou.....')
        sleep(1)
        print(computador)
        if (num + computador) % 2 == 0:
            cont +=1
            print('Voce Ganhou!')
        else:
            print('Vixe... Voce perdeu')
            break
    elif parimpar == 'IMPAR':
        num = int(input('Jogue um numero: '))
        computador = randint(0, 10)
        print('O computador jogou.....')
        sleep(1)
        print(computador)
        if (num + computador) % 2 == 0:
            print('Voce Perdeu!')
            break
        else:
            print('Voce ganhou!')
            cont +=1

print(f'Voce ganhou {cont} vezes!')