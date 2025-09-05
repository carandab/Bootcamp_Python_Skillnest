""" Formulario Básico """


print("=== Formulario ===")

nombre = input("Nombre: ")
edad = int(input("Edad: "))
altura = float(input("Altura (en cm): "))
response = input("¿Es Estudiante? (s/n): ")
while response.lower() not in ['s', 'n']:
    print("Por favor, ingrese 's' o 'n'")
    response = input("¿Es Estudiante? (s/n): ")

estudiante = response.lower() == 's'

print("\n=== Datos del Usuario ===")
print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Altura: {altura / 100} mts")
print(f"Es estudiante: {estudiante}")
