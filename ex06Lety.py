# Exercício 2 do Nível 2
# Docente: Luiz Fernando
# Autora: Letícia Sieira Chaves
import numpy as np
import matplotlib.pyplot as plt

V = 10 # m ** 3
m = 10 # Kg/s
Te = 25 # ºC
Tr = 100 # ºC
U = 2000 # W/ ((m**2) * ºC)
A = 80 # m ** 2
ρ = 1000 # Kg/ m **3
cp = 4180 # J/ (Kg * ºC)

Top = ((m * cp * Te) + (U * A * Tr))/ ((U * A) + (m * cp))

τ = (V * ρ * cp)/ ((m * cp) + (U * A))
T = (Te * np.exp(τ)) + (Top * (1 - np.exp(τ)))

# Formar gráfico a solução da temperatura ao longo do tempo
# ( y = f(x) = T ) -> eixo y
# ( x = x = t ) -> eixo x

x = np.linspace(0, 1000) #chute
plt.xlabel('Tempo (t)')
plt.ylabel('Temperatura (T)')

# Substitui "T" por "y" e "t" por "x":
y = (Te * np.exp(-x/τ)) + (Top * (1 - np.exp(-x/τ)))

# Gerar gráfico:
plt.plot(x, y)
plt.show()

# Legenda para o gráfico
plt.title('Solução da temperatura ao longo do tempo')
plt.legend()

# Peguei isso do Exercício 2 Nível 2 da folha 2 de exercícios Python
# x = np.linspace(320,350)
# x = temperaturas entre 320 e 350 kelvin
# plt.xlabel(' Temperatura (Kº) ')
# plt.ylabel(' Parâmetro Cinético da Reação (s**-1)')
# y = k0 * (e** (-E/(R * x)))
# matplotlib.pyplot.plot(x, y)
# plt.show()
# Exercício 3 não tinha nada que eu pudesse reutilizar