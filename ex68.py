from random import randint
from time import sleep
from operator import itemgetter
ranking = list()
jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)}
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-'*45)
print('O ranking foi:')
sleep(1)
for i, v in enumerate(ranking):
    print(f'{i + 1} lugar foi o {v[0]} com {v[1]}')