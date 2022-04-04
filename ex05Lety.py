#ex 1 nivel 2
while True:
    DRE = int(input('Insira seu DRE: '))
    if DRE < 0:
        break
    P1 = int(input('Insira valor da Prova 1: '))
    P2 = int(input('Insira valor da Prova 2: '))
    val = [DRE, P1, P2]
    Mf = (P1 + P2) / 2
    if Mf >= 7.0:
        print(f'Sua média é {Mf} e voce passou direto.')
    elif 3.0 < Mf < 7.0:
        print(f'Sua média é {Mf} e voce precisa realizar a prova final')
    else:
        print(f'Sua média é {Mf} e voce foi reprovado sem chance da realização da prova final')

print('Programa finalizado!')
#print(val)