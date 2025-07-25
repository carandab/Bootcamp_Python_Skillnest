""" Evaluacion del Módulo 3 """
import os
# =============== Definiciones ===============

# Lista de tareas
tareas = [
    {"id": 1, "descripcion": "Estudiar Python", "completada": False},
    {"id": 2, "descripcion": "Hacer ejercicio", "completada": False},
    {"id": 3, "descripcion": "Sacar la basura", "completada": False}
]

# Define la función add_task
def add_task(lista_tareas):

    """ Añade tarea nueva a la lista "Tareas" """

    print("\n====== Agregar tarea ======\n")
    descripcion = input("Ingrese la descripción de la tarea que desea agregar: ")
    nueva_tarea = {"id": len(lista_tareas) + 1, "descripcion": descripcion, "completada": False}
    tareas.append(nueva_tarea)
    print("\n---Tarea agregada exitosamente---\n")

# Define la función show_list
def show_list(lista_tareas):

    """Muestra una tabla con cada item de la lista."""

    print("\n======= Lista de Tareas =======\n")
    print(f"{'ID':<3} | {'Descripción':<25} | {'Estado':<10}")
    print("-" * 45)
    for tarea in lista_tareas:
        estado = "Completada" if tarea['completada'] else "Pendiente"
        print(f"{tarea['id']:<3} | {tarea['descripcion']:<25} | {estado:<10}")
    print()

# Define la función delete_task
def delete_task(lista_tareas):

    """ Elimina una tarea de la lista 'Tareas' """

    print("\n====== Eliminar tarea ======\n")
    id_tarea = int(input("Ingrese el ID de la tarea que desea eliminar: "))
    for tarea in lista_tareas:
        if tarea["id"] == id_tarea:
            lista_tareas.remove(tarea)
            print("\n--- Tarea eliminada exitosamente ---\n")
            break
    else:
        print("\n--- Tarea no encontrada. Ingrese un ID válido ---\n")
# Define la funcion check_task
def check_task(lista_tareas):

    """ Cambia el estado de una tarea de la lista "Tareas" """

    print("\n====== Cambiar estado de tarea ======\n")

    id_tarea = int(input("Ingrese el ID de la tarea que desea cambiar: "))
    tarea_encontrada = False

    for tarea in lista_tareas:
        if tarea["id"] == id_tarea:
            tarea_encontrada = True
            estado_anterior = "completada" if tarea["completada"] else "pendiente"
            tarea["completada"] = not tarea["completada"]
            estado_nuevo = "completada" if tarea["completada"] else "pendiente"
            print(f"\n'{tarea['descripcion']}' cambiada de {estado_anterior} a {estado_nuevo}\n")
            break

    if not tarea_encontrada:
        print(f"\n---No se encontró ninguna tarea con ID {id_tarea}---\n")

# Define la función pausar
def pausar():

    """ Pausa la ejecución del programa hasta que el usuario presione Enter """

    input("\n---Presiona Enter para continuar---\n")

# Define la función show_menu
def show_menu():

    """ Muestra el menú principal de la aplicación."""

    print("\n-----Bienvenido a la Evaluación del Módulo 3-----\n")
    print("\n=== MENÚ PRINCIPAL ===\n")
    print("1 - Agregar tarea")
    print("2 - Ver tareas")
    print("3 - Marcar tarea como completada")
    print("4 - Eliminar tarea")
    print("5 - Salir")
    print("\nPor favor, seleccione una opción del menú:\n")
    print("=" * 20)
    print("\n")

# Define la función menu_main
def menu_main():

    """ Funcion principal del menú """

    while True:
        show_menu()
        option = input("Selecciona una opción: ")

        if option == "1":
            # Llama a la función add_task
            add_task(tareas)
            pausar()

        elif option == "2":
            # Llama a la función show_list
            show_list(tareas)
            pausar()

        elif option == "3":
            # Llama a la función check_task
            check_task(tareas)
            pausar()

        elif option == "4":
            # Llama a la función delete_task
            delete_task(tareas)
            pausar()

        elif option == "5":
            # Salir del programa
            print("\n¡Hasta luego!\n")
            os.system(f'echo "{tareas}" >> evaluación_de_modulo_3.txt')
            break

        else:
            # Comprueba si la opcion es valida
            print("\n Opción no válida. Por favor, intente de nuevo.\n")
            input("\n---Presiona Enter para continuar---\n")

# ========== Funcion Principal ===============

def main():
    """ Función principal que inicia la aplicación."""
    menu_main()

# Ejecucion de la función principal
if __name__ == "__main__":
    main()
