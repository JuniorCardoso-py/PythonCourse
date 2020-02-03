from PythonCourse.ProgramaHBSIS.Model.model_endereco import Endereco_cliente
class Cliente:
    def __init__(self):
        self.codigo_do_cliente = 0
        self.nome = ''
        self.cpf = ''
        self.data_nasci = ''
        self.id_endereco_cliente = 0
        self.endereco = Endereco_cliente()

    def __str__(self):
        return f"{self.codigo_do_cliente};{self.nome};{self.cpf};{self.data_nasc};{self.id_endereco_cliente}"