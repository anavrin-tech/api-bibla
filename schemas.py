from typing import Optional
from pydantic import BaseModel


class NVIBase(BaseModel):
    book_id: Optional[int] = None
    chapter: Optional[int] = None
    verse: Optional[int] = None

    class Config:
        schema_extra = {
            "example_url": {
                'example': 'http://localhost:3000/nvi?book_id=5&chapter=4&verse=5&offset=0&limit=100'
            }
        }
