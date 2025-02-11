# Función para ordenar cuatro números
def sort_four_numbers(n1, n2, n3, n4):
    # Primera comparación n1 > n2
    if n1 > n2:
        n1, n2 = n2, n1
    
    # Segunda comparación n2 > n3
    if n2 > n3:
        n2, n3 = n3, n2
        # Volver a verificar n1 y n2
        if n1 > n2:
            n1, n2 = n2, n1
    
    # Tercera comparación n3 > n4
    if n3 > n4:
        n3, n4 = n4, n3
        # Volver a verificar n2 y n3
        if n2 > n3:
            n2, n3 = n3, n2
            # Volver a verificar n1 y n2
            if n1 > n2:
                n1, n2 = n2, n1
    
    # Una última verificación n2 > n3
    if n2 > n3:
        n2, n3 = n3, n2
        # Verificar n1 y n2
        if n1 > n2:
            n1, n2 = n2, n1
        # Verificar n3 y n4
        if n3 > n4:
            n3, n4 = n4, n3
    
    return (n1, n2, n3, n4)

# Entrada de datos
n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))
n3 = float(input("Ingrese el tercer número: "))
n4 = float(input("Ingrese el cuarto número: "))

# Ordenar los números
sorted_numbers = sort_four_numbers(n1, n2, n3, n4)

# Mostrar el resultado
print("Los números ordenados de menor a mayor son:", sorted_numbers)

