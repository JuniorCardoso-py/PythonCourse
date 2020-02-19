# Rev Classe
# Métodos de classe
# Método __init__  =  construtor
# Variáveis de classe
# Variáveis privadas
# Metodos Getters e Setters

class Calc:
    def __init__(self, numero1, numero2):
        # variável de classe
        self.__n1 = numero1
        self.__n2 = numero2
        self.__resultado = 0

    def set_n1(self, valor):
        self.__n1 = valor
    def get_n1(self):
        return self.__n1

    def set_n2(self, valor):
        self.__n2 = valor
    def get_n2(self):
        return self.__n2

    def get_resultado(self):
        return self.__resultado

    def soma(self):
        self.__resultado = self.__n1 + self.__n2

    def subtracao(self):
        self.__resultado = self.__n1 - self.__n2

    def multiplicacao(self):
        self.__resultado = self.__n1 * self.__n2



# Instanciando um objeto da classe Calc
c = Calc(10,20)
print(c.get_n1())
print(c.get_n2())
c.set_n1(1000)
c.set_n2(18000)
print(c.get_n1())
print(c.get_n2())
