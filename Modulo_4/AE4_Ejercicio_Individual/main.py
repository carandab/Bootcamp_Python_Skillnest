from tamagotchi import Tamagotchi, Kuchipatchi, Mimitchi, Pochitchi
from persona import Persona

# Crear los tamagotchi

kuchipatchi1 = Kuchipatchi("Kuchi", "Verde")
mimitchi1 = Mimitchi("Mimi", "Blanco")
pochitchi1 = Pochitchi("Pochi", "Amarillo")

# Crear una persona y asignarle un tamagotchi

persona1 = Persona("Esteban", "Dido", None)

def pausar():
    input("Presiona enter para continuar...")

def inicio():
    print("\n")
    print("=" * 30)
    print("Bienvenido a Tamagotchi!")
    print("-" * 30)
    print("1. Kuchipatchi | 2. Mimitchi | 3. Pochitchi")

    while True:
        option = input("Elije tu Tamagotchi: " )
        if option == "1":
            persona1.set_tamagotchi(kuchipatchi1)
            print("\nHas elegido el Tamagotchi Kuchipatchi! 🐥")
            print("-" * 46)
            break
        elif option == "2":
            persona1.set_tamagotchi(mimitchi1)
            print("\nHas elegido el Tamagotchi Mimitchi! 🐰")
            print("-" * 46)
            break
        elif option == "3":
            persona1.set_tamagotchi(pochitchi1)
            print("\nHas elegido el Tamagotchi Pochitchi! 🐕")
            print("-" * 46)
            break
        else:
            print("\n")
            print("Opcion no valida")
            print("\n")

def main_menu():
    print("\n")
    print("=" * 46)
    print("=" * 15, "Menú Principal", "=" * 15)
    print("=" * 46)
    print("1. Jugar con tu tamagotchi")
    print("2. Darle comida a tu Tamagotchi")
    print("3. Curar a tu Tamagotchi")
    print("4. Dormir")
    print("5. Mostrar información de tu Tamagotchi")
    print("6. Salir")
    print("=" * 46)

def main():

    inicio()

    while True:
        main_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            print("=" * 46)
            persona1.jugar_con_tamagotchi()
            print("\n")
            persona1.mostrar_stats()
            print("=" * 46)
            pausar()

        elif opcion == "2":
            print("=" * 46)
            persona1.dar_comida()
            print("\n")
            persona1.mostrar_stats()
            print("=" * 46)
            pausar()

        elif opcion == "3":
            print("=" * 46)
            persona1.curar_tamagotchi()
            print("\n")
            persona1.mostrar_stats()
            print("=" * 46)
            pausar()

        elif opcion == "4":
            print("=" * 46)
            persona1.dormir()
            print("\n")
            persona1.mostrar_stats()
            print("=" * 46)
            pausar()

        elif opcion == "5":
            print("=" * 46)
            persona1.mostrar_dueño()
            persona1.mostrar_stats()
            print("=" * 46)
            pausar()

        elif opcion == "6":

            print("\n")
            print("Vuelve Pronto!")
            print("\n")

            break

        elif opcion == "7":
            persona1.nono()
            print("\n")
            persona1.mostrar_stats()
            print("=" * 46)


        else:
            print("\n")
            print("Opcion no valida. Por favor, elige una opcion entre 1 y 6.")
            print("\n")



if __name__ == "__main__":

    main()
