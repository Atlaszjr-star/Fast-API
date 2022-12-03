from fastapi import FastAPI

app = FastAPI()
BOOKS = {
    'book_1': {'title': 'Title One', 'author': 'Author One'},
    'book_2': {'title': 'Title Two', 'author': 'Author Two'},
    'book_3': {'title': 'Title Three', 'author': 'Author Three'},
    'book_4': {'title': 'Title Four', 'author': 'Author Four'},
    'book_5': {'title': 'Title Five', 'author': 'Author Five'},
}


# creating a new HTTP Route in FastAPI
@app.get("/")
async def read_all_books():
    return BOOKS

'''
this has to be in front of @app.get("/books/{book_id}")
otherwise 'mybook' will be viewed as integer parameter {book_id}
if use path parameter, the path parameters must be underneath
any kind of API that's going to be following the same kind of path
'''


@app.get("/books/mybook")
async def read_favorite_book():
    return {"book_title": "My favorite Book"}


@app.get("/books/{book_id}")
async def read_all_book_id(book_id: int):
    return {"book_id": book_id}



