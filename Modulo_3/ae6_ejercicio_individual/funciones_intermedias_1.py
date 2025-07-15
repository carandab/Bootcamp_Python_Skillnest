""" AE6-ABP Ejercicio Individual """

# -----Ejercicio 1: Actualizar valores en diccionarios y listas-----

# - Cambia el valor de 3 en matriz por 6.
#    Una vez realizado el cambio tu matriz debería ser: [ [10, 15, 20], [6, 7, 14] ]
# - Cambia el nombre del primer cantante de “Ricky Martin” a “Enrique Martin Morales”
# - En ciudades, cambia “Cancún” por “Monterrey”
# - En las coordenadas, cambia el valor de “latitud” por 9.9355431

matriz = [ [10, 15, 20], [3, 7, 14] ]

cantantes = [

   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},

   {"nombre": "Chayanne", "pais": "Puerto Rico"}

]

ciudades = {

   "México": ["Ciudad de México", "Guadalajara", "Cancún"],

   "Chile": ["Santiago", "Concepción", "Viña del Mar"]

}

coordenadas = [

   {"latitud": 8.2588997, "longitud": -84.9399704}

]

def value_update():
    """ Actualiza los valores de las variables segun las especificaciones del ejercicio. """ 

    # Actualizar el valor de 3 en matriz por 6
    matriz[1][0] = 6
    # Cambiar el nombre del primer cantante
    cantantes[0]["nombre"] = "Enrique Martin Morales"
    # Cambiar "Cancún" por "Monterrey"
    ciudades["México"][2] = "Monterrey"
    # Cambiar el valor de "latitud" por 9.9355431
    coordenadas[0]["latitud"] = 9.9355431

# Imprime información
print("\n---EJERCICIO 1---\n")
print("Matriz actualizada:\n", matriz, "\n")
print("Cantantes actualizados:\n", cantantes, "\n")
print("Ciudades actualizadas:\n", ciudades, "\n")
print("Coordenadas actualizadas:\n", coordenadas, "\n")



# -----Ejercicio 2: Iterar a través de una lista de diccionarios -----
# Crea la función iterarDiccionario(lista)
# que reciba una lista de diccionarios y recorra cada diccionario de la lista e imprima
# cada llave y el valor correspondiente. Por ejemplo:

artistas = [

   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},

   {"nombre": "Chayanne", "pais": "Puerto Rico"},

   {"nombre": "José José", "pais": "México"},

   {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}

]

# Define la función iterar_diccionario
def iterar_diccionario(diccionarios):

    """Recorre una lista de diccionarios e imprime cada llave y su valor."""

    for artista in diccionarios:
        for key, value in artista.items():
            print(f"{key} - {value}")
    print("\n")

print("---EJERCICIO 2---\n")

# Llama a la función iterar_diccionario
iterar_diccionario(artistas)



# -----Ejercicio 3: Obtener valores de una lista de diccionarios-----

#  Crea la función iterarDiccionario2(llave, lista)que reciba una cadena
#   con el nombre de una llave y una lista de diccionarios.
#  La función debe imprimir el valor almacenado para esa clave de cada diccionario
#   que se encuentra en la lista.

# Define la función iterar_diccionario2
def iterar_diccionario2(key, lista):
    """Imprime los valores de una llave específica en una lista de diccionarios."""

    for dictionary in lista:
        if key in dictionary:
            print(dictionary[key])
    print("\n")

print("---EJERCICIO 3---\n")

# Llama a la función iterar_diccionario2
print("Nombres de los artistas:\n")
iterar_diccionario2("nombre", artistas)
print("Países de los artistas:\n")
iterar_diccionario2("pais", artistas)




# ---Ejercicio 4: Iterar a través de un diccionario con valores de lista.---

#  Crea una función imprimirInformacion(diccionario)
#   que reciba un diccionario en donde los valores son listas.
#  La función debe imprimir el nombre de cada clave
#   junto con el tamaño de su lista y seguido de esto los valores de la lista para esa clave.

costa_rica = {

   "Ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],

   "Comidas": ["Gallo pinto", "Casado", "Tamales", "Chifrijo", "Olla de carne"]

}

# Define la función imprimir_informacion
def imprimir_informacion(lista):
    """Imprime el nombre de cada clave, el tamaño de su lista y los valores de la lista."""

    for key, value in lista.items():
        print(f"\n{key} (Tamaño de la Lista: {len(value)}):\n")
        for item in value:
            print(f" - {item}")
    print("\n")

print("---EJERCICIO 4---")
# Llama a la función imprimir_informacion
imprimir_informacion(costa_rica)
