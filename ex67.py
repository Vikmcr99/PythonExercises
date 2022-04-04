from random import randint
mega = list()
lista = list()
jogos = int(input('Quantos jogos voce quer que eu sorteie? '))
for c in range(0,jogos):
    for l in range (1,7):
        pc = randint(1, 60)
        if pc not in mega:
            mega.append(pc)
    lista.append(mega[:])
    mega.clear()
lista.sort()
print(lista)

