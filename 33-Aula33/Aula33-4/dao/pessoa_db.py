#----- Importar biblioteca do Mysql
import MySQLdb
from model.pessoa import Pessoa

class PessoaDb:
    #----- Configurar a conexão
    conexao = MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user='topskills01', passwd='ts2019')
    #----- Salva o cursor da conexão em uma variável
    cursor = conexao.cursor()
    
    def listar_todos(self):
        #----- Criação do comando SQL e passado para o cursor
        comando_sql_select = "SELECT * FROM 01_MDG_PESSOA"
        self.cursor.execute(comando_sql_select)
        #---- Pega todos os resultados da execução do comando SQL e armazena em uma variável
        resultado = self.cursor.fetchall()
        lista_pessoas_classe = self.converter_tabela_classe(resultado)
        return lista_pessoas_classe

    def buscar_por_id(self, id):
        #----- Criação do comando SQL e passado para o cursor
        comando_sql_select = f"SELECT * FROM 01_MDG_PESSOA WHERE ID= {id}"
        self.cursor.execute(comando_sql_select)
        resultado = self.cursor.fetchone()
        return resultado

    def converter_tabela_classe(self, lista_tuplas):
        #cria uma lista para armazenar os dicionarios
        lista_pessoas = []
        for p in lista_tuplas:
            #----- Criação do objeto da classe pessoa
            p1 = Pessoa()
            #--- pega cada posição da tupla e atribui a uma chave do dicionário
            p1.id = p[0]
            p1.nome = p[1]
            p1.sobrenome= p[2]
            p1.idade = p[3]
            p1.endereco_id = p[4]
            lista_pessoas.append(p1)
        return lista_pessoas