from Golden_Lounge.Model.Base_Model import Base
import sqlalchemy as db


class Tabela_das_pessoas(Base):
    __tablename__ = "cadastros"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(45))
    data_nascimento = db.Column(db.DATE)

    def __init__(self,nome,datanasc,id=None):
        self.nome = nome
        self.data_nascimento = datanasc
        self.id = id

    def serializer(self):
        return {'id':self.id, 'nome':self.nome, 'data_nascimento':str(self.data_nascimento)}

