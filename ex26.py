from datetime import date
atual = date.today().year
nasc = int(input('Data de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em 2021'.format(nasc, idade))
falt = 18 - idade
alist = atual + falt
if idade < 18:
    print('Ainda faltam {} anos para seu alistamento.'.format(falt))
    print('Seu alistamento sera em {}!'.format(alist))
elif idade == 18:
    print('Seu alistamento é esse ano!')
else:
    print('Seu alistamento deveria ter sido em {}!'.format(alist))