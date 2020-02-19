from flask import request
from Golden_Lounge.Controller.Base_Controller import Base_Controller
from Golden_Lounge.Dao.Usuario_Dao import Usuario_dao
from Golden_Lounge.Model.Model_Pessoa import User




class Controller_Usuario(Base_Controller):
    def __init__(self):
        super().__init__(Usuario_dao())

    def post(self):
        return super().post(self.request_dados())

    def put(self, id):
        model = self.request_dados()
        model.id = id
        return super().put(model)

    def request_dados(self):
        model = User()
        model.email = request.json["email"]
        model.senha= request.json["senha"]
        model.pessoa_id= request.json["pessoa_id"]
        model.pessoa = request.json["pessoa"]
        model.id = request.json["id"]
        return model
