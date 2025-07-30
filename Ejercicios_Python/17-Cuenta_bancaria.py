class BankAccount:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("Dinero insuficiente.")

    def mostrar_saldo(self):
        print("Saldo actual:", self.saldo)

mi_cuenta = BankAccount(100000)
mi_cuenta.depositar(5000)
mi_cuenta.retirar(300)
mi_cuenta.mostrar_saldo()
