from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import models
import schemas


models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Connect Solutions",
    description="Fornece Api-Biblia para soluções Connect Church",
    version="1.0.1"
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/', tags=["Index"])
async def index():
    return{
        'Project': 'Connect Solutions - Api Biblia',
        'Development': 'David Borges',
        'phone': '+55 34 9 9967-9387',
        'language': 'Python3.8.1',
        'Data': '09/01/2021',
        'Description': 'Fornecer Biblia para Connect Solutions, versões nvi e acf.'
    }


@app.get('/nvi', tags=["Versão: NVI"])
async def biblia_nvi(book_id: int = None, chapter: int = None, verse: int = None, db: Session = Depends(get_db), offset: int = 0, limit: int = 100):
    '''
        Atributos passado pelo Path:
        book_id,
        chapter,
        verse
    '''
    nvi = db.query(models.Nvi)

    if book_id:
        nvi = nvi.filter(models.Nvi.book_id >= book_id)

    if chapter:
        nvi = nvi.filter(models.Nvi.chapter >= chapter)

    if verse:
        nvi = nvi.filter(models.Nvi.verse >= verse)

    nvi = nvi.offset(offset).limit(limit).all()

    if nvi == []:
        raise HTTPException(status_code=404, detail="Item not found")
    return nvi


@app.get('/acf', tags=["Versão: ACF"])
async def biblia_acf(book_id: int = None, chapter: int = None, verse: int = None, db: Session = Depends(get_db), offset: int = 0, limit: int = 100):

    acf = db.query(models.Acf)

    if book_id:
        acf = acf.filter(models.Acf.book_id == book_id)

    if chapter:
        acf = acf.filter(models.Acf.chapter == chapter)

    if verse:
        acf = acf.filter(models.Acf.verse == verse)

    acf = acf.offset(offset).limit(limit).all()
    return acf
