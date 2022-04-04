# Fórmula T = Tm + (Tp − Tm) cos [w(t − tp)]

import math

import matplotlib
import numpy as np

# T = média diária
# Tm = temperatura média anual
# Tp = temperatura de pico
# w = frequência anual de variação
w = 2* math.pi /365
# tp = dia médio que ocorre a temperatura de pico
tp = 205

import numpy as np

tm = np.array([22.1, 10.6, 10.7]) #ºC
tp = np.array([28.3, 17.6, 22.9]) #ºC


import matplotlib.pyplot as plt

# Comando para calcular a variação de temperatura entre dois dias do ano
t1 = np.linspace(0, 59, 1)
t2 = np.linspace(180,242,1)
w = (2*np.pi)/365
t1 = np.arange(3)
t2 = np.arange(3)

ta = tm + (tp - tm) * np.cos([w * (t1 - tp)])
#print(ta)

tb = tm + (tp - tm) * np.cos([w * (t2 - tp)])
#print(tb)

# Não consegue calcular porque certas incógnitas são arrays (sequências) e outras são constantes
# Cálculo não pode ser realizado

# Gráficos:
x = np.linspace(0, 59, 1)
x = np.arange(3)
# x = temperaturas entre 320 e 350 kelvin
plt.xlabel(' Mês ')
plt.ylabel(input('Inserir nome do eixo y: '))
y = tm + (tp - tm) * np.cos([w * (x - tp)])
matplotlib.pyplot.plot(x, y)
plt.show()
