from fastapi import FastAPI

app = FastAPI()

@app.get("/books/{id}")
def read_book(id: int):
    return {
        "id": id,
        "title": "1984",
        "author": "George Orwell",
        "availability": True
    }