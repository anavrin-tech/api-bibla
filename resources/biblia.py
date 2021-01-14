from flask_restful import Resource, reqparse
from model.biblia import BiblaModel

class Biblia(Resource):
    def get(self):
        return{'biblia':[biblia.json() for biblia in BiblaModel.query.all()]}