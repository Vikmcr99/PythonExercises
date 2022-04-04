numeros = list()
cont = 0
while True:
    numeros.append(int(input('Digite um numero: ')))
    cont +=1
    parar = str(input('Deseja parar?[S/N]')).strip().upper()[0]
    if parar == 'S':
        break
numeros.sort(reverse=True)
print(numeros)
print(f'Foram digitados {cont} numeros')
if 5 in numeros:
    print('o valor 5 está na lista')
else:
    print('O valor 5 não foi digitado')
