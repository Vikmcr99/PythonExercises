ptermo = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
dec = ptermo + (10-1) * razao
for c in range (ptermo, dec+1, razao):
    print(c, end=' ')