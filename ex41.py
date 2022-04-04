n1 = int(input('Digite o 1 valor: '))
n2 = int(input('Digite o 2 valor: '))
opcao = 0
while opcao !=5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos numeros
    [5] Sair''')
    opcao = int(input('Qual sua opcao? '))
    if opcao ==1:
        print('A soma é {}'.format(n1 + n2))
    elif opcao ==2:
        print('A multiplicação é {}'.format(n1*n2))
    elif opcao ==3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior é {}'.format(maior))
    elif opcao ==4:
        print('Novos numeros....')
        n1 = int(input('Digite o 1 valor: '))
        n2 = int(input('Digite o 2 valor: '))
    elif opcao ==5:
        break;
    else:
        print('Opcao invalida!')

print('Programa encerrado!')