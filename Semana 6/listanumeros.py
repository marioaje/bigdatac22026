# -*- coding: utf-8 -*-

# Con una lista de números del 1 al 10. Determine:
# La suma de todos los números usando una función.
# Encontrar la lista de números pares usando una función.
# Contar cuántos números son mayor que un número “x”.

import numpy as np
import sys

numeros = np.array([ 1,2,3,4,5,6,7,8,9,10])

#La suma de todos los números usando una función.
def sumar_numeros(listaArreglo):
    return np.sum(listaArreglo)

# Encontrar la lista de números pares usando una función.
def obtener_pares(listaArreglo):
    return listaArreglo[listaArreglo % 2 == 0 ]

# Contar cuántos números son mayor que un número “x”.
def contar_mayores_x(listaArreglo, x):
    return np.sum(listaArreglo > x)

print("Lista:", numeros)
print("La suma de todos los números:", sumar_numeros(numeros))
print("Encontrar la lista de números pares:", obtener_pares(numeros))
print("Contar cuántos números son mayor que un número “x”:", contar_mayores_x(numeros, 6))