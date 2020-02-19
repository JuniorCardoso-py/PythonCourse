from flask import request
from Golden_Lounge.Dao.Pessoa_Dao import Pessoas_Dao
from Golden_Lounge.Controller.Base_Controller import Base_Controller
from Golden_Lounge.Model.Model_Pessoa import Tabela_das_pessoas

class Pessoas_Controller(Base_Controller):
    def __init__(self):
        super().__init__(Pessoas_Dao())

    def post(self):
        return super().post(self.request_dados())

    def put(self, id):
        model = self.request_dados()
        model.id = id
        return super().put(model)

    def request_dados(self):
        model = Tabela_das_pessoas()
        model.nome = request.json['nome']
        model.data_nascimento = request.json['data_nascimento']
        model.id = request.json['id']
        return model

