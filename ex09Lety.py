# Importanto o módulo numpy
import numpy as np

# Definição da função de interpolação
def interpol (x,y,z):
    if (x > 400 or x < 250):
        print ( " Este valor está fora do intervalo dado ")
        quit()
    if (x <= 400 and x > 350 ):
        h = ((((y[3]-x)(z[3]-z[2]))/(y[3]-y[2]))-z[3])(-1)
    if (x <= 350 and x > 300 ):
        h = ((((y[2] - x) * (z[2] - z[1])) / (y[2] - y[1])) - z[2]) * (-1)
    if (x <= 300 and x >= 250 ):
        h = ((((y[1] - x) * (z[1] - z[0])) / (y[1] - y[0])) - z[1]) * (-1)
    return h

# Temperatura ( em Kelvin )
T = np.array([250.0, 300.0, 350.0, 400.0])

# Massa específica ( em quilograma por metro cúbico )
p = np.array([1.3947, 1.1614, 0.9950, 0.8711])

# Capacidade calorífica ( em Jaulo por quilograma Kelvin )
cp = np.array([1006.0, 1007.0, 1009.0, 1014.0])

# Viscosidade ( Newton segundo por metro quadrado )
u = np.array([159.6e-7, 184.6e-7, 208.2e-7, 230.1e-7])

# Condutividade Térmica ( em Watts por metro kelvin )
k = np.array([22.3e-3, 26.3e-3, 30.0e-3, 33.8e-3])

# Definindo a variável x e z
x = float(input(" Digite uma temperatura entre 250 e 400 K : "))
z = float(input( " Escolha a propriedade: (1) - Massa Específica / (2) - Capacidade Calorífica"
                 " (3) - Viscosidade / (4) - Condutividade Térmica : "))

# Interpolação a partir da escolha da propriedade física
if z == 1:
    q = interpol(x, T, p)
    print( " A massa específica é na temperatura ", x, " é ", q)
if z == 2:
    q = interpol(x, T, cp)
    print(" A capacidade calorífica é na temperatura ", x, " é ", q)
if z == 3:
    q = interpol(x, T, u)
    print(" A viscosidade é na temperatura ", x, " é ", q)
if z == 4:
    q = interpol(x, T, k)
    print(" A condutividade térmica é na temperatura ", x, " é ", q)