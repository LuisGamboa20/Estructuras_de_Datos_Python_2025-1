# Crear un diccionario con dos pares clave-valor
d1 = {
   "nombre": "Juan",
   "id": 123,
}

# Imprimir el valor asociado a la clave "nombre"
print(d1["nombre"])  

# Imprimir el valor asociado a la clave "id"
print(d1["id"])  

# Modificar el valor asociado a la clave "nombre"
d1["nombre"] = "Pedro"
# Imprimir el nuevo valor asociado a la clave "nombre"
print(d1["nombre"])  

# Agregar un nuevo par clave-valor al diccionario
d1["Direccion"] = "Calle 1234"

# Imprimir el diccionario completo
print(d1) 

# Iterar sobre las claves del diccionario e imprimir cada clave
for i in d1:
    print(i)  

# Iterar sobre las claves del diccionario e imprimir el valor asociado a cada clave
for i in d1:
    print(d1[i])  

# Iterar sobre los pares clave-valor del diccionario e imprimir cada par
for i, j in d1.items():
    print(i, ":", j) 

# Crear dos diccionarios anidados
anidado1 = {"a": 1, "b": 2, "c": 3}
aninado2 = {"b": 10, "c": 4, "d": 5}

# Crear un diccionario que contiene los dos diccionarios anidados
d = {
    "aninado1": anidado1,
    "aninado2": aninado2
}

# Imprimir el diccionario que contiene los diccionarios anidados
print(d)  

