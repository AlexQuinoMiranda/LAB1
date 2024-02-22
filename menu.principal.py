import pickle
import os
from datetime import datetime

class Tarea:
    def __init__(self, descripcion, completada=False, plazo=None):
        self.descripcion = descripcion
        self.completada = completada
        self.plazo = plazo

    def marcar_como_completada(self):
        self.completada = True

    def __str__(self):
        estado = 'Completada' if self.completada else 'Pendiente'
        plazo_str = f" (Plazo: {self.plazo.strftime('%Y-%m-%d')})" if isinstance(self.plazo, datetime) else ""

        return f"{self.descripcion} - {estado}{plazo_str}"

class ListaDeTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion, plazo=None):
        tarea = Tarea(descripcion, plazo=plazo)
        self.tareas.append(tarea)

    def marcar_tarea_como_completada(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].marcar_como_completada()
        else:
            print("Índice de tarea no válido")

    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            del self.tareas[indice]
        else:
            print("Índice de tarea no válido")

    def obtener_tareas_pendientes(self):
        return [tarea for tarea in self.tareas if not tarea.completada]

    def obtener_tareas_completadas(self):
        return [tarea for tarea in self.tareas if tarea.completada]

    def guardar_en_archivo(self, nombre_archivo):
        with open(nombre_archivo, 'wb') as f:
            pickle.dump(self.tareas, f)

    def cargar_desde_archivo(self, nombre_archivo):
        if os.path.exists(nombre_archivo):
            with open(nombre_archivo, 'rb') as f:
                self.tareas = pickle.load(f)

def mostrar_tareas(tareas):
    for i, tarea in enumerate(tareas, 1):
        print(f"{i}. {tarea}")

def mostrar_menu():
    print("\nMenú:")
    print("1. Agregar Tarea")
    print("2. Marcar Tarea como Completada")
    print("3. Eliminar Tarea")
    print("4. Ver Tareas Pendientes")
    print("5. Ver Tareas Completadas")
    print("6. Guardar y Salir")
    print("7. Salir sin Guardar")

def main():
    lista_de_tareas = ListaDeTareas()

    nombre_archivo = "tareas.pickle"
    print(f"Las tareas se guarda en el archivo: {nombre_archivo}")

    # Cargar tareas desde el archivo si existe
    lista_de_tareas.cargar_desde_archivo(nombre_archivo)

    while True:
        mostrar_menu()
        opcion = input("Ingrese su opción: ")

        if opcion == '1':
            descripcion_tarea = input("Ingrese la descripción de la tarea: ")
            plazo = input("Ingrese el plazo (opcional - formato: YYYY-MM-DD): ")
            lista_de_tareas.agregar_tarea(descripcion_tarea, plazo)
            print("Tarea agregada exitosamente.")
        elif opcion == '2':
            tareas_pendientes = lista_de_tareas.obtener_tareas_pendientes()
            if tareas_pendientes:
                print("Tareas Pendientes:")
                mostrar_tareas(tareas_pendientes)
                indice = int(input("Ingrese el número de la tarea para marcar como completada: ")) - 1
                lista_de_tareas.marcar_tarea_como_completada(indice)
            else:
                print("No hay tareas pendientes para marcar como completadas.")
        elif opcion == '3':
            tareas_pendientes = lista_de_tareas.obtener_tareas_pendientes()
            if tareas_pendientes:
                print("Tareas Pendientes:")
                mostrar_tareas(tareas_pendientes)
                indice = int(input("Ingrese el número de la tarea para eliminar: ")) - 1
                lista_de_tareas.eliminar_tarea(indice)
                print("Tarea eliminada exitosamente.")
            else:
                print("No hay tareas pendientes para eliminar.")
        elif opcion == '4':
            tareas_pendientes = lista_de_tareas.obtener_tareas_pendientes()
            if tareas_pendientes:
                print("Tareas Pendientes:")
                mostrar_tareas(tareas_pendientes)
            else:
                print("No hay tareas pendientes.")
        elif opcion == '5':
            tareas_completadas = lista_de_tareas.obtener_tareas_completadas()
            if tareas_completadas:
                print("Tareas Completadas:")
                mostrar_tareas(tareas_completadas)
            else:
                print("No hay tareas completadas.")
        elif opcion == '6':
            lista_de_tareas.guardar_en_archivo(nombre_archivo)
            print("Tareas guardadas en el archivo. Saliendo...")
            break
        elif opcion == '7':
            print("Saliendo sin guardar...")
            break
        else:
            print("Opción no válida. Por favor ingrese un número entre 1 y 7.")

if __name__ == "__main__":
    main()

