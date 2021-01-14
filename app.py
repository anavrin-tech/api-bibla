# Project: Api-Biblia
# Development: David Borges
# Version: 0.0.1
# language: Python | flask_restful
# Data: 09/01/2021

from flask import Flask
from flask_restful import Resource, Api
from resources.book import Book
from resources.testament import Testament
from resources.verse import Verse
from resources.biblia import Biblia

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def cria_banco():
    banco.create_all()

class Index(Resource):
    def get(self):
        return{
                'Project': 'Connect Solutions - Api Biblia',
                'Development': 'David Borges',
                'phone':'+55 34 9 9967-9387',
                'language':'Python3.8.1',
                'Data':'09/01/2021',
                'Description':'Fornecer Biblia para Connect Solutions, versões nvi e acf.'
        }, 200

api.add_resource(Index, '/')
api.add_resource(Book, '/book')
api.add_resource(Testament, '/testament')
api.add_resource(Verse, '/verse')
api.add_resource(Biblia, '/biblia')

if __name__ == '__main__':
    from db import banco
    banco.init_app(app)
    app.run(port=3000, debug=True)