cont = 0
numero = 0
soma = 0
numero = int(input('Digite um numero: '))
while numero != 999:
    soma += numero
    cont +=1
    numero = int(input('Digite um numero: '))
print('Voce digitou {} numeros e a soma total deles é {}!'.format(cont, soma))