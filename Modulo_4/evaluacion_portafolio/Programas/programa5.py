""" Registro de usuarios """

import json

users_list = []
next_id = 1

# Guardar y cargar datos
"""Esta parte fue hecha con ClaudeAI, con el fin de poder guardar los datos en un archivo JSON.
a pesar de no manejar el uso de try y except """

#Guarda los datos en un archivo JSON

def save_data():

    data = {
        "users": users_list,
        "next_id": next_id
    }
    try:
        with open("users_data.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
        print("✅ Datos guardados correctamente.")
    except Exception as e:
        print(f"Error al guardar: {e}")


#Carga los datos desde el archivo JSON

def load_data():

    global users_list, next_id
    try:
        with open("users_data.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            users_list = data.get("users", [])
            next_id = data.get("next_id", 1)
        print(f"✅ Datos cargados: {len(users_list)} usuarios encontrados.")
    except FileNotFoundError:
        print("📝 Archivo no encontrado. Iniciando con datos vacíos.")
        users_list = []
        next_id = 1
    except json.JSONDecodeError:
        print("Error al leer el archivo. Iniciando con datos vacíos.")
        users_list = []
        next_id = 1
    except Exception as e:
        print(f"Error inesperado: {e}")
        users_list = []
        next_id = 1


# Funciones

# Creacion de usuarios

def create_user_template():

    return {
        "name": "",
        "age": 0,
        "email": "",
        "height": 0.0,
        "is_student": False
    }

def create_user_input():

    user = create_user_template()

    # Solicita datos al usuario

    user["name"] = input("Nombre: ")                    # str
    user["age"] = int(input("Edad: "))                  # int
    user["email"] = input("Email: ")                    # str
    user["height"] = float(input("Altura (en cm): " ))  # float
    response = input("¿Es estudiante? (si/no): ")         # bool
    while response.lower() not in ['si', 'no']:
        print("Por favor, ingrese 'si' o 'no'")
        response = input("¿Es estudiante? (si/no): ")

    user["is_student"] = response.lower() == 'si'
    return user

# Agregar usuarios

def add_user():

    global next_id
    user = create_user_input()
    user["id"] = next_id
    users_list.append(user)
    print(f"Usuario agregado con ID: {next_id}")
    next_id += 1
    save_data()

# Eliminar usuarios

def delete_user():

    user_id = int(input("Ingrese el ID del usuario que desea eliminar: "))
    for user in users_list:
        if user["id"] == user_id:
            users_list.remove(user)
            print(f"Usuario con ID {user_id} eliminado.")
            save_data()
            return
    print(f"Usuario con ID {user_id} no encontrado.")


# Mostrar usuarios

def display_users_list():

    if not users_list:
        print("No hay usuarios registrados.")
        return
    print("=== Lista de Usuarios ===")
    print(f"{'ID':<3} | {'Nombre':<15} | {'Edad':<4} | {'Email':<20} | {'Altura':<7} | {'Estudiante'}")
    print("-" * 75)

    for user in users_list:
        print(f"{user['id']:<3} | {user['name']:<15} | {user['age']:<4} | {user['email']:<20} | {(user['height']/100):<7.2f} | {user['is_student']:<5}")

def find_user_by_id_list(user_id):

    for user in users_list:
        if user["id"] == user_id:
            return user
    print(f"Usuario con ID {user_id} no encontrado.")
    return None

# Funciones de Menú

def show_menu():

    print("\n======= Menu =======\n")
    print("1. Agregar Usuario")
    print("2. Eliminar Usuario")
    print("3. Mostrar Usuarios")
    print("4. Encontrar Usuario")
    print("5. Salir")
    print("=" * 20 + "\n")

def main_menu():

    while True:
        show_menu()
        option = input("Selecciona una opcion: ")
        if option == "1":
            add_user()
        elif option == "2":
            delete_user()
        elif option == "3":
            display_users_list()
        elif option == "4":
            user_id = int(input("Ingrese el ID de usuario: "))
            user = find_user_by_id_list(user_id)
            if user:
                print(f"{user}")
        elif option == "5":
            save_data()
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")

def main():

    load_data()
    main_menu()

if __name__ == "__main__":
    main()
