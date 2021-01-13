from db import banco

class BookModel(banco.Model):
    __tablename__ = 'book'

    id = banco.Column(banco.Integer, primary_key=True)
    book_reference_id = banco.Column(banco.Integer)
    testament_reference_id = banco.Column(banco.Integer)
    name = banco.Column(banco.String(40))

    def __init__(self, id, book_reference_id, testament_reference_id, name):
        self.id = id
        self.book_reference_id = book_reference_id
        self.testament_reference_id = testament_reference_id
        self.name = name

    def json(self):
        return{
            'id': self.id,
            'book_reference_id': self.book_reference_id,
            'testament_reference_id': self.testament_reference_id,
            'name': self.name
        }
    
    @classmethod
    def find_book(cls, id):
        book = cls.query.filter_by(id=id).first()
        if book:
            return book
        return None