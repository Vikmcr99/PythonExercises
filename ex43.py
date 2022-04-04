ptermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <=total:
        print('{}--'.format(ptermo),end='')
        ptermo +=razao
        cont+=1
    mais = int(input('\nQuantos termos voce quer ver mais? '))
print('Fim')