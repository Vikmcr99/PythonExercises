pessoas = list()
dados = list()
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) ==0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1]< menor:
            menor = dados[1]

    pessoas.append(dados[:])
    dados.clear()
    parar = str(input('Deseja parar?[S/N]'))
    if parar in 'Ss':
        break
print(pessoas)
print(f'Voce cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi {maior} e o menor foi {menor}')