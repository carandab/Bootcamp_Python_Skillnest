from tarjeta_credito import TarjetaCredito

if __name__ == '__main__':

    tarjeta1 = TarjetaCredito(0, 1000, 0.01)
    tarjeta2 = TarjetaCredito(0, 1500, 0.03)
    tarjeta3 = TarjetaCredito(0, 2000, 0.02)


    #Para la primera tarjeta, haz 2 compras y un pago. Luego cobra los intereses y muestra la información de la tarjeta;
    # todo esto en una sola línea a través de la encadenación.
    
    print("\n")
    print("=== Tarjeta 1 ===\n")
    tarjeta1.compra(100).compra(200).pago(150).cobrar_interes().mostrar_info_tarjeta()
    

    #Para la segunda tarjeta, haz 3 compras y 2 pagos. Luego cobra los intereses
    #  y muestra la información de la tarjeta; todo esto en una sola línea a través de la encadenación.
    print("=== Tarjeta 2 ===\n")
    tarjeta2.compra(100).compra(200).compra(300).pago(150).pago(100).cobrar_interes().mostrar_info_tarjeta()


    #Para la tercera tarjeta, haz 5 compras y excede su límite de crédito.
    #  Luego muestra la información de la tarjeta; todo esto en una sola línea a través de la encadenación.
    print("=== Tarjeta 3 ===\n")
    tarjeta3.compra(500).compra(600).compra(300).compra(400).compra(500).mostrar_info_tarjeta()