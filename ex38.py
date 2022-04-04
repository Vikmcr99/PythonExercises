soma = 0
velho = 0
menos = 0
nomevelho=''
for c in range(1,5):
    nome = input('Nome da {}ª pessoa: '.format(c))
    idade = int(input('Idade da {}ª pessoa: '.format(c)))
    sexo = str(input('Sexo da {}ª pessoa [M/F]: '.format(c))).upper()
    soma += idade
    if c ==1:
        velho = idade
        nomevelho=nome
    if sexo == 'M' and idade > velho:
        velho = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        menos +=1

media = soma / 4
print('A média de idade é de {}'.format(media))
print('A pessoa mais velha é {} e tem {} anos'.format(nomevelho, velho))
print('Existem {} mulheres com menos de 20 anos'.format(menos))