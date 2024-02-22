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

def mostrar_menu():
    print("\nMenú:")
    print("1. Agregar Tarea")
    print("2. Salir")

def main():
    lista_de_tareas = ListaDeTareas()

    while True:
        mostrar_menu()
        opcion = input("Ingrese su opción: ")

        if opcion == '1':
            descripcion_tarea = input("Ingrese la descripción de la tarea: ")
            plazo = input("Ingrese el plazo (opcional - formato: YYYY-MM-DD): ")
            lista_de_tareas.agregar_tarea(descripcion_tarea, plazo)
            print("Tarea agregada exitosamente.")
        elif opcion == '2':
            break
        else:
            print("Opción no válida. Por favor ingrese 1 o 2.")

if __name__ == "__main__":
    main()
