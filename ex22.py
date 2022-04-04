print("Verificador de triangulos:")
r1 = int(input('Digite um valor:'))
r2 = int(input('Digite um valor:'))
r3 = int(input('Digite um valor:'))
if r1 < r2 + r3 and r2<r1+r3 and r3< r1 + r2:
    print('O triangulo pode ser formado')
else:
    print("n pode formar um triangulo!")