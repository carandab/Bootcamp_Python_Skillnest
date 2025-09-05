""" Generador de tablas de multiplicar y multiplicar infinito """

def tabla_multiplicar(n):

    for i in range(1, 12):
        print(f"{n} x {i} = {n * i}")

def multiplicar_infinito(n):

    i = n
    while True:
        print(f"{n} x {i} = {n * i}")
        i += 1

def options():

    print("Elija una opción:")
    print("1. Tabla de multiplicar")
    print("2. Multiplicar infinito")

def main():

    num = int(input("Ingrese un numero: "))
    options()
    option = int(input("Ingrese una opción: "))
    if option == 1:
        tabla_multiplicar(num)
    elif option == 2:
        multiplicar_infinito(num)
    else:
        print("Opción no valida")

if __name__ == "__main__":
    main()