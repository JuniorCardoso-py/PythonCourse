#======= Estruturas de dados e DB

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

def converter_tabela_dicionario(lista_tuplas):
    #cria uma lista para armazenar os dicionarios
    lista_pessoas = []
    for p in lista_tuplas:
        #----- Criação do dicionario que representa uma pessoa
        dicionario_pessoa = {'Id': 0, 'Nome' : '', 'Sobrenome': '', 'Idade' : 0, 'Endereco_Id': 0}
        #--- pega cada posição da tupla e atribui a uma chave do dicionário
        dicionario_pessoa['Id'] = p[0]
        dicionario_pessoa['Nome'] = p[1]
        dicionario_pessoa['Sobrenome'] = p[2]
        dicionario_pessoa['Idade'] = p[3]
        dicionario_pessoa['Endereco_Id'] = p[4]
        lista_pessoas.append(dicionario_pessoa)
    return lista_pessoas

def exportar_txt(lista_pessoas):
    #----- Cria um arquivo e atribui a uma variável 'arquivo'
    with open('33-Aula33/pessoas2.txt','a') as arquivo:
        #---- Percorre a lista de dicionário e salva no arquivo em formato pré-definido
        for p in lista_pessoas:
            arquivo.write(f"{p['Id']};{p['Nome']};{p['Sobrenome']};{p['Idade']};{p['Endereco_Id']}\n")

lpt = listar_todos()
lpd = converter_tabela_dicionario(lpt)
exportar_txt(lpd)