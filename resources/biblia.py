from flask_restful import Resource, reqparse
from model.biblia import BiblaModel
import sqlite3

def normalize_path_params(book_id=1,book=None,chapter=1,verse=1,text=None,limit=50,offset=0,**dados):
    if book_id:
        return{
            'book_id':book_id,
            'book':book,
            'chapter':chapter,
            'verse':verse,
            'text':text,           
            'limit':limit,
            'offset':offset
        }
    return{
        'book':book,
        'chapter':chapter,
        'verse':verse,
        'text':text,
        'limit':limit,
        'offset':offset
    }


# path /bilia?book_id=5&chapter=3&verse=7
path_params = reqparse.RequestParser()
path_params.add_argument('book_id', type=int)
#path_params.add_argument('book', type=str)
path_params.add_argument('chapter', type=int)
path_params.add_argument('verse', type=int)
#path_params.add_argument('text', type=str)
path_params.add_argument('limit', type=int)
path_params.add_argument('offset', type=int)

class Biblia(Resource):
    def get(self):

        connection = sqlite3.connect('banco.db')
        cursor = connection.cursor()

        dados = path_params.parse_args()
        dados_validos = {chave:dados[chave] for chave in dados if dados[chave] is not None}
        parametros = normalize_path_params(**dados_validos)

        
        if not parametros.get('book_id'):
            consulta = "SELECT * FROM biblia WHERE chapter > ? and  verse > ? LIMIT ? OFFSET ?"
            tupla = tuple([parametros[chave] for chave in parametros])
            resultado = cursor.execute(consulta, tupla)
        else:
            consulta = "SELECT * FROM biblia WHERE book_id > ? and chapter > ? and  verse > ? LIMIT ? OFFSET ?"
            tupla = tuple([ parametros[chave] for chave in parametros])
            resultado = cursor.execute(consulta, tupla)

        biblia = []
        for linha in resultado:
            biblia.append({
                'id':linha[0],
                'book_id':linha[1],
                'book':linha[2],
                'chapter':linha[3],
                'verse':linha[4],
                'text':linha[5]
            })

        return{'biblia':[biblia.json() for biblia in BiblaModel.query.all()]}