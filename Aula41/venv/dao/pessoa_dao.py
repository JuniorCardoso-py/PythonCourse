import MySQLdb


conexao = MySQLdb.connect(host='127.0.0.1' ,database= 'exercicio_restful',user='root' ,passwd = '')
cursor = conexao.cursor()


class PessoaDao:
    def __init__(self):
        self.conexao = MySQLdb.connect(host='127.0.0.1', database='exercicio_restful', user='root', passwd='')
        self.cursor = conexao.cursor()

    def list_all(self):
        return 'listando todos os dados da tabela'

    def get_by_id(self,id):
        return f'Listando o dado de id: {id}'

    def insert(self,pessoa):
        return f'Cadastrando uma pessoa:{pessoa}'

    def update(self,pessoa):
        return  f'Alterando uma pessoa:{pessoa}'

    def remove(self,id):
        return f'Acessando metodo DELETE: {id}'