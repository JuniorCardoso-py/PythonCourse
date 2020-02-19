from Golden_Lounge.Model.Base_Model import Base
from Golden_Lounge.Model.Cadastro_Model import Tabela_das_pessoas
import sqlalchemy as db
from passlib.hash import pbkdf2_sha512

from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(550), nullable=False)
    senha = db.Column(db.String(550), nullable=False)
    pessoa_id = db.Column(db.Integer, db.ForeignKey("cadastros.id"))
    pessoa = relationship(Tabela_das_pessoas)

    def gerador_de_hash(self):
        self.senha = pbkdf2_sha512.hash(self.senha)

    def verifcador_de_senha(self,senha):
        return pbkdf2_sha512.verify(senha, self.senha)

    def __init__(self,email, senha, pessoa_id, pessoa, id=None):
        self.email = email
        self.senha = senha
        self.pessoa_id = pessoa_id
        self.pessoa = pessoa
        self.id = id

    def serializer(self):
        return {'id': self.id, 'email': self.email, 'senha': self.senha, 'pessoa_id': self.pessoa_id, 'pessoa': self.pessoa.serializer()}