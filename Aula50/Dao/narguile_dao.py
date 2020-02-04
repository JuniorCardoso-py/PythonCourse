import MySQLdb
<<<<<<< HEAD
from PythonCourse.Aula50.Model.narguile_model import Narguile_model
=======
from Aula50.Model.narguile_model import Narguile_model
>>>>>>> 5691ac37e1bfa460dd2d1456e6af6e80021d1b72


class Narguile_Dao:
    def __init__(self):
        self.conexao = MySQLdb.connect(host='mysql.topskills.dev', database='topskills01', user='topskills01', passwd='ts2019')
        self.cursor = self.conexao.cursor()


    def salvar(self, narguile:Narguile_model):
        self.cursor.execute(f"INSERT INTO Junior2 (nome_narguile, tamanho, valor) VALUES('{narguile.nome}','{narguile.tamanho}',{narguile.valor})")
        self.conexao.commit()
        id = self.cursor.lastrowid
        narguile.id = id
        return narguile.__dict__

    def listar_tudo(self):
        self.cursor.execute("SELECT * FROM Junior2")
        resultado = self.cursor.fetchall()
        lista_produtos = []
        for produtos in resultado:
            product = Narguile_model(produtos[1],produtos[2],produtos[3],produtos[0])
            lista_produtos.append(product.__dict__)
        return lista_produtos

    def atualizar(self, narguiles:Narguile_model):
        self.cursor.execute(f"UPDATE Junior2 SET nome_narguile = '{narguiles.nome}', tamanho = '{narguiles.tamanho}', valor = {narguiles.valor} WHERE Id ={narguiles.id}")
        self.conexao.commit()

    def remover(self,id):
        self.cursor.execute(f"DELETE FROM Junior2 WHERE Id = {id}")
        self.conexao.commit()


    def buscar_por_id(self,id):
        self.cursor.execute(f"SELECT * FROM Junior2 where Id = {id}")
        resultado = self.cursor.fetchone()
        produto = Narguile_model(resultado[1],resultado[2],resultado[3],resultado[0])
        return produto.__dict__

