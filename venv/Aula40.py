from flask import Flask
from flask_restful import Api
from Controllers.Cerveja_Controller import CervejaController

app = Flask(__name__)
api = Api(app)

api.add_resource(CervejaController, '/api/cerveja')

@app.route('/')
def inicio():
    return 'Olá Mundo'

app.run(debug=True)