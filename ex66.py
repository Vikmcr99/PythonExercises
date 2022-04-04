matriz = [[0,0,0], [0,0,0], [0,0,0]]
par = ter = mai = 0
for c in range (0,3):
    for l in range (0,3):
        matriz[c][l]= int(input(f'Digite um valor para [{c}], [{l}]: '))
        if matriz[c][l]%2==0:
            par+=matriz[c][l]
        if matriz[c][2]:
            ter += matriz[c][2]
        if matriz[1][l]:
             mai = matriz[1][l]
        elif matriz[1][l] > mai:
            mai = matriz[1][l]
print('-='*30)
for c in range (0,3):
    for l in range(0,3):
        print(f'[{matriz[c][l]:^4}]',end = '')
    print()
print('-='*30)
print(f'A soma dos valores pares é: {par}')
print(f'A soma dos valores da terceira coluna é: {ter}')
print(f'O maior valor da segunda linha é {mai}')