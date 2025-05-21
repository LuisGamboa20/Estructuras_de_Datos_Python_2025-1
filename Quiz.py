diccionario = {
    "nombre": "Juan",
    "edad": 123,
}

print("Por favor digite su nombre: ")
x = input()

diccionario["nombre"] = x

print("Por favor digit su edad: ")
y = int(input())

diccionario["edad"] = y

for i, j in diccionario.items():
    print(i, ":", j)
