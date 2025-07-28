""" Conversor de Unidades Metrico/Imperial """

# Unidades de masa

def kg_lb():
    """ Funcion para convertir kilogramos a libras """

    print("=== Kilogramos a Libras ===")

    kg = float(input("KG: "))
    lb = kg * 2.2046
    print(f"{kg:.2f} Kg son {lb:.2f} libras")

def lb_kg():
    """ Funcion para convertir libras a kilogramos """

    print("=== Libras a Kilogramos ===")

    lb = float(input("LB: "))
    kg = lb * 0.4536
    print(f"{lb:.2f} libras son {kg:.2f} Kg")

# Unidades de longitud

def m_ft():
    """ Función para convertir metros a pies con formato ft'inch" """

    print("=== Metros a Pies y Pulgadas ===")
    m = float(input("M: "))
    ft_total = m * 3.2808

    # Separar pies enteros de la parte decimal
    ft_enteros = int(ft_total)
    ft_decimal = ft_total - ft_enteros

    # Convertir la parte decimal a pulgadas (12 pulgadas = 1 pie)
    pulgadas = ft_decimal * 12

    print(f"{m} metros = {ft_enteros}'{pulgadas:.2f}\"")

def ft_m():
    """ Función para convertir ft'inch" a metros """

    print("=== Pies y Pulgadas a Metros ===")
    ft = int(input("Pies: "))
    inch = float(input("Pulgadas: "))

    # Convertir todo a pies decimales
    ft_total = ft + (inch / 12)

    # Convertir a metros
    m = ft_total * 0.3048

    print(f"{ft}'{inch:.2f}\" son {m:.2f} metros")

def km_millas():
    """ Función para convertir kilómetros a millas """

    print("=== Kilómetros a Millas ===")
    km = float(input("Kilómetros: "))
    millas = km * 0.6214
    print(f"{km} km son {millas:.2f} millas")

def millas_km():
    """ Función para convertir millas a kilómetros """

    print("=== Millas a Kilómetros ===")
    millas = float(input("Millas: "))
    km = millas * 1.6093
    print(f"{millas} millas son {km:.2f} km")

# Unidades de Temperatura

def celsius_fahrenheit():
    """ Función para convertir Celsius a Fahrenheit """

    print("=== Celsius a Fahrenheit ===")
    c = float(input("°C: "))
    f = (c * 9/5) + 32
    print(f"{c}°C son {f}°F")

def fahrenheit_celsius():
    """ Función para convertir Fahrenheit a Celsius """

    print("=== Fahrenheit a Celsius ===")
    f = float(input("°F: "))
    c = (f - 32) * 5/9
    print(f"{f}°F son {c:.2f}°C")

# Unidades de Volumen

def lt_gal():
    """ Función para convertir litros a galones US """

    print("=== Litros a Galones US ===")
    l = float(input("Litros: "))
    gal = l * 0.2642
    print(f"{l} litros son {gal:.2f} galones US")

def gal_lt():
    """ Función para convertir galones US a litros """

    print("=== Galones US a Litros ===")
    gal = float(input("Galones US: "))
    l = gal * 3.7854
    print(f"{gal} galones US son {l:.2f} litros")

def ml_oz():
    """ Función para convertir mililitros a onzas fluidas """

    print("=== Mililitros a Onzas Fluidas ===")
    ml = float(input("Mililitros: "))
    fl_oz = ml * 0.0338
    print(f"{ml} ml son {fl_oz:.2f} fl oz")

def oz_ml():
    """ Función para convertir onzas fluidas a mililitros """

    print("=== Onzas Fluidas a Mililitros ===")
    fl_oz = float(input("Onzas fluidas: "))
    ml = fl_oz * 29.5735
    print(f"{fl_oz} fl oz son {ml:.2f} ml")

# Funcion de pausa
def pausar():

    """ Pausa la ejecución del programa hasta que el usuario presione Enter """

    input("\n---Presiona Enter para continuar---\n")

# Funciones de Menu

def show_menu():
    """ Muestra el menú principal de la aplicación."""

    print("\n-----Conversor de Unidades-----\n")
    print("\n=== MENÚ PRINCIPAL ===\n")
    print("1 - Masa")
    print("2 - Longitud")
    print("3 - Temperatura")
    print("4 - Volumen")
    print("5 - Salir")
    print("\nPor favor, seleccione una opción del menú:\n")
    print("=" * 20)
    print("\n")

def menu_masa():
    """ Muestra el menú de opciones de masa """

    print("\n=== MASA ===\n")
    print("1 - Kilogramos a Libras")
    print("2 - Libras a Kilogramos")
    print("3 - Volver al menú principal")
    print("\nPor favor, seleccione una opcion del menú:\n")
    print("=" * 20)
    print("\n")

def main_masa():
    """ Función principal del menú de masa """

    while True:
        menu_masa()
        option = input("\nSelecciona una opcion: \n")

        if option == "1":
            kg_lb()
            pausar()

        elif option == "2":
            lb_kg()
            pausar()

        elif option == "3":
            # Volver a Menu Principal
            return

        else:
            print("Por favor, seleccione una opcion del menú.")
            pausar()

def menu_longitud():
    """ Muestra el menú de opciones de longitud """

    print("\n=== LONGITUD ===\n")
    print("1 - Pies a Metros")
    print("2 - Metros a Pies")
    print("3 - Kilómetros a Millas")
    print("4 - Millas a Kilómetros")
    print("5 - Volver al menú principal")
    print("\nPor favor, seleccione una opcion del menú:\n")
    print("=" * 20)
    print("\n")

def main_longitud():
    """ Función principal del menú de longitud """

    while True:
        menu_longitud()
        option = input("\nSelecciona una opcion: \n")

        if option == "1":
            ft_m()
            pausar()

        elif option == "2":
            m_ft()
            pausar()

        elif option == "3":
            km_millas()
            pausar()

        elif option == "4":
            millas_km()
            pausar()

        elif option == "5":
            # Volver a Menu Principal
            return

        else:
            print("Por favor, seleccione una opcion del menú.")
            pausar()

def menu_temperatura():
    """ Muestra el menú de opciones de temperatura """

    print("\n=== TEMPERATURA ===\n")
    print("1 - Celsius a Fahrenheit")
    print("2 - Fahrenheit a Celsius")
    print("3 - Volver al menú principal")
    print("\nPor favor, seleccione una opcion del menú:\n")
    print("=" * 20)
    print("\n")

def main_temperatura():
    """ Función principal del menú de temperatura """

    while True:
        menu_temperatura()
        option = input("\nSelecciona una opcion: \n")

        if option == "1":
            celsius_fahrenheit()
            pausar()

        elif option == "2":
            fahrenheit_celsius()
            pausar()

        elif option == "3":
            # Volver a Menu Principal
            return

        else:
            print("Por favor, seleccione una opcion del menú.")
            pausar()

def menu_volumen():
    """ Muestra el menú de opciones de volumen """

    print("\n=== VOLUMEN ===\n")
    print("1 - Litros a Galones US")
    print("2 - Galones US a Litros")
    print("3 - Mililitros a Onzas Fluidas")
    print("4 - Onzas Fluidas a Mililitros")
    print("5 - Volver al menú principal")
    print("\nPor favor, seleccione una opcion del menú:\n")
    print("=" * 20)
    print("\n")

def main_volumen():
    """ Función principal del menú de volumen """

    while True:
        menu_volumen()
        option = input("\nSelecciona una opcion: \n")

        if option == "1":
            lt_gal()
            pausar()

        elif option == "2":
            gal_lt()
            pausar()

        elif option == "3":
            ml_oz()
            pausar()

        elif option == "4":
            oz_ml()
            pausar()

        elif option == "5":
            # Volver a Menu Principal
            return

        else:
            print("Por favor, seleccione una opcion del menú.")
            pausar()

def menu_main():

    """ Funcion principal del menú """

    while True:
        show_menu()
        option = input("Selecciona una opción: ")

        if option == "1":
            main_masa()

        elif option == "2":
            main_longitud()

        elif option == "3":
            main_temperatura()

        elif option == "4":
            main_volumen()

        elif option == "5":
            # Salir del programa
            print("\n¡Hasta luego!\n")
            return

        else:
            # Comprueba si la opcion es valida
            print("\n Opción no válida. Por favor, intente de nuevo.\n")
            input("\n---Presiona Enter para continuar---\n")

def main():
    """ Función principal que inicia la aplicación."""

    menu_main()

if __name__ == "__main__":
    main()
