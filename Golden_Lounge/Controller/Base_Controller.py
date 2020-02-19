from flask_restful import Resource
from Golden_Lounge.Dao.Base_Dao import Base_Dao

class Base_Controller(Resource):
    def __init__(self, dao:Base_Dao):
        self.dao = dao

    def get(self, id=None):
        if id:
            return self.dao.buscar_por_id(id)
        return self.dao.listar_todos()

    def post(self,model):
        self.dao.inserir(model)

    def put(self,model):
        self.dao.atualizar(model)

    def deletar(self,id):
        self.dao.deletar(id)