from fastapi import FastAPI

# from models.Book import Book # relative import fails
# hence absolute import path from Level_2
from fast_api.models.Book import Book, BookRequest

app = FastAPI()

books = [
    Book(book_id=1, title='Computer Science', author='Roby', description='A beginners book to computer science',rating= 5),
    Book(book_id=2, title='Math Basics', author='Toby', description='An intermediate book to computer science', rating=4.5),
    Book(book_id=3, title='Physics Introduction', author='Coby', description='Physics for dummies', rating=4.3),
    Book(book_id=4, title='Intro To Chemistry', author='Dolby', description='Chemistry for grade 12', rating=4.9),
    Book(book_id=5, title='Machine Tooling', author='Scooby', description='Intro to machine tooling for sophomore year', rating=4.2),
]

@app.get("/books")
def get_books():
    return books


@app.get("/books/{book_id}")
async def get_book_by_id(book_id: int):
    for book in books:
        if book.id == book_id:
            return book


@app.post("/books")
async def create_book(book_request : BookRequest):
    new_book = Book(
        get_new_book_id(),
        **book_request.model_dump()
    )
    books.append(new_book)
    return new_book




def get_new_book_id() -> int:
    return 1 if(len(books) == 0) else books[-1].id + 1