maior = 0
menor = 0
for c in range(1,6):
    peso = float(input('Peso da {}ª pessoa(kg): '.format(c)))
    if c ==1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O maior peso foi {}, e o menor foi {}'.format(maior, menor))
