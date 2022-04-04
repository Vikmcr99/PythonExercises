
import numpy as np
import matplotlib.pyplot as plt
TmM = 22.1
TmS = 10.6
TmB = 10.7

TpM = 28.3
TpS = 17.6
TpB = 22.9

tp = 205

w = 2* np.pi /365

t = np.array([0,59])

TM = TmM + (TpM - TmM) * np.cos(np.array([w * (t- tp)]) )# Temperatura Miami
TS = TmS + (TpS - TmS) * np.cos(np.array([w * (t-tp)]) )# Temperatura Seatle
TB = TmB + (TpB - TmB) * np.cos(np.array([w * (t-tp)])) # Temperatura Boston

plt.plot(t,TM,label = '$ TM - Miami$')
plt.plot(t,TS,label= '$ TS - Seatle$')
plt.plot(t,TB,label= '$ TB - Boston $')
plt.title('Temperatura Diária de Cidades Americanas ')
plt.xlabel('Dia do ano ')
plt.ylabel('Temperatura Diária ')
plt.legend()
plt.grid(True)
#matplotlib.pyplot.plot(x, y)
plt.show()

t2 = np.array([180,242])

plt.plot(t2,TM,label = '$ TM - Miami$')
plt.plot(t2,TS,label= '$ TS - Seatle$')
plt.plot(t2,TB,label= '$ TB - Boston $')

plt.title('Temperatura Diária de Cidades Americanas ')
plt.xlabel('Dia do ano ')
plt.ylabel('Temperatura Diária ')
plt.legend()
plt.grid(True)
plt.show()

deltaTM = TM[-1] - TM[0]
deltaTS = TS[-1] - TS[0]
deltaTB = TB[-1] - TB[0]

print(deltaTM)
print(deltaTS)
print(deltaTB)

