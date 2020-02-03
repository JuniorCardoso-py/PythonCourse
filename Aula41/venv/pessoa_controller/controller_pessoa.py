from flask_restful import Resource
from dao.pessoa_dao import PessoaDao


class PessoaController(Resource):
    def __init__(self):
        self.dao = PessoaDao()

    def get(self, id=None):
        if id:
            return self.dao.get_by_id(id)
        return self.dao.list_all()


    def post(self):
        msg = self.dao.insert('')
        return msg

    def put(self):
        msg = self.dao.update('')
        return msg

    def delete(self, id):
        return self.dao.remove(id)
