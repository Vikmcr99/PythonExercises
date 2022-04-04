contH = 0
contmulher = 0
contidade = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    if sexo == 'M':
        contH +=1
    if idade > 18:
        contidade+=1
    if sexo == 'M' and idade <20:
        contmulher +=1
    continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if continuar == 'N':
        break
print(f'Existem {contidade} pessoas maiores de 18 anos')
print(f'{contH} homens cadastrados')
print(f'{contmulher} mulheres com menos de 20 anos!')
