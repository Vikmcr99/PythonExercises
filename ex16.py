from random import randint
comp= randint(0,5)
print('Tente advinhar o numero que estou pensando!')
user=int(input('Digite um numero de 1 a 5:'))
if user ==comp:
    print("Eu pensei no numero {} e voce acertou!".format(comp))
else:
    print('Eu pensei no numero {} e voce errou!'.format(comp))
