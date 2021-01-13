from flask_restful import Resource, reqparse
from model.book import BookModel

class Book(Resource):
    def get(self):
        return{'book': [book.json() for book in BookModel.query.all() ]}