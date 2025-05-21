import random
import time

def busqueda_binaria(lista,objetivo):
    inicio, fin = 0, len(lista) - 1
    while inicio <= fin:
        medio = int((inicio + fin)/2)
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin: medio - 1
            return -1
        
n = 10 ** 6
datos = sorted(random.sample(range(n*10), n))
objetivo = random.choice(datos)

inicio  = time.time()
busqueda_binaria(datos,objetivo)
fin = time.time()
tiempo_binario = fin - inicio

print(f"Busqueda binaria (O(log n)): {tiempo_binario:.6f} segundos")