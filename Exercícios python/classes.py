class conta:
    def __init__(self, nome, numero):
        self.cliente = nome
        self.num = numero
        self.saldo = 0.0

    def Saldo(self):
        return self.saldo

    def getCliente(self):
        return self.cliente

    def depositar(self, valor):
        self.saldo += valor

