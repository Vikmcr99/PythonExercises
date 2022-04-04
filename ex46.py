resp = 'S'
cont = 0
num = 0
soma = 0
maior = 0
menor = 0
while resp == 'S':
    num = int(input('Digite um numero: '))
    cont+=1
    soma += num
    resp = str(input(('Deseja continuar? [S/N] '))).upper()
    if cont == 1:
        maior = menor = num
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
media = soma/cont
print('Voce digitou {} numeros, e a media entre eles é {:.2f}'.format(cont, media))
print('O maior numero foi {}, e o menor foi {}.'.format(maior, menor))