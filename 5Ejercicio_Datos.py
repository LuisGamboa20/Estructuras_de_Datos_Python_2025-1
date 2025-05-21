#escribe un programa en python que solicite al ususario lo siguiente
#nombre tipo string, edad tipo int
# porcentaje de propina que desea tipo int total de la cuenta tipo int
#el programa debe asegurarse que los valores ingresados sean validos , debe calcular
# la cantidad de propina el total a pagar, cuenta + propina
# y un mensaje personalizado segun la edad del usuario
# brindele al usuario la posibilidad de elegir 
# productos de un menu antes de calcular la propina 
 
 #informacion del usuario
nombre_usuario = str(input("Por favor, ingrese su nombre: "))
edad_usuario = int(input("Ingrese su edad: "))
if 0 < edad_usuario <= 18:
    print("Hola joven, ¿en qué podemos asistirte?")
elif 18 < edad_usuario <= 30:
    print("Buen día, ¿qué le gustaría ordenar?")
elif 30 < edad_usuario <= 80:
    print("Es un placer atenderlo, ¿qué desea ordenar?")    
else:
    print("Esa edad no parece válida.")
menu_productos = [
    ("Ensalada César", 10000),
    ("Pizza Margarita", 20000),
    ("Hamburguesa Clásica", 18000),
    ("Refresco", 4000),
    ("Helado", 6000),
]
for i, (producto, precio) in enumerate(menu_productos, 1):
    print(f"{i}. {producto} - ${precio}")
opcion_seleccionada = True  # para los productos que el usuario elija
orden_usuario = []  # vector que almacenara los productos del usuario
while opcion_seleccionada:
    opcion_seleccionada = int(input("¿Qué desea ordenar? (0 para salir): "))
    if opcion_seleccionada == 0:
        opcion_seleccionada = False 
    elif 1 <= opcion_seleccionada <= len(menu_productos):
        producto, precio = menu_productos[opcion_seleccionada - 1]
        orden_usuario.append((producto, precio))
        print(f"Ha seleccionado: {producto}")
    else: 
        print("Opción no válida.")
total_sin_propina = sum(precio for _, precio in orden_usuario)  # total de la cuenta sin propina
print(f"\nEl total de su cuenta es: ${total_sin_propina}")
# variable para guardar el porcentaje de propina
porcentaje_propina = int(input("Indique el porcentaje de propina que desea dar: "))
propina = porcentaje_propina / 100  # para guardar el porcentaje
total_con_propina = total_sin_propina + (total_sin_propina * propina)
print(f"El total a pagar, incluyendo la propina, es: ${total_con_propina}")