""" Determinar si un número es positivo, negativo o cero. """


def main():

    num = int(input("Ingrese un numero: "))

    if num > 0:
        print("El numero es positivo")
    elif num < 0:
        print("El numero es negativo")
    else:
        print("El numero es cero")

if __name__ == "__main__":
    main()
