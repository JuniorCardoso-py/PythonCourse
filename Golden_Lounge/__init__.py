from flask import Flask
from flask_restful import Api
from Golden_Lounge.Controller.Controller_User import Controller_Usuario


app = Flask(__name__)
api = Api(app)

api.add_resource(Controller_Usuario, '/api/pessoa', endpoint ='pessoa' )
api.add_resource(Controller_Usuario, '/api/pessoa/<int:int>', endpoint ='pessoas')




app.run(debug=True)