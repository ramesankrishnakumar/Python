# how to add validation
from typing import Optional

from pydantic import BaseModel, Field


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: float

    def __init__(
            self,
            book_id: int,
            title: str,
            author: str,
            description: str,
            rating: float,
    ):
        self.id = book_id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating




class BookRequest(BaseModel):
    title: str = Field(min_length=3)
    author: str = Field(min_length=3)
    description: str = Field(min_length=10, max_length=100)
    rating: float = Field(ge=1.0, le=5.0),
    # generated_id: Optional[int] = Field(default=None, description="generated_id is not needed, added for educational purposes")

    model_config = {
        "json_schema_extra" : {
            "example": {
                "title": "Existence of Sayians",
                "author": "Bulma Johnson",
                "description": "A simple book",
                "rating": 4.5,
            }

        }
    }
