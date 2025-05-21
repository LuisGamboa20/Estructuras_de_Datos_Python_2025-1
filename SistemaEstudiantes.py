class Estudiante:
    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id
        self.calificaciones = {}

    def agregar_calificacion(self, materia, calificacion):
        self.calificaciones[materia] = calificacion

    def obtener_promedio(self):
        if not self.calificaciones:
            return 0
        return sum(self.calificaciones.values()) / len(self.calificaciones)

class SistemaEstudiantes:
    def __init__(self):
        self.estudiantes = {}

    def agregar_estudiante(self, nombre, id):
        if id in self.estudiantes:
            print(f"El estudiante con ID {id} ya está registrado.")
        else:
            self.estudiantes[id] = Estudiante(nombre, id)
            print(f"Estudiante {nombre} agregado con éxito.")

    def agregar_calificacion(self, id, materia, calificacion):
        if id in self.estudiantes:
            self.estudiantes[id].agregar_calificacion(materia, calificacion)
            print(f"Calificación agregada para {materia}.")
        else:
            print(f"No se encontró estudiante con ID {id}.")

    def obtener_promedio_estudiante(self, id):
        if id in self.estudiantes:
            promedio = self.estudiantes[id].obtener_promedio()
            print(f"El promedio del estudiante con ID {id} es {promedio:.2f}.")
        else:
            print(f"No se encontró estudiante con ID {id}.")

    def mostrar_estudiantes(self):
        for id, estudiante in self.estudiantes.items():
            print(f"ID: {id}, Nombre: {estudiante.nombre}, Promedio: {estudiante.obtener_promedio():.2f}")

    def mostrar_estudiantes_aprobados_reprobados(self):
        print("\nEstudiantes Aprobados:")
        for id, estudiante in self.estudiantes.items():
            if estudiante.obtener_promedio() >= 3.0:
                print(f"ID: {id}, Nombre: {estudiante.nombre}, Promedio: {estudiante.obtener_promedio():.2f}")
        
        print("\nEstudiantes Reprobados:")
        for id, estudiante in self.estudiantes.items():
            if estudiante.obtener_promedio() < 3.0:
                print(f"ID: {id}, Nombre: {estudiante.nombre}, Promedio: {estudiante.obtener_promedio():.2f}")

    def consultar_estudiantes(self):
        print("\nEstudiantes Registrados:")
        for id, estudiante in self.estudiantes.items():
            print(f"ID: {id}, Nombre: {estudiante.nombre}")

    def consultar_materias(self):
        materias = set()
        for estudiante in self.estudiantes.values():
            materias.update(estudiante.calificaciones.keys())
        print("\nMaterias Registradas:")
        for materia in materias:
            print(materia)

if __name__ == "__main__":
    sistema = SistemaEstudiantes()
    while True:
        print("\n1. Agregar estudiante")
        print("2. Agregar calificación")
        print("3. Obtener promedio de estudiante")
        print("4. Mostrar todos los estudiantes")
        print("5. Mostrar estudiantes aprobados y reprobados")
        print("6. Consultar estudiantes registrados")
        print("7. Consultar materias registradas")
        print("8. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del estudiante: ")
            id = input("Ingrese el ID del estudiante: ")
            sistema.agregar_estudiante(nombre, id)
        elif opcion == "2":
            id = input("Ingrese el ID del estudiante: ")
            materia = input("Ingrese la materia: ")
            calificacion = float(input("Ingrese la calificación: "))
            sistema.agregar_calificacion(id, materia, calificacion)
        elif opcion == "3":
            id = input("Ingrese el ID del estudiante: ")
            sistema.obtener_promedio_estudiante(id)
        elif opcion == "4":
            sistema.mostrar_estudiantes()
        elif opcion == "5":
            sistema.mostrar_estudiantes_aprobados_reprobados()
        elif opcion == "6":
            sistema.consultar_estudiantes()
        elif opcion == "7":
            sistema.consultar_materias()
        elif opcion == "8":
            break
        else:
            print("Opción no válida. Intente de nuevo.")