def maior(*num):
    cont = maior = 0
    print()
    print('Analisando os valores....')
    for valor in num:
        print(f'{valor}',end=' ')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor

        cont+=1
    print()
    print(f'Foram informados {cont} valores e o maior deles foi o {maior}')

maior(2,4,6,10,15,3)
maior(1,8,6,4,5,10)
maior(1,10)
maior(6)
