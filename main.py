import db

class Cliente:
    def __init__(self):
        self.db = db.cliente
        self.nome = None
        self.nconta = None
        self.senha = None
        self.saldo = None

    def validar(self, nconta, senha):

        nconta = str(nconta)
        senha = int(senha)

        for c in self.db:
            if c["nconta"] == nconta and c["senha"] == senha:
                self.nome = c["nome"]
                self.nconta = c["nconta"]
                self.saldo = c["saldo"]
                return True

    def getSaldo(self):

        return self.saldo


    def depositar(self, valor):
        self.saldo += valor
        return True

    def saque(self,valor):
        valor = int(valor)
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False

     #def transferencia(self, nconta, valor):
        #if valor <= self.transferencia:




class Display:

    def telaInicio(self):
        print("Bem vindo ao banco Mad")
        print("----------------------")
        nconta = input("digite o número da conta:\n")
        senha = input("digite a senha:\n")
        return nconta,senha

    def telaOp(self):
        a = input("Selecione 1 para ver o saldo\nSelecione 2 para sacar\nSelecione 3 para depositar")
        return int(a)

    def telaSaldo(self,saldo):
        print("Seu saldo é de " + str(saldo))

    def telaSaque(self):
        i=input("qual quantidade deseja sacar?")
        return i
    def box(self,txt):
        print(txt)



    def telaDep(self):
        i = input("qual quantidade deseja depositar?")
        return i

class CaixaEletronico:

    def __init__(self):
        self.cliente = Cliente()
        self.display = Display()

    def start(self):
        while True:

            a = self.display.telaInicio()
            if self.cliente.validar(a[0],a[1]):
                while True:
                    b = self.display.telaOp()
                    if b == 1:
                        c = self.cliente.getSaldo()
                        self.display.telaSaldo(c)
                    elif b == 2:
                        d = self.display.telaSaque()
                        if self.cliente.saque(d):
                            self.display.box("Saque realizado com sucesso")
                        else:
                            self.display.box("Valor inválido")



a = CaixaEletronico()
a.start()