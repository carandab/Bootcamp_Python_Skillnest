""" AE 6 Ejercicio Grupal - Manejo de Archivos "Moda Xpress" """

import os
import time

# 1 Apertura de archivo en modo lectura: Leer todo el inventario.
def leer_inventario():
    try:
        with open("inventario.txt", "r", encoding ="utf-8") as file:
            contenido = file.read()
        if contenido.strip():
            print("\n === Inventario ===")
            print(contenido)
        else:
            print("El inventario está vacio")
    except FileExistsError:
        print("No existe el archivo de inventario")
        
# 2 Apertura de archivo en modo escritura: Escribir datos de nuevos productos.
def registrar_nuevoinventario():
    with open("inventario.txt", "w", encoding="utf-8") as file:
        producto = input("Producto:")
        precio = input ("Precio:")
        cantidad = input("Cantidad:")
        talla = input("Talla:").upper()
        file.write(f"{producto}, {precio} USD, {cantidad} unidades, {talla.upper()}\n")
    print("Invetario creado desde cero")


# 3 Apertura de archivo en modo "append": Agregar productos sin eliminar los datos existentes.
def agregar_producto():
    try:
        with open("inventario.txt", "a", encoding="utf-8") as file:
            producto = input("Producto:")
            precio = input ("Precio:")
            cantidad = input("Cantidad:")
            talla = input("Talla:")
            file.write(f"{producto}, {precio} USD, {cantidad} unidades, {talla.upper()}\n")
        print("Producto agregado")
    except FileNotFoundError:
        print("El producto no existe.")

# 4 Apertura de archivo en modo lectura y escritura: Modificar y consultar productos existentes en el inventario.

def consulta_productos():
    """ Consulta el inventario y modifica un producto existente. """
    try:
        # Abre el archivo en modo r+ (lectura y escritura).
        with open("inventario.txt", "r+", encoding="utf-8") as file:
            
            # Lee el archivo
            lineas = file.readlines()
            
            # Mostrar inventario original
            print("\n=== Inventario original ===")
            print(lineas)
            
            # Define nuevo contenido
            nuevo_contenido = "Pantalon Azul, 35 USD, 35 unidades, L\n"
            
            lineas[1] = nuevo_contenido
            
            # Modifica el contenido
            print("\nContenido a modificar (línea 2):", lineas[1].strip())
            print("Contenido modificado")
            
            # Mueve el puntero al inicio
            file.seek(0)
            
            # Escribir la lista completa nuevamente
            file.writelines(lineas)
            
            print("\nProducto modificado.")
            
            # Mueve el puntero de nuevo al inicio para mostrar el resultado.
            file.seek(0)
            print("\n=== Inventario modificado ===")
            
            print(f"\n{file.read()}")
            
    except FileNotFoundError:
        print("El archivo no existe.")
    except IOError as e:
        print(f"Error al acceder al archivo: {e}")
   
# 5 Obtener atributos del archivo: Ver información sobre el archivo como el tamaño y la fecha de última modificación.

def obtener_atributos():

    info = os.stat("inventario.txt")
    nombre = os.path.basename("inventario.txt")
    # Nombre del archivo
    print(f"Nombre: {nombre}")
    # Tamaño en bytes
    print(f"Tamaño: {info.st_size} bytes")

    # Fecha de última modificación
    tiempo = time.ctime(info.st_mtime)
    print(f"Última modificación: {tiempo}")
    

# 6 Leer un producto específico: Buscar por nombre o ID y mostrar los detalles del producto.

def leer_producto():

    """Busca un producto en el archivo inventario.txt de forma simple."""

    producto_buscar = input("Ingresa el nombre del producto que quieres buscar: ").strip().capitalize()
    encontrado = False

    try:
        with open("inventario.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                # split(',') separa la informacion de la linea usando la ',' como separador y strip elimina los espacios
                # bucle para recorrer la informacion
                atributos = [atributo.strip() for atributo in linea.split(',')]
                # Por la posicion en la lista [0] accede al producto
                nombre_producto = atributos[0]

                if nombre_producto.capitalize() == producto_buscar:
                    print("\n=== Producto encontrado ===")
                    print(f"Nombre: {atributos[0]}")
                    print(f"Precio: {atributos[1]}")
                    print(f"Cantidad: {atributos[2]}")
                    print(f"Talla: {atributos[3]}")
                    encontrado = True
                    break
        
        if not encontrado:
            print(f"\nEl producto '{producto_buscar}' no se encontró en el inventario.")

    except FileNotFoundError:
        print("Error: No se encontró el archivo 'inventario.txt'.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# 7 Modificar el nombre de un producto: Cambiar el nombre de un artículo en el inventario.

def modificar_nombre_producto():

    producto_a_modificar = input("Ingresa el nombre del producto que quieres modificar: ").strip().capitalize()
        
    modificado = False

    try:
        # Leer el archivo 
        with open("inventario.txt", "r", encoding="utf-8") as file:
            lineas = file.readlines()

        # Crea lista para el nuevo contenido
        nuevas_lineas = []

        # Bucle para buscar el producto linea por linea
        for linea in lineas:
            # split(',') separa la informacion de la linea usando la ',' como separador y strip elimina los espacios
            # con [0] se accede al producto por la posicion en la lista
            # Se crea bucle en atributos para recorrer la informacion de la linea
            atributos = [atributo.strip() for atributo in linea.split(',')]
            nombre_en_linea = atributos[0].capitalize()

            # Condicional que compara busqueda con inventario
            if nombre_en_linea == producto_a_modificar:
                print(f"Producto encontrado: {linea.strip()}")
                nuevo_nombre = input(f"Ingresa el nuevo nombre para '{producto_a_modificar}': ").strip()
                # Crea nueva línea con nombre nuevo
                nueva_linea = f"{nuevo_nombre}, {atributos[1]}, {atributos[2]}, {atributos[3]}\n"
                nuevas_lineas.append(nueva_linea)
                modificado = True

            # Las lineas que no fueron buscadas se añaden sin cambios
            else:
                nuevas_lineas.append(linea)

        # Si esta modificado se sobreescribe
        if modificado:
            with open("inventario.txt", "w", encoding="utf-8") as file:
                file.writelines(nuevas_lineas)
            print("\n¡Nombre de producto modificado correctamente!")
        else:
            print("\nProducto no encontrado. No se realizó ninguna modificación.")

    except FileNotFoundError:
        print("Error: El archivo 'inventario.txt' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    finally:
        file.close()

# 8 Eliminar un producto: Eliminar un producto del inventario.

def eliminar_producto():
    producto = input("Ingrese el nombre del producto a eliminar: ").lower
    eliminado = False

    try:
        with open("inventario.txt", "r", encoding="utf-8") as file:
            lineas = file.readlines()

        with open("inventario.txt", "w", encoding="utf-8") as file:
            for linea in lineas:
                if producto in linea.lower():
                    eliminado = True  
                else:
                    file.write(linea)

        if eliminado:
            print(f"El producto: {producto} fue eliminado de inventario.")
        else:
            print("Producto no encontrado")
    except FileNotFoundError:
        print("El archivo inventario.txt no existe")


# Bonus: Modificar un archivo completamente

def modificar_producto():
    
    """Modifica los datos de un producto existente en inventario.txt."""

    producto_a_modificar = input("¿Qué producto desea modificar?: ").strip().capitalize()
    modificado = False

    try:
        # Lee el contenido del archivo
        with open("inventario.txt", "r", encoding="utf-8") as file:
            lineas = file.readlines()

        # Crea lista para la informacion nueva
        nuevas_lineas = []

        # Bucle para buscar el producto linea por linea
        for linea in lineas:
            # split(',') separa la informacion de la linea usando la ',' como separador y strip elimina los espacios
            # con [0] se accede al producto por la posicion en la lista
            nombre_en_linea = linea.split(',')[0].strip().capitalize()

            # Condicional que compara busqueda con inventario

            if nombre_en_linea == producto_a_modificar:
                print("Producto encontrado:", linea.strip())
                
                # Pedimos los nuevos datos
                nuevo_nombre = input("Nuevo nombre: ")
                nuevo_precio = input("Nuevo precio: ")
                nueva_cantidad = input("Nueva cantidad: ")
                nueva_talla = input("Nueva talla: ")
                
                # Creamos la nueva línea y la agregamos a la lista
                nuevas_lineas.append(f"{nuevo_nombre}, {nuevo_precio} USD, {nueva_cantidad} unidades, {nueva_talla.upper()}\n")
                modificado = True

            # Las lineas que no coinciden con la busqueda se mantienen sin cambios
            else:
                nuevas_lineas.append(linea)

        # Si esta modificado se sobreescribe el archivo con la informacion nueva
        if modificado:
            with open("inventario.txt", "w", encoding="utf-8") as f:
                f.writelines(nuevas_lineas)
            print("Producto modificado correctamente.")
        else:
            print("Producto no encontrado.")

    except FileNotFoundError:
        print("No existe el archivo de inventario.")
    finally:
        file.close()
    
# 9 Cerrar archivos: Asegurarse de cerrar correctamente el archivo después de cada operación.


# === Menu Principal ===

def menu():

    while True:
        print("\n === Moda Xpress ===")
        print("1. Ver Inventario")
        print("2. Agregar nuevo Producto")
        print("3. Registrar Producto")
        print("4. Modificar y consultar producto")
        print("5. Ver información del archivo")
        print("6. Buscar producto especifico")
        print("7. Modificar nombre de producto")
        print("8. Eliminar producto")
        print("9. Modificar producto completo")
        print("10. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            leer_inventario()

        elif opcion == "2":
            registrar_nuevoinventario()

        elif opcion == "3":
            agregar_producto()

        elif opcion == "4":
            consulta_productos()

        elif opcion == "5":
            obtener_atributos()

        elif opcion == "6":
            leer_producto()

        elif opcion == "7":
            modificar_nombre_producto()

        elif opcion == "8":
            eliminar_producto()

        elif opcion == "9":
            modificar_producto

        elif opcion == "10":
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")   

if __name__ == "__main__":
    menu()    
