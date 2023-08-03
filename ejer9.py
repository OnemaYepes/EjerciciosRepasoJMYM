import numpy as np
import random

filas = int(input("Ingrese el # de filas de la matriz: "))
columnas = int(input("Ingrese el # de columnas de la matriz: "))

matriz = np.zeros((filas,columnas))

for i in range(0,filas):
    for j in range(0,columnas):
        matriz[i,j] = int(random.random()*1000)

print(matriz)