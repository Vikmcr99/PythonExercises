from datetime import date
atual = date.today().year
cont = 0
contmenores = 0
for c in range(1,8):
    nasc = int(input('Em que ano a {} pessoa nasceu? '.format(c)))
    idade = atual - nasc
    if idade >= 18:
        cont +=1
    else:
        contmenores+=1
print('Ao todo temos {} pessoas maiores de idade e {} menores de idade!'.format(cont, contmenores ))