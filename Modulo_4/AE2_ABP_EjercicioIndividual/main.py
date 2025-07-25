from tarjeta_credito import TarjetaCredito

if __name__ == '__main__':

    tarjeta1 = TarjetaCredito(0, 1000, 0.01)
    tarjeta2 = TarjetaCredito(0, 1500, 0.03)
    tarjeta3 = TarjetaCredito(0, 2000, 0.02)
    tarjeta4 = TarjetaCredito(0, 1000, 0.04)


    #Para la primera tarjeta, haz 2 compras y un pago. Luego cobra los intereses y muestra la información de la tarjeta;
    # todo esto en una sola línea a través de la encadenación.
    
    print("\n")
    print("=== Tarjeta 1 ===")
    tarjeta1.compra(100).compra(200).pago(150).cobrar_interes().mostrar_info_tarjeta()
    

    #Para la segunda tarjeta, haz 3 compras y 2 pagos. Luego cobra los intereses
    #  y muestra la información de la tarjeta; todo esto en una sola línea a través de la encadenación.
    
    print("=== Tarjeta 2 ===")
    tarjeta2.compra(100).compra(200).compra(300).pago(150).pago(100).cobrar_interes().mostrar_info_tarjeta()

    #Para la tercera tarjeta, haz 5 compras y excede su límite de crédito.
    #  Luego muestra la información de la tarjeta; todo esto en una sola línea a través de la encadenación.

    print("=== Tarjeta 3 ===")
    tarjeta3.compra(500).compra(600).compra(300).compra(400).compra(500).mostrar_info_tarjeta()

    #BONUS: crea un método de clase para imprimir todas las instancias de la información de las tarjetas creadas.
    # En el capítulo pasado te dimos algunas pistas de cómo realizarlo.

    print("\n")
    print("============== Bonus ==============")
    print("=== Información de las tarjetas ===")
    TarjetaCredito.imprimir_info_tarjetas()

    print("---- Ejemplo por si el pago excediera el saldo a pagar ----\n")
    tarjeta4.compra(200).compra(300).pago(1000).cobrar_interes().mostrar_info_tarjeta()

