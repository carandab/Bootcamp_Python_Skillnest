""" Ejercicio de Estructuras Intermedias """

print("\n ------Ejercicio de Estructuras Intermedias------\n")

#1. Actualizar valores en diccionarios y listas:
#   A continuación se presentan varias estructuras de datos.
#   Realiza los siguientes cambios directamente:

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

#Cambia el valor 3 en matriz por 6.

print("------Ejercicio 1-----\n")

print("Matriz Original:", matriz)
matriz[1][0] = 6
print("Matriz Actualizada:", matriz)

print("\n")

#Cambia el nombre del primer cantante por "Enrique Martin Morales".

print("Cantantes Originales:", cantantes)
cantantes[0]["nombre"] = "Enrique Martin Morales"
print("Cantantes Actualizados:", cantantes)

print("\n")

#En el diccionario ciudades, reemplaza "Cancún" por "Monterrey".

print("Ciudades Originales:", ciudades)
ciudades.update({"México": ["Ciudad de México", "Guadalajara", "Monterrey"]})
# Otra opción sería ciudades["México"][2] = "Monterrey"

print("Ciudades Actualizadas:", ciudades)


print("\n")

#En la lista coordenadas, cambia el valor de "latitud" por 9.9355431.

print("Coordenadas Originales:", coordenadas)
coordenadas[0]["latitud"] = 9.9355431
print("Coordenadas Actualizadas:", coordenadas)


#2. Recorrer una lista de diccionarios:
#  Utiliza estructuras de control para iterar la lista cantantes.
#  Muestra el nombre y país de cada cantante.

print("\n ------Ejercicio 2------\n")

for i in cantantes:
    print(f"Nombre - {i['nombre']}, País - {i['pais']}")

#3. Obtener valores específicos desde una lista de diccionarios:  Utilizando la lista cantantes,
# imprime por separado todos los valores correspondientes a la clave "nombre".
# Luego, imprime todos los valores correspondientes a la clave "pais"

print("\n ------Ejercicio 3------\n")

nombres = [i["nombre"] for i in cantantes]
print("Nombres de Cantantes:", nombres)

paises = [i["pais"] for i in cantantes]    
print("Países de Cantantes:", paises)

print("\n")

#4. Recorrer un diccionario con listas como valores:  Dado el siguiente diccionario:

costa_rica = {
   "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
   "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

#Realiza un recorrido del diccionario que imprima lo siguiente:
# - La cantidad de elementos en cada lista seguida del nombre de la clave en mayúsculas.
# - Cada elemento de la lista correspondiente, en líneas separadas.

print("\n ------Ejercicio 4------\n")

for key, value in costa_rica.items():
    print(f"{len(value)}", f"{key.upper()}: \n")
    for item in value:
        print(f"- {item}")
    print("\n")
