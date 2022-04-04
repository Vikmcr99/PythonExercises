num = int(input('Digite um numero: '))
cont = 0
for c in range(1,num+1):
    print(c, end =' ')
    if num % c ==0:
        cont +=1
if cont ==2:
    print(' O numero {} só foi divisivel {} vezes, por isso é primo'.format(num,cont))
else:
    print(' O numero {} foi divisivel {} vezes, por isso não é primo'.format(num,cont))




