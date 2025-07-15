""" Ejercicio individual AE4 - Bucle For Básico 1"""

def menu(first_time=False):

    """ Muestra un menú de opciones al usuario """
    if first_time:
        print("--- La idea de este menú fue robada vilmente a Felipe Burgos---\n")
    print("\nSeleccione una opción:\n")
    print("1. Ejercicio 1")
    print("2. Ejercicio 2")
    print("3. Ejercicio 3")
    print("4. Ejercicio 4")
    print("5. Ejercicio 5")
    print("6. Ejercicio 6")
    print("7. Salir")
    print("\n Por favor, ingrese el número de la opción deseada:\n")

def option_select(option):

    """ Ejecuta la opción seleccionada por el usuario """

    if option == 1:

    # Ejercicio 1
    #Imprime todos los números enteros del 0 al 100.
        print("\n ---Este es el ejercicio 1---\n")

        for i in range (101):
            print(i)
        pausar()
        return True

    elif option == 2:

    # Ejercicio 2
    #Imprime todos los números múltiplos de 2 entre 2 y 500

        print("\n ---Este es el ejercicio 2---\n")

        for i in range(2, 501, 2):
            print(i)
        pausar()
        return True

    elif option == 3:

    # Ejercicio 3
    #Imprime los números enteros del 1 al 100.
    # Si es divisible por 5 imprime “ice ice” en vez del número.
    # Si es divisible por 10, imprime “baby”

        print("\n ---Este es el ejercicio 3---\n")
        for i in range(1, 101):
            if i % 10 == 0:
                print("baby")
            elif i % 5 == 0:
                print("ice ice")
            else:
                print(i)
        pausar()
        return True

    elif option == 4:

    # Ejercicio 4
    #Suma los números pares del 0 al 500,000 e imprime la suma total.
        print("\n ---Este es el ejercicio 4---\n")
        suma = 0
        for i in range(0, 500001, 2):
            suma += i
        print(suma)

        pausar()
        return True

    elif option == 5:

    # Ejercicio 5
    # Imprime los números positivos comenzando desde 2024, en cuenta regresiva de 3 en 3.
        print("\n ---Este es el ejercicio 5---\n")

        for i in range(2024, 0, -3):
            print(i)
        pausar()
        return True

    elif option == 6:

    # Ejercicio 6
    # Establece tres variables: numInicial, numFinal y multiplo.
    # Comenzando en numInicial y pasando por numFinal, imprime
    #  los números enteros que sean múltiplos de multiplo.
    # Por ejemplo: si numInicial = 3, numFinal = 10, y multiplo = 2,
    #  el bucle debería de imprimir 4, 6, 8, 10 (en líneas sucesivas).
        print("\n ---Este es el ejercicio 6---\n")

        start_num = 4
        end_num = 84
        multiple = 4

        for i in range(start_num, end_num + 1):
            if i % multiple == 0:
                print(i)
        pausar()
        return True

    elif option == 7:
        print("\n---Saliendo del programa---\n")
        return False
    return True

def pausar():

    """ Pausa la ejecución del programa hasta que el usuario presione Enter """

    input("\n---Presiona Enter para continuar---\n")

def main():

    """ Funcion Principal """

    first = True
    while True:
        menu(first_time=first)
        first = False
        opcion = input()
        while not (opcion.isdigit() and 1 <= int(opcion) <= 7):
            print("Por favor, ingrese un número válido entre 1 y 7:")
            opcion = input()
        if not option_select(int(opcion)):
            break

if __name__ == "__main__":
    main()
