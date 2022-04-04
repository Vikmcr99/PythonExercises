diametro =int(input('Informe o diametro: '))
user = str(input("Ciclone ou Hidrociclone?")).upper()
if user == 'CICLONE':
    Bc = diametro/4
    De = diametro/2
    Hc = diametro/2
    Lc = diametro*2
    Sc = diametro/8
    Zc = diametro*2
    Jc = diametro/4
    print('os valores das dimensões do equipamento sao:')
    print('Bc = {}, De = {}, Hc = {}, Lc = {}, Sc = {}, Zc = {}, Jc = {}'.format(Bc, De, Hc, Lc, Sc, Zc, Jc))
elif user == 'HIDROCICLONE':
    L = diametro * 5
    B = 0.28 * diametro
    E = 0.34 * diametro
    I =  0.40 * diametro
    print('os valores das dimensões do equipamento sao:')
    print('L = {}, B = {:.2f}, E = {:.2f}, I = {}'.format(L, B, E, I))
else:
    print("ERRO! Voce digitou errado!")





