from db import banco

class BiblaModel(banco.Model):
    __tablename__ = 'biblia'

    id = banco.Column(banco.Integer, primary_key=True)
    book_id = banco.Column(banco.Integer)
    book = banco.Column(banco.String(40))
    chapter = banco.Column(banco.Integer)
    verse = banco.Column(banco.Integer)
    text = banco.Column(banco.String(255))

    def __init__(self, id, book_id, book, chapter, verse, text):
        self.id = id
        self.book_id = book_id
        self.book = book
        self.chapter = chapter
        self.verse = verse
        self.text = text

    def json(self):
        return{
            'id':self.id,
            'book_id':self.book_id,
            'book':self.book,
            'chapter':self.chapter,
            'verse':self.verse,
            'text':self.text
        }

    @classmethod
    def find_biblia(cls, id):
        biblia = cls.query.filter_by(id=id).first()
        if biblia:
            return biblia
        return None

