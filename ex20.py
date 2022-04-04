from datetime import date
ano = int(input('Digite um ano qualquer para verificar se o mesmo é bissexto: Digite 0 para verificar sobre o ano atual:'))
if ano == 0:
    ano = date.today().year
if ano % 4 ==0:
    print('O ano é bissexto!')
else:
    print('O ano nao é bissexto')