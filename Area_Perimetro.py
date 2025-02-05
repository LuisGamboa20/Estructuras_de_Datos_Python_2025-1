# A travez de los ejercicios planteados el estudiante debera identificar resultados datos y procesos
# adicional a ello debera explicar cada una de las instrucciones escritas dentro del codigo y su proposito
# en el mismo#

# Ejercicio 1 por el cual se halla el perimetro de un triangulo


# Se define la funcion calcular_perimetro que recibe 3 parametros a, b y c

def calcular_perimetro(a, b, c):
    return a + b + c

# Se solicita al usuario que ingrese el valor de los lados del triangulo

lado = float(input("Ingrese el valor del lado 1: "))
lado2 = float(input("Ingrese el valor del lado 2: "))
lado3 = float(input("Ingrese el valor del lado 3: "))

# Se llama a la funcion calcular_perimetro y se le pasan los valores de los lados del triangulo

perimetro = calcular_perimetro(lado, lado2, lado3)

# Se imprime el valor del perimetro del triangulo

print(f"El perimetro del triangulo es: {perimetro}")