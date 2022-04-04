
import numpy as np

v = np.array([[3],[2],[4]])
u = np.array([[3], [4], [8], [6]])
a = np.array([[8, 4, 5, 2], [5, 3, 4, 6], [2, 9, 7, 4], [3, 7, 3, 3]])
b = np.array([[3, 1, 8], [1, 3, 2], [8, 2, 3]])
#multiBU = np.multiply(b, u) impossivel completar a multiplicação pois nao respeita as regras de brodcast (shapes (3,3) (4,1)
#multiUB = np.multiply(u, b) impossivel completar a multiplicação pois nao respeita as regras de brodcast (shapes (4,1) (3,3)
#somaAB = np.add(a, b) o array a é (4,4), enquanto o array b é (3,3)
multiUA = np.multiply(u, a)
somaABel = a[3,0] + b[2,2]
multicolBV= np.multiply(b[1],v )
print(multiUA)
print('-'*20)
print(somaABel)
print('-'*20)
print(multicolBV)

