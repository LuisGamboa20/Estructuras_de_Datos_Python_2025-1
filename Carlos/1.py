n1 = int(input("Ingrese el primer numero:"))
n2 = int(input("Ingrese el segundo numero:"))

print(f"La suma de los numeros es: {n1 + n2}")
print(f"La resta de los numeros es: {n1 - n2}")
print(f"La multiplicacion de los numeros es: {n1 * n2}")
print(f"La division de los numeros es: {n1 / n2}")


#2 Condicionales

n = int(input("Ingrese un numero:"))

if n > 0:
    print("El numero es positivo")
elif n < 0:
    print("El numero es negativo")
else:
    print("El numero es cero")
    
if n % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")
    
if n % 5 == 0 and n % 3 == 0:
    print("El numero es multiplo de 5 y de 3")
elif n % 3 == 0:
    print("El numero es multiplo de 3")
elif n % 5 == 0:
    print("El numero es multiplo de 5")
else:
    print("El numero no es multiplo de 5 ni de 3")
    
    
#3 Bucles

try:
    n = int(input("Ingrese un numero:"))
    if n < 0:
        raise ValueError("El numero debe ser positivo")
except ValueError as e:
    print(e)      

