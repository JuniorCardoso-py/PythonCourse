class Endereco_cliente:
    def __init__(self):
        self.id_endereco = 0
        self.estado_nascimento = ''
        self.cidade = ''
        self.cep = ''
        self.bairro = ''
        self.rua = ''
        self.numero = 0
        self.complemento = ''

    def __str__(self):
        return f"{self.id_endereco};{self.estado_nascimento};{self.cidade};{self.cep};{self.bairro};{self.rua};{self.numero};{self.complemento}"