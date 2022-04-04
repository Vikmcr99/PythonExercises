listanum = []
for c in range (0,5):
    listanum.append(int(input(f'Digite um valor para a posicao {c}:')))
    if c ==0:
        maior = listanum[0]
        menor = listanum[0]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print(listanum)
print(f'O maior valor foi {maior}, e o menor foi {menor}')