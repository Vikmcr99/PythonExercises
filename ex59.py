numeros = []
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
    else:
        print('Este valor ja existe na lista!')
    r = str(input('Deseja parar?[S/N]')).upper()
    if r == 'S':
        break
numeros.sort()
print(numeros)
