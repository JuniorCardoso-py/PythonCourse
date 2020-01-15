### Classes
import MySQLdb

def listar_todos():
    # Configurando conexão
    conexao = MySQLdb.connect(host='127.0.0.1',database= 'junior_aula_bancodados', user='root', passwd='')
    # Cursor da variavel de conexão
    cursor = conexao.cursor()
    #Criação do dicionario que representa uma pessoa
    # Criação do comando SQL  e passado para o cursor
    cursor.execute("SELECT * FROM pessoa")
    resultado = cursor.fetchall() # fetchall pegar toods os reultados que estão na tabela selecionada e fetchone pegar apenas um resultado
    return resultado


def converte_tabela_dicionario(lista_tuplas):
    lista_pessoa = []
    for p in lista_tuplas:
        dicionario_pessoa = {'ID': 0, 'Nome': '', 'Sobrenome': '', 'Idade': 0, 'Endereco_Id': 0}
        dicionario_pessoa['ID'] = p[0]
        dicionario_pessoa['Nome'] = p[1]
        dicionario_pessoa['Sobrenome'] = p[2]
        dicionario_pessoa['Idade'] = p[3]
        dicionario_pessoa['Endereco_Id'] = p[4]
        lista_pessoa.append(dicionario_pessoa)
    return lista_pessoa

def exportar_txt(lista_pessoa):
    with open('Aula32.txt', 'w') as arquivo:
        for p in lista_pessoa:
            arquivo.write(f"{p['ID']};{p['Nome']};{p['Sobrenome']};{p['Idade']};{p['Endereco_Id']}\n")


lpt = listar_todos()
lpd = converte_tabela_dicionario(lpt)
exportar_txt(lpd)