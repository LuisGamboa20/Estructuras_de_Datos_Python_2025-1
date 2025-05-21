# Crear un conjunto (set) de números
numeros = {2, 3, 4, 1}

# Mostrar el conjunto de números
print("Conjunto de números:", numeros)

# Agregar un número al conjunto
numeros.add(5)
print("Después de agregar 5:", numeros)

# Intentar agregar un número que ya está en el conjunto
numeros.add(3)
print("Después de intentar agregar 3 nuevamente:", numeros)

# Eliminar un número del conjunto
numeros.remove(2)
print("Después de eliminar 2:", numeros)

# Verificar si un número está en el conjunto
if 4 in numeros:
    print("El número 4 está en el conjunto de números.")