from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import Book as DBBook, get_db  # Import the SQLAlchemy Book model as DBBook to avoid confusion

class BookCreate(BaseModel):  # Define a Pydantic model to handle book creation requests
    title: str
    author: str

app = FastAPI()

#add a single book
@app.post("/book", response_model=dict)
def add_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = DBBook(title=book.title, author=book.author)  # Create an instance of the SQLAlchemy model
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return {"message": "Book added to the database", "id": db_book.id}

#get all books
@app.get("/books/", response_model=list[dict])
def get_books(db: Session = Depends(get_db)):
    books = db.query(DBBook).all()
    return [{"id": book.id, "title": book.title, "author": book.author} for book in books]

#get a single book by id
@app.get("/books/{book_id}", response_model=dict)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(DBBook).filter(DBBook.id == book_id)
    if book:
        return {"id": book.id, "title": book.title, "author": book.author}
    else:
        return {"message": "Book not found"}
    
#delete a single book by id
@app.delete("/books/{book_id}", response_model=dict)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(DBBook).filter(DBBook.id == book_id)
    if book:
        db.delete(book)
        db.commit()
        return {"message": "Book deleted successfully"}
    else:
        return {"message": "Book not found"}
    

#put method to update a book
@app.put("/books/{book_id}", response_model=dict)
def update_book(book_id: int, book: BookCreate, db: Session = Depends(get_db)):
    db_book = db.query(DBBook).filter(DBBook.id == book_id)
    if db_book:
        db_book.title = book.title
        db_book.author = book.author
        db.commit()
        return {"message": "Book updated successfully"}
    else:
        return {"message": "Book not found"}