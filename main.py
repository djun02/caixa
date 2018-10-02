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
        self.saldo += int(valor)
        

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


class DispensadorNotas:
    def __init__(self):
        self.montante = 0
        self.cedula = 100
        self.contagem = 0

    def dispensar(self,valor):
        self.montante = int(valor)
        while True:
            if self.montante >= self.cedula:
                self.montante -= self.cedula
                self.contagem += 1
            
            
            else:
                if self.contagem > 0:
                    print("{0} cedulas de {1}".format(self.contagem, self.cedula))
                self.contagem = 0
                if self.montante == 0:
                    break
                if self.cedula == 100:
                    self.cedula = 50
                elif self.cedula == 50:
                    self.cedula = 20
                elif self.cedula == 20:
                    self.cedula = 5
                elif self.cedula == 5:
                    self.cedula = 2
            
            continue



class CaixaEletronico:

    def __init__(self):
        self.cliente = Cliente()
        self.display = Display()
        self.dispensador = DispensadorNotas()

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
                            self.dispensador.cedula=100
                            self.dispensador.dispensar(d)
                        else:
                            self.display.box("Valor inválido")
                    elif b == 3:
                        e = self.display.telaDep()
                        self.cliente.depositar(e)
                    
                         
                        



a = CaixaEletronico()
a.start()
