from sqlalchemy.orm import Session
import models
import schemas


def list_book_with_filter(db: Session, book_id: int = None):
    if book_id:
        return db.query(models.Nvi).filter(models.Nvi.book_id == book_id).all()
    return db.query(models.Nvi).all()
