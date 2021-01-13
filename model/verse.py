from db import banco

class VerseModel(banco.Model):
    __tablename__ = 'verse'

    id = banco.Column(banco.Integer, primary_key=True)
    book_id = banco.Column(banco.Integer)
    chapter = banco.Column(banco.Integer)
    verse = banco.Column(banco.Integer)
    text = banco.Column(banco.String(255))

    def __init__(self, id, book_id, chapter, verse, text):
        self.id = id
        self.book_id = book_id
        self.chapter = chapter
        self.verse = verse
        self.text = text

    def json(self):
        return{
            'id': self.id,
            'book_id': self.book_id,
            'chapter': self.chapter,
            'verse': self.verse,
            'text': self.text
        }
    
    @classmethod
    def find_verse(cls, id):
        verse = cls.query.filter_by(id=id).first()
        if verse:
            return verse
        return None