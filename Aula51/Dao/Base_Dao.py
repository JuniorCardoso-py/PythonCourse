#--- Importação da classe principal do alchemy
import sqlalchemy as db

#--- Criação da classe base de acessoa ao banco de dados
class BaseDao:
    #--- declaração do método construtor para definir as configurações de acesso ao banco de dados
    def __init__(self):
        #--- Declaração da engine de acesso passando as informações para conectar ao banco de dados
        # ----database+conector://user:passwd@url:porta/database
        conexao = db.create_engine("mysql+mysqlconnector://topskills01:ts2019@mysql.topskills.dev:3306/topskills01")
        #--- Declaração da variável para geração de uma sessao com o banco de dados
        criador_sessao = db.orm.sessionmaker()
        #--- Configuração para que a sessão ao ser gerada, utilize os dados de acesso ao banco criados nas linhas anteriores
        criador_sessao.configure(bind=conexao)
        #--- Criação de uma sessao com o banco de dados
        self.sessao = criador_sessao()