from flask_restful import Resource, reqparse
from model.verse import VerseModel

class Verse(Resource):
    def get(self):
        return{'verse': [verse.json() for verse in VerseModel.query.all() ]}