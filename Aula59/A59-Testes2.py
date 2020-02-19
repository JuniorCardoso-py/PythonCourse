# Teste parte 2

class Calc:
    def __init__(self, numero1, numero2):
        # variável de classe
        self.__n1 = numero1
        self.__n2 = numero2
        self.__resultado = 0

    def set_n1(self, valor):
        self.__n1 = valor
        return self.__n1

    def get_n1(self):
        return self.__n1

    def set_n2(self, valor):
        self.__n2 = valor
        return self.__n2

    def get_n2(self):
        return self.__n2

    def get_resultado(self):
        return self.__resultado

    def soma(self):
        return self.__n1 + self.__n2

    def multiplicacao(self):
        return self.__n1 * self.__n2

    def subtracao(self):
        return self.__n1 - self.__n2


c = Calc(10,20)
assert isinstance(c, Calc)
assert c.soma() == 30
assert c.multiplicacao() == 200
assert c.subtracao() == -10

assert c.get_n1() == 10
assert c.get_n2() == 20

c.set_n1(50)
assert c.set_n1(50) == 50
c.set_n2(100)
assert c.set_n2(100) == 100
assert c.soma() == 150
