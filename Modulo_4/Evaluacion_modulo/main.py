import os
from biblioteca import Biblioteca
from libro import Libro, LibroDigital

def mostrar_menu():
    
    #Mostrar el menú principal

    print("\n" + "="*50)
    print("Bienvenido a nuestra Biblioteca ")
    print("="*50)
    print("=== Menú Principal ===")
    print("1. Mostrar todos los libros")
    print("2. Mostrar libros disponibles")
    print("3. Buscar libro por título")
    print("4. Agregar nuevo libro")
    print("5. Eliminar libro")
    print("6. Prestar libro")
    print("7. Devolver libro")
    print("8. Guardar cambios")
    print("9. Salir")
    print("="*50)

def agregar_libro_menu(biblioteca):

    try:

        print("\n=== Agregar nuevo libro ===")
        titulo = input("Título del libro: ").strip()

        if not titulo:
            print("ERROR: El título no puede estar vacío.")
            return
        
        autor = input("Autor del libro: ").strip()
        if not autor:
            print("ERROR: El autor no puede estar vacío.")
            return
        
        while True:
            try:

                año = int(input("Año de publicación: "))

                if año <= 0:
                    print("ERROR: El año debe ser un número positivo.")
                    continue
                break

            except ValueError:

                print("ERROR: Por favor, ingresa un año válido (número).")
        
        while True:

            tipo = input("¿Es un libro físico o digital?: ").lower().strip()

            if tipo in ['f', 'fisico', 'físico']:

                libro = Libro(titulo, autor, año)
                biblioteca.agregar_libro(libro)
                break

            elif tipo in ['d', 'digital']:

                while True:

                    formato = input("Formato digital (PDF/EPUB/MOBI): ").upper().strip()

                    if formato in ['PDF', 'EPUB', 'MOBI']:
                        libro = LibroDigital(titulo, autor, año, formato)
                        biblioteca.agregar_libro(libro)
                        break

                    else:
                        print("ERROR: Formato inválido. Usa: PDF, EPUB o MOBI")
                break

            else:
                raise ValueError("ERROR: Opción inválida.")
                
    except Exception as e:

        print(f"Error al agregar libro: {e}")

def buscar_libro_menu(biblioteca):
    titulo = input("\nIngresa el título del libro a buscar: ").strip()
    if not titulo:
        print("ERROR: El título no puede estar vacío.")
        return
    
    libro = biblioteca.buscar_libro(titulo)
    if libro:
        print(f"\nLibro Encontrado:")
        print(f"   {libro}")
    else:
        print(f"No se encontró el libro '{titulo}'")

def eliminar_libro_menu(biblioteca):

    titulo = input("\nIngresa el título o parte del título del libro a eliminar: ").strip()
    if not titulo:
        print("ERROR: El título no puede estar vacío.")
        return
    
    try:
        libros_encontrados = biblioteca.buscar_libro(titulo)
        
        if not libros_encontrados:
            print(f"No se encontró ningún libro con título que contenga '{titulo}'.")
            return
            
        # Muestra solo el libro encontrado si solo se encuentra uno
        if len(libros_encontrados) == 1:
            libro_a_eliminar = libros_encontrados[0]
            print("\nSe encontró el siguiente libro:")
            print(f"   {libro_a_eliminar}")
        
        # Si se encuentran varios libros, se le pide al usuario que elija
        else:
            print("\nSe encontraron múltiples libros. Selecciona uno para eliminar:")
            for i, libro in enumerate(libros_encontrados, 1):
                print(f"  {i}. {libro.get_titulo()}")
            
            while True:
                try:
                    opcion = int(input("\nIngresa el número del libro a eliminar: "))
                    if 1 <= opcion <= len(libros_encontrados):
                        libro_a_eliminar = libros_encontrados[opcion - 1]
                        break
                    else:
                        print("Opción inválida. Inténtalo de nuevo.")
                except ValueError:
                    print("Entrada inválida. Por favor, ingresa un número.")
        
        # Confirmación de eliminación
        respuesta = input(f"\n¿Estás seguro de que quieres eliminar '{libro_a_eliminar.get_titulo()}'?: ").lower().strip()
        
        if respuesta in ['y', 'si', 's', 'sí']:
            biblioteca.eliminar_libro(libro_a_eliminar.get_titulo())
        else:
            print("Eliminación cancelada.")
            
    except Exception as e:
        print(f"ERROR: {e}")


def prestar_libro_menu(biblioteca):
    titulo = input("\nIngresa el título del libro a prestar: ").strip()
    if not titulo:
        print("ERROR: El título no puede estar vacío.")
        return
    
    try:
        biblioteca.prestar_libro(titulo)
    except Exception as e:
        print(f"ERROR: {e}")

def devolver_libro_menu(biblioteca):
    titulo = input("\nIngresa el título del libro a devolver: ").strip()
    if not titulo:
        print("ERROR: El título no puede estar vacío.")
        return
    
    try:
        biblioteca.devolver_libro(titulo)
    except Exception as e:
        print(f"ERROR: {e}")

def salir_menu(biblioteca):

    respuesta = input("\nDesea guardar los cambios?")
    if respuesta in ['y', 'si', 's', 'sí']:
        print("\nGuardando datos...")
        biblioteca.guardar_archivo()
    else:
        print("\Cambios no guardados.")

    print("¡Hasta luego!")

def main():

    os.system("cls")
    print("Iniciando biblioteca...")
    biblioteca = Biblioteca()
    
    while True:
        try:
            mostrar_menu()
            opcion = input("\nSelecciona una opción (1-8): ").strip()
            
            if opcion == "1":
                biblioteca.mostrar_lista()
            elif opcion == "2":
                biblioteca.mostrar_disponibles()
            elif opcion == "3":
                buscar_libro_menu(biblioteca)
            elif opcion == "4":
                agregar_libro_menu(biblioteca)
            elif opcion == "5":
                eliminar_libro_menu(biblioteca)
            elif opcion == "6":
                prestar_libro_menu(biblioteca)
            elif opcion == "7":
                devolver_libro_menu(biblioteca)
            elif opcion == "8":
                print("\nGuardando datos...")
                biblioteca.guardar_archivo()
            elif opcion == "9":
                print("¡Hasta luego!")
                break   
            else:
                print("ERROR: Opción inválida. Selecciona un número del 1 al 8.")
            
            input("\nPresiona ENTER para continuar...")
            
        except KeyboardInterrupt:

            print("\n\nInterrupción detectada. Guardando datos antes de salir...")
            biblioteca.guardar_archivo()
            print("Datos guardados. ¡Hasta luego!")
            break

        except Exception as e:

            print(f"ERROR inesperado: {e}")
            input("\nPresiona ENTER para continuar...")

if __name__ == "__main__":
    main()