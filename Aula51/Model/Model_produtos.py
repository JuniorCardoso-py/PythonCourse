#--- Importação da classe principal do alchemy
import sqlalchemy as db
#--- Importação do metodo para gerar a classe base do Alchemy que fará o mapeamento da tabela do banco de dados
from sqlalchemy.ext.declarative import declarative_base
#--- Geração da classe que sera usado na herança para mapear a tabela do banco de dados
BaseAlchemy = declarative_base()

#--- Criação da classe para model produto usando herança da classe base do alchemy criada na linha anterior
class ProdutoModel(BaseAlchemy):
    #--- variável que define qual tabela será usada para mapear a classe
    __tablename__ = "Produto"
    #--- Declaração de variáveis que serão mapeadas de acordo com as colunas da tabela no banco de dados
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(length=100))
    descricao = db.Column(db.String(length=200))

    #--- Sobreescrita do método para conversão do objeto da classe em uma string para imprimir as variáveis
    def __str__(self):
        return "{}-{}-{}".format(self.id, self.nome,self.descricao)