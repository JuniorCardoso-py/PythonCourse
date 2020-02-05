from flask_restful import Resource
from flask import request

from Aula50.Dao.narguile_dao import Narguile_Dao
from Aula50.Model.narguile_model import Narguile_model


class Narguile_controller(Resource):
    def __init__(self):
        self.dao = Narguile_Dao()

    def get(self, id=None):
        if id:
            msg_json = self.dao.buscar_por_id(id)
            return msg_json
        return self.dao.listar_tudo()

    def post(self):
        nome = request.json['nome']
        tamanho = request.json['tamanho']
        valor = int(request.json['valor'])
        narguile = Narguile_model(nome,tamanho,valor)
        msg_json = self.dao.salvar(narguile)
        return msg_json

    def put(self,id):
        nome = request.json['nome_narguile']
        tamanho = request.json['tamanho']
        valor = int(request.json['valor'])
        narguile = Narguile_model(nome,tamanho,valor,id)
        msg_json = self.dao.atualizar(narguile)
        return msg_json

    def delete(self,id):
        return self.dao.remover(id)