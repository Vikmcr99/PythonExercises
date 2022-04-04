val = float(input('Qual o valor das compras? '))
print('Como voce deseja pagar?')
print('''[1] A vista (Dinheiro/Cheque)
[2] A vista Cartao
[3] 2x no Cartao
[4] 3x ou mais no Cartao''')
opcao = int(input('Qual a sua opção? '))
if opcao == 1:
    desc = val - (val *0.10)
    print('O valor final com os descontos é de R${}'.format(desc))
elif opcao ==2:
    desc = val - (val * 0.05)
    print('O valor final com os descontos é de R${}'.format(desc))
elif opcao == 3:
    desc = val
    print('O valor final com os descontos é de R${}'.format(desc))
else:
    juros = val + (val * 0.20)
    print('O valor final com os descontos é de R${}'.format(juros))
