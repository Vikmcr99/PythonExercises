jogador = dict()
jogadores = list()
while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    jogador['jogos'] = int(input(f"Quantos jogos {jogador['nome']} jogou?  "))
    cont = 1
    gols = list()
    while cont <= jogador['jogos']:
        gols.append(int(input(f'Quantos gols na partida {cont}? ')))
        cont+=1
        jogador['gols'] = sum(gols)
    jogadores.append(jogador.copy())
    jogador.clear()
    parar = str(input('Deseja parar?[S/N]: '))
    if parar in 'Ss':
        break
print('*'*45)
print('cod ',end='')
print('                gols: ',end='')
print('         total ',end='')
for k in jogador.keys():
    print(f'{k:<15}',end='')
print()
print('*'* 45)
for i , v in enumerate(jogadores):
    print(f'{i+1:>3} ',end='')
    for d in v.values():
        print(f' {d:<15}',end='')
    print()
print('*'* 45)