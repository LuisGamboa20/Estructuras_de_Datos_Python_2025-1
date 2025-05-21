# Ejemplo sencillo de cómo funciona una tupla en Python

# Definición de una tupla
mi_tupla = (10, 20, 30)

# Acceso a elementos de la tupla
print("Primer elemento:", mi_tupla[0])  
print("Segundo elemento:", mi_tupla[1])  
print("Tercer elemento:", mi_tupla[2])  

# Longitud de la tupla
print("Longitud de la tupla:", len(mi_tupla))  

# Intento de modificar un elemento (esto generará un error)
try:
    mi_tupla[1] = 40
except TypeError as e:
    print("Error:", e)  