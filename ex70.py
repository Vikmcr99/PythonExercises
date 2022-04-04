jogador = dict()
jogador['nome'] = str(input('Nome do jogador: '))
jogador['jogos'] = int(input(f"Quantos jogos {jogador['nome']} jogou?  "))
cont = 1
gols = list()
while cont <= jogador['jogos']:
    gols.append(int(input(f'Quantos gols na partida {cont}? ')))
    cont+=1
    jogador['gols'] = sum(gols)

print(jogador)