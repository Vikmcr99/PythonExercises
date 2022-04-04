num = int(input('Digite um numero inteiro para a conversao: '))
print('''(1) - Binario 
(2) - Octal 
(3) - Hexadecimal''')
opcao = int(input(''))
if opcao == 1:
    print('Seu numero {} convertido em binario é: {}'.format(num, bin(num)))
elif opcao == 2:
    print('Seu número {} convertido em octal é: {}'.format(num, oct(num)))
elif opcao ==3:
    print('Seu numero {} convertido em Hexadecimal é: {}'.format(num, hex(num)))
else:
    print('OPÇÂO INVALIDA!')
