while True:
    numero = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco',
              'seis','sete','oito','nove','dez','onze','doze',
              'treze', 'catorze','quinze', 'dezesseis','dezesete', 'dezoito',
              'dezenove','vinte')
    numuser = int(input('Digite um numero entre 0 e 20: '))
    if numuser>20:
        break
    else:
        print(numero[numuser])
print('Fim')