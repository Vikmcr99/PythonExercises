def leiaInt(msg):
    ok = False
    valor = 0
    while ok == False:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mErro! Numero Invalido!!!!\033[m')
    return valor


n = leiaInt('Digite um numero: ')
print(f'Voce acabou de digitar o numero {n}')