class TarjetaCredito:


    def __init__(self, saldo_pagar, limite_credito, intereses):

        self.saldo_pagar = saldo_pagar
        self.limite_credito = limite_credito
        self.intereses = intereses

    def compra(self, monto):

        if (self.saldo_pagar + monto) > self.limite_credito:
            print("Tarjeta excede límite")

        else:
            self.saldo_pagar = self.saldo_pagar + monto
            print(f"Compra realizada con exito por ${monto}")

        return self


    def pago(self, monto):
        
        if monto >= self.saldo_pagar:
            monto_cobrado = self.saldo_pagar
            self.saldo_pagar = 0
            print(f"Pago realizado por ${monto_cobrado}. Saldo liquidado completamente.")

        else:
            self.saldo_pagar = self.saldo_pagar - monto
            print(f"Pago realizado por ${monto}")

        return self

    def cobrar_interes(self):

        self.saldo_pagar = self.saldo_pagar + (self.saldo_pagar * self.intereses)

        return self

    def mostrar_info_tarjeta(self):

        print("\n")
        print(f"Saldo a pagar: {self.saldo_pagar}")
        print(f"Limite de credito: {self.limite_credito}")
        print(f"Tasa de Interes: {self.intereses}")
        print("\n")

        return self