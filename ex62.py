numeros = list()
numerospares = list()
numerosimpares = list()
while True:
    n = int(input('Digite um numero: '))
    numeros.append(n)
    if n % 2 == 0:
        numerospares.append(n)
    else:
        numerosimpares.append(n)
    parar = input('Deseja parar?[S/N]')
    if parar in 'Ss':
        break

print(f'A lista dos seus numeros é: {numeros}')
print(f'A lista com valores pares é {numerospares}')
print(f'A lista com os valores impares é {numerosimpares}')