# Exercício 2 do Nível 3
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

Tr =  100 + 2.5 * (np.cos(x))

# Gerar gráfico:
plt.plot(x, y)
plt.show()

if (Tr > 50).all():
    plt.close()
    print(f'Falha! A temperatura dos reatores ultrapassaram o limite de 50ºC')

# Legenda para o gráfico
plt.title('Solução da temperatura ao longo do tempo')
plt.legend()# Exercício 2 do Nível 3
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

Tr =  100 + 2.5 * (np.cos(x))

# Gerar gráfico:
plt.plot(x, y)
plt.show()

if (Tr > 50).all():
    plt.close()
    print(f'Falha! A temperatura dos reatores ultrapassaram o limite de 50ºC')

# Legenda para o gráfico
plt.title('Solução da temperatura ao longo do tempo')
plt.legend()