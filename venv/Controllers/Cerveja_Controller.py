from flask_restful import Resource
class CervejaController(Resource):
    def get(self):
        return 'Acessando a API usando o metodo HTTP GET'
    def post(self):
        return 'Acessando a API usando o metodo HTTP POST'
    def put(self):
        return 'Acessando a API usando o metodo HTTP PUT'
    def delete(self):
        return 'Acessando a API usando o metodo HTTP DELETE'
