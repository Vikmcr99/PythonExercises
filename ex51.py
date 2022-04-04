tot = 0
maismil = 0
barato = 0
cont=0
nomebarato = ''
while True:
    nome = input('Nome do produto: ')
    preco = float(input('Valor: '))
    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    tot += preco
    cont+=1
    if preco > 1000:
        maismil+=1
    if cont == 1:
        barato = preco
        nomebarato = nome
    else:
        if preco < barato:
            barato = preco
            nomebarato = nome
    if continuar == 'N':
        break
print(f'O total gasto foi {tot}, existem {maismil} produtos acima de mil reais e o produto mais barato foi {nomebarato}')