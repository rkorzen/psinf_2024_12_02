from fastapi import FastAPI, HTTPException
from pony.orm import Database, Required, db_session, select

# Konfiguracja bazy danych
db = Database()
db.bind(provider='sqlite', filename='books.db', create_db=True)

# Definicja modelu
class Book(db.Entity):
    title = Required(str)
    author = Required(str)

# Generowanie tabel w bazie danych
db.generate_mapping(create_tables=True)

# Tworzenie aplikacji FastAPI
app = FastAPI()

@app.on_event("startup")
def startup_event():
    print("App started!")

@app.get("/books", response_model=list[dict])
@db_session
def get_books():
    """Pobieranie wszystkich książek"""
    return [{"id": book.id, "title": book.title, "author": book.author} for book in select(b for b in Book)]

@app.post("/books", response_model=dict)
@db_session
def add_book(book: dict):
    """Dodawanie nowej książki"""
    if "title" not in book or "author" not in book:
        raise HTTPException(status_code=400, detail="Title and author are required.")
    new_book = Book(title=book["title"], author=book["author"])
    return {"id": new_book.id, "title": new_book.title, "author": new_book.author}

@app.delete("/books/{book_id}", response_model=dict)
@db_session
def delete_book(book_id: int):
    """Usuwanie książki po ID"""
    book = Book.get(id=book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found.")
    book.delete()
    return {"message": f"Book with ID {book_id} deleted successfully."}
