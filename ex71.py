pessoas = dict()
lista = list()
acima = list()
cont = 1
soma =  0
while True:
    pessoas['nome'] = str(input('Nome: '))
    pessoas['sexo'] = str(input('Sexo[M/F]: '))
    if pessoas['sexo'] not in 'MmFf':
        print('ERRO! Responda apenas com M ou F')
        pessoas['sexo'] = str(input('Sexo[M/F]: '))
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    lista.append(pessoas.copy())
    parar = str(input('Deseja parar?[S/N] '))
    if parar in 'Ss':
        break
    elif parar not in 'SsNn':
        print('ERRO! Responda apenas com S ou N')
        parar = str(input('Deseja parar?[S/N] '))
    cont +=1
    pessoas.clear()
media = soma / cont
print(lista)
print('-'*40)
print(f'Foram cadastradas {cont} pessoas')
print(f'A media de idade é {media:.2f}')
print(f'As mulheres cadastradas foram: ')
for p in lista:
    if p['sexo'] in 'Ff':
        print(f'     =>{p["nome"]}')
for m in lista:
    if m['idade'] > media:
        acima.append(m['nome'])
print(f'As pessoas com a idade acima da media foram: ')
print(acima)