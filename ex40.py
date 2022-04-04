from random import randint
computador = randint(0,10)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpites += 1
    if jogador == computador:
        print('Acertou!')
        print('Foram {} tentativas!'.format(palpites))
        break;
    else:
        print('Nossa, vc errou!')