from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

dane = []

class RequestManagement(Resource):
    def get(self):
        return dane
    def post(self):
        dane.append(request.get_json(force=True))
        

api.add_resource(RequestManagement, '/')


app.run()