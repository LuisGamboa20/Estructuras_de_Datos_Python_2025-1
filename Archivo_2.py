# Usando Python elabore un programa que reciba 2 números distintos e indique cuál es el mayor

# Función para comparar dos números
def comparar_numeros(num1, num2):
    if num1 > num2:
        return f"El número {num1} es mayor que el número {num2}"
    else:
        return f"El número {num2} es mayor que el número {num1}"

# Solicitar la entrada del usuario
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Llamado a la función y almacenamiento del resultado
resultado = comparar_numeros(num1, num2)

# Impresión del resultado
print(resultado)