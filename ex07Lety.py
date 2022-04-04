#Nivel 2 ex1
import sys
import numpy as np

# Temperatura em Kelvin
T = np.array([250., 300., 350., 400.])
# Condutividade Térmica
Kp = np.array([22.3e-3, 26.3e-3, 30.0e-3, 33.8e-3])
# Massa específica ( em quilograma por metro cúbico )
p = np.array([1.3947, 1.1614, 0.9950, 0.8711])
# Capacidade calorífica ( em Jaulo por quilograma Kelvin )
cp = np.array([1006.0, 1007.0, 1009.0, 1014.0])
# Viscosidade ( Newton segundo por metro quadrado )
u = np.array([159.6e-7, 184.6e-7, 208.2e-7, 230.1e-7])

def temperatura(x,y,z):
    if (x <= 400 and x > 350):
        h = ((((y[3] - x)(z[3] - z[2])) / (y[3] - y[2])) - z[3])(-1)
    if (x <= 350 and x > 300):
        h = ((((y[2] - x) * (z[2] - z[1])) / (y[2] - y[1])) - z[2]) * (-1)
    if (x <= 300 and x >= 250):
        h = ((((y[1] - x) * (z[1] - z[0])) / (y[1] - y[0])) - z[1]) * (-1)
    return h

x = float(input('Informe a temperatura (Entre 250.K e 400.K): '))
if x < T[0] or x > T[-1]:
    print('Temperatura de entrada incompatível com dados tabelados')
    print(f'Dados tabelados entre {T[0]}K e {T[-1]}K')
    sys.exit()

while True:
    z = int(input('Escolha uma opção: '
                        '\n(1) - Massa Especifica'
                        '\n(2) - Capacidade Calorofica'
                        '\n(3) - Viscosidade'
                        '\n(4) - Condutividade Termica'
                        '\n(5) - Sair\n'))
    if z == 1:
        print(f'A massa especifica é {temperatura(x, T, p)}')
    if z == 2:
        print(f'A capacidade calorófica é {temperatura(x, T, cp)}')
    if z == 3:
        print(f'A viscosidade é {temperatura(x, T, u)}')
    if z == 4:
        print(f'A condutividade térmica é {temperatura(x, T, Kp)}')
    if z == 5:
        sys.exit()

    continuar = str(input('Deseja continuar?[S/N]'))
    if continuar in 'Nn':
        break



