""" Calcular el área de diferentes figuras geométricas utilizando funciones separadas."""

def area_rectangulo(lado1, lado2):
    area = lado1 * lado2
    return area

def area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

def area_circulo(radio):
    area = 3.14159 * (radio ** 2)
    return area

def area_cuadrado(lado):
    area = lado ** 2
    return area

def pausar():
    input("\n---Presiona Enter para continuar---\n")

def menu_figuras():
    print("\n=== FIGURAS ===\n")
    print("1 - Rectángulo")
    print("2 - Triángulo")
    print("3 - Círculo")
    print("4 - Cuadrado")
    print("5 - Volver al menú principal")
    print("\nPor favor, seleccione una opcion del menú:\n")
    print("=" * 20)
    print("\n")

def main_figuras():
    while True:
        menu_figuras()
        option = input("\nSelecciona una opcion: \n")

        if option == "1":
            lado1 = float(input("Ingrese el lado 1: "))
            lado2 = float(input("Ingrese el lado 2: "))
            area = area_rectangulo(lado1, lado2)
            print(f"El area del rectangulo es: {area}")
            pausar()

        elif option == "2":
            base = float(input("Ingrese la base: "))
            altura = float(input("Ingrese la altura: "))
            area = area_triangulo(base, altura)
            print(f"El area del triangulo es: {area}")
            pausar()

        elif option == "3":
            radio = float(input("Ingrese el radio: "))
            area = area_circulo(radio)
            print(f"El area del circulo es: {area}")
            pausar()

        elif option == "4":
            lado = float(input("Ingrese la longitud de un lado: "))
            area = area_cuadrado(lado)
            print(f"El area del cuadrado es: {area}")
            pausar()

        elif option == "5":
            # Volver a Menu Principal
            return

        else:
            print("Por favor, seleccione una opcion del menú.")
            pausar()

def main():
    main_figuras()

if __name__ == "__main__":
    main()