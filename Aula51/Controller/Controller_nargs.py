#ORM
# ---- SqlAlchemy
#---- Instalação do framework
#--- pip3 install sqlalchemy

#---- Conector do Mysql
#---- Instalação do conector do Mysql
#---- pip3 install mysql-connector-python

from Aula51.Dao.Produto_Dao import ProdutoDao

#--- Teste de listagem dos dados de uma tabela
#--- Utilização da classe dao de produtos que utiliza uma classe base que contem os dados de acesso a base de dados
dao = ProdutoDao()
produtos = dao.list_all()
print(produtos)
for p in produtos:
    print(p)