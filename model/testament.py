from db import banco

class TestamentModel(banco.Model):
    __tablename__ = 'testament'

    id = banco.Column(banco.Integer, primary_key=True)
    name = banco.Column(banco.String(40))

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def json(self):
        return{
            'id': self.id,
            'name': self.name
        }
    
    @classmethod
    def find_testament(cls, id):
        testament = cls.query.filter_by(id=id).first()
        if testament:
            return testament
        return None