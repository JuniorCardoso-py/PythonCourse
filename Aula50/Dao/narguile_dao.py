import MySQLdb
from PythonCourse.Aula50.Model.narguile_model import Narguile_model


class Narguile_Dao:
    def __int__(self):
        self.conexao = MySQLdb.connect(host='mysql.topskills.dev', database='topskills01', user='topskills01', passwd='ts2019')
        self.cursor = self.conexao.cursor()


    def salvar(self, narguile:Narguile_model):
        self.cursor.execute(f"INSERT INTO Junior2(nome_narguile,tamanho,valor) VALUES('{self.narguile.nome}','{self.narguile.tamanho}',{self.narguile.valor})")
        self.conexao.commit()
        id = self.cursor.lastrowid
        narguile.id = id
        return narguile.__dict__

    def listar_tudo(self):
        self.cursor.execute("SELECT * FROM Junior2")
        resultado = self.cursor.fetchall()
        lista_produtos = []
        for produtos in resultado:
            produtos = Narguile_model(produtos[1],produtos[2],produtos[3],produtos[0])
            lista_produtos.append(produtos.__dict__)
        return lista_produtos

    def atualizar(self, narguile:Narguile_model):
        self.cursor.execute(f"UPDATE Junior2 SET nome_narguile = {narguile.nome}, tamanho = {narguile.tamanho}, valor = {narguile.valor} WHERE Id ={narguile.id}")
        self.conexao.commit()

    def remover(self,id):
        self.cursor.execute(f"DELETE FROM Junior2 WHERE Id = {id}")
        self.conexao.commit()

    def buscar_por_id(self,id):
        self.cursor.execute(f"SELECT * FROM Junior2 where Id = {id}")
        resultado = self.cursor.fetchone()
        return resultado

