from flask import Flask
from flask_restful import Api

from Aula51.Dao.Produto_Dao import Dao_metodos


app = Flask(__name__)
api = Api(app)

api.add_resource(Dao_metodos, '/api/Narguile', endpoint='narguiles')
api.add_resource(Dao_metodos, '/api/Narguile<int:id>', endpoint='narguile')


app.run(debug=True)