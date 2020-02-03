import MySQLdb


class PessoaDao:
    def __init__(self):
        self.connection = MySQLdb.connect(host='mysql.topskills.dev', database='topskills01', user='topskills01', passwd='ts2019')
        self.cursor = self.connection.cursor()

    def list_all(self):
        self.cursor.execute("SELECT * FROM 01_MDG_PESSOA")
        pessoas = self.cursor.fetchall()
        lista_pessoa = []
        for p in pessoas:
            pessoa = PessoaModel(p[1], p[2], p[3], p[0])
            lista_pessoa.append(pessoa.__dict__)
        return lista_pessoa

    def get_by_id(self, id):
        self.cursor.execute("SELECT * FROM 01_MDG_PESSOA WHERE ID = {}".format(id))
        pessoa = self.cursor.fetchone()
        p = PessoaModel(pessoa[1], pessoa[2], pessoa[3], pessoa[0])
        return p.__dict__

    def insert(self, pessoa):
        return 'Adicionando a pessoa : {}'.format(pessoa)
    def update(self, pessoa):
        return 'Alterando a pessoa : {}'.format(pessoa)
    def remove(self, id):
        self.cursor.execute("DELETE FROM 01_MDG_PESSOA WHERE ID = {}".format(id))
        self.connection.commit()
        return 'Removido a pessoa de id : {}'.format(id)