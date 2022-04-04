from datetime import date
atual = date.today().year
nasc = int(input('Ano do seu nascimento: '))
idade = atual - nasc
print('Voce tem {} anos e sua categoria é: '.format(idade))
if idade <= 7:
    print('Mirim!')
elif idade <=14:
    print('Infantil!')
elif idade <= 19:
    print('Junior')
elif idade <=25:
    print('Senior')
else:
    print('Master')