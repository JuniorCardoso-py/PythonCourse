#----- Importar biblioteca do Mysql
import MySQLdb

def listar_todos():
    #----- Configurar a conexão
    conexao = MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user='topskills01', passwd='ts2019')
    #----- Salva o cursor da conexão em uma variável
    cursor = conexao.cursor()
    #----- Criação do comando SQL e passado para o cursor
    comando_sql_select = "SELECT * FROM 01_MDG_PESSOA"
    cursor.execute(comando_sql_select)
    #---- Pega todos os resultados da execução do comando SQL e armazena em uma variável
    resultado = cursor.fetchall()
    return resultado