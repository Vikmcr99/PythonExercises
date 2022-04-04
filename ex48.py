while True:
    num = int(input('Digite um numero para ver sua tabuada: '))
    if num < 0:
        break
    for cont in range(1,11):
     print(f'{num} X {cont} = {num*cont}')
print('Fim')

