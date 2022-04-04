from time import sleep
def contador(inicio, fim, passo):
    print()
    print(f'Contagem de {inicio} ate {fim} pulando de {passo} em {passo}')
    for c in range (inicio, fim + 1, passo):
        sleep(0.5)
        print(c, end=' ')

contador(1,10,1)
contador(10,0,-2)
print()
print('Agora a sua vez de definir!')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)