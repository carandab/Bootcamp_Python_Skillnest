import datetime

# Define la funicion para calcular descuento

def calcular_descuento(cantidad_productos, compras_previas, total_compra, dia):

    descuento_total = 0

    if dia.lower() in ["miercoles", "viernes", "domingo"]:
        dia_promocion = True
    else:
        dia_promocion = False

    if cantidad_productos >= 10:
        descuento_total += 0.10

    if compras_previas >= 5:
        descuento_total += 0.05

    if total_compra >= 500:
        descuento_total += 0.07

    if dia_promocion:
        descuento_total += 0.15

    if descuento_total > 0.30:
        descuento_total = 0.30

    return descuento_total


# Programa principal

# Deteccion de dia actual
dias_semana = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
hoy = datetime.datetime.now()
dia = dias_semana[hoy.weekday()]

# Solicita datos al usuario


print("\n ¡Bienvenido! Por favor ingrese los datos de su compra")
print("\n")

cantidad_productos = int(input("Ingrese la cantidad de productos: "))

compras_previas = float(input("¿Cuántas veces ha comprado en esta tienda?: "))
if compras_previas < 5:
    print("¡Recuerda! Si compras 5 o más veces en nuestra tienda se te aplicará un descuento de 5% en tu compra.")


total_compra = float(input("Ingrese el total de la compra: "))

# Muestra promocion especial del dia

print("\n")
print(f"Hoy es {dia.capitalize()}.")
if dia.lower() in ["miercoles", "viernes", "domingo"]:
    print("¡Hoy hay una promoción especial!" \
    " Tienes un descuento adicional del 15% en tu compra. (Máximo descuento aplicable: 30%)")
else:
    print("Hoy no hay promociones.")

# Datos finales de compra

descuento_total = calcular_descuento(cantidad_productos, compras_previas, total_compra, dia)
total_final = total_compra - (total_compra * descuento_total)

print("\n El monto de su compra es:", total_compra)

print("\n Descuento total aplicado:", descuento_total * 100, "%" " (Máximo descuento aplicable: 30%)")

print("\n El total de su compra es:", total_final)

print("\n")

print("¡Muchas gracias por su compra!")

print("\n")