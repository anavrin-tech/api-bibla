from flask_restful import Resource, reqparse
from model.testament import TestamentModel

class Testament(Resource):
    def get(self):
        return{'testament': [testament.json() for testament in TestamentModel.query.all() ]}