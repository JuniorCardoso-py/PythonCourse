
class Model_timee:
    def __init__(self):
        self.ID = 0
        self.nome = ''
        self.descricao= ''
        self.numeropessoas = 0
        self.linguagemback =
        self.framework =

    def __str__(self):
        return f'{self.ID};{self.nome};{self.descricao};{self.numeropessoas};{self.linguagemback};{self.framework}'

pessoas = Model_timee