from fastapi import FastAPI, Body

app = FastAPI()

new_book_id = 6
books = [
    {"id": 1, "title": "C Programming", "author": "John", "category": "Programming"},
    {"id": 2, "title": "Python Programming", "author": "Mario", "category": "Math"},
    {"id": 3, "title": "Java Programming", "author": "Jack", "category": "Science"},
    {"id": 4, "title": "Kotlin Programming", "author": "Jim", "category": "Arts"},
    {"id": 5, "title": "SQL Fundamentals", "author": "Jil", "category": "Statistics"},
]

# run instructions
""" 
poetry shell
uvicorn --reload fast_api.books_api:app 
"""


@app.get("/books")
def get_books():
    return books


@app.get("/books/{book_id}")
async def get_book_by_id(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            return book


@app.get("/books/search/{book_title}")
async def search_book(book_title: str, category: str = None):
    matched_books = []
    for book in books:
        if not category:
            if book["title"].casefold() == book_title.casefold():
                matched_books.append(book)
        else:
            if book["title"].casefold() == book_title.casefold() and book["category"].casefold() == category.casefold():
                matched_books.append(book)

    return matched_books


@app.post("/books")
async def create_book(book = Body() ) -> dict:
    global new_book_id # python way to modify global variables
    book["id"] = new_book_id
    books.append(book)
    new_book_id += 1
    return book

@app.put("/books/{book_id}")
async def update_book(book_id: int, updated_book = Body()) -> dict:
    for book in books:
        if book["id"] == book_id:
            book["title"] = updated_book["title"]
            book["author"] = updated_book["author"]
            book["category"] = updated_book["category"]
            return book
    return {}

@app.delete("/books/{book_id}")
async def delete_book(book_id: int) -> bool:
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return True
    return False
