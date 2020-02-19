import sqlalchemy as db
from sqlalchemy.orm.session import sessionmaker

class Base_Dao:
    def __init__(self, table):
        self.table = table
        conexao = db.create_engine("mysql+mysqlconnector://root:@127.0.0.1:3306/usuarios")
        criador_de_sessao = db.orm.sessionmaker()
        criador_de_sessao.configure(bind=conexao)
        self.sessao = criador_de_sessao()

    def listar_todos(self):
        lista_dados = []
        lista = self.sessao.query(self.table).all()
        for user in lista:
            lista_dados.append(user.serializer())
        return lista_dados

    def buscar_por_id(self,id):
        return self.sessao.query(self.table).filter_by(id = id).one()

    def inserir(self, model_desejado):
        self.sessao.add(model_desejado)
        self.sessao.commit()

    def atualizar(self, model_desejado):
        self.sessao.merge(model_desejado)
        self.sessao.commit()

    def deletar(self,id):
        self.sessao.delete(self.buscar_por_id(id))
        self.sessao.commit()

