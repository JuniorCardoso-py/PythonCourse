import MySQLdb

class Conector:
    def pegar_dados_banco():
        conexao = MySQLdb.connect(host='127.0.0.1', database='junior_aula_bancodados', user='root', passwd='')
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM endereco')
        dados = cursor.fetchall()
        return dados

class Tratamento:
    def separar_tuplas_em_dicionario(self, lista_tuplas):
        lista_tuplas = []
        for pessoas in self.pegar_dados_banco():
            dicionario = {'Logradouro': '', 'Numero': 0, 'Complemento': '', 'Bairro': '', 'Cidade': '', 'Endereco': ''}
            dicionario['Logradouro'] = pessoas[0]
            dicionario['Numero'] = pessoas[1]
            dicionario['Complemento'] = pessoas[2]
            dicionario['Bairro'] = pessoas[3]
            dicionario['Cidade'] = pessoas[4]
            dicionario['Endereco'] = pessoas[5]
            lista_tuplas.append(dicionario)
        return lista_tuplas