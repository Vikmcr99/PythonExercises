#nivel 4 ex 2
import math
import sys
import matplotlib.pyplot as plt

# Temperatura em graus celsius
Tb = 25
# Pressão em atm
PressãoB = 1
# em metros
D = 0.01
L = 1.3
#Coeficiente de difusão em metros ao quadrado por segundo
DAB = 26e-6
#Densidade específica de A na condição de saturação
pas = 0.0226
#Massa específica do ar
pb = 1.17
#Viscosidade dinâmica do ar em Newton
mib = 183.6e-7

pain = 0


m = float(input("Digite o valor da taxa mássica: "))
T = float(input('Informe a temperatura(ºC): '))

# Valor de Red
Red = (4*m)/(math.pi*D*mib)
Sc = (mib)/(pb*DAB)

print(f'Red = {Red}')

if 10 < Red < 2000:
    hm = (1.86*((D/L)*Red*Sc)**1/3)*(DAB/D)
    print('-'*40)
    print ("Você está em regime laminar!")
elif 2000 < Red < 35000:
    hm = 0.023*(Red**0.83)*(Sc**0.44)*(DAB/D)
    print('-' * 40)
    print ( "Você está em regime turbulento!")
else:
    print('-' * 40)
    print('Não foi possivel calcular este valor!')
    sys.exit()

pout = - (((pas - pain)*(math.exp(-(math.pi*D*L)/(m/pb))*hm)) - pas)

print('-'*40)
print ( f"O resultado da concentração mássica de água na saida é {pout}")

#4(a)
plt.xlabel('Taxa massica')
plt.ylabel(' concentração mássica de água na saída')

m = 1.2e-3
out = (pout * T)
x = [0,m]
y = [0, out]
plt.plot(x, y)
plt.title('Variação da concentração massica')
plt.show()

#4(b)
m = [1.5e-5, 1.5e-3]
T = 25
x = [0, T]
y = [0, pout]
#out = m * pout
plt.xlabel('Temperatura')
plt.ylabel(' concentração mássica de água na saída')
plt.plot(x, y )
plt.title('Variação da concentração massica')
plt.show()