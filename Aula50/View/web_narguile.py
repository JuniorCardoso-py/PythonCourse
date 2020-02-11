from flask import Flask
from flask_restful import Api

from Aula50.Controller.narguile_controller import Narguile_controller

app = Flask(__name__)
api = Api(app)

api.add_resource(Narguile_controller, '/api/narguile', endpoint='narguiles')
api.add_resource(Narguile_controller, '/api/narguile/<int:id>', endpoint='narguile')


app.run(debug=True)