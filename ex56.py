num = (int(input('Digite um numero: ')),int(input('Digite um numero: ')),int(input('Digite um numero: ')),
       int(input('Digite um numero: ')))
print(num)
print(f'O 9 apareceu {num.count(9)} vezes')
if 3 in num:
       print(f'O valor 3 apareceu na {num.index(3)+1} posição')
else:
       print('O valor 3 não foi digitado')
print('Os valores pares digitados sao: ')
for n in num:
       if n%2==0:
              print(f'{n}',end=' ')
