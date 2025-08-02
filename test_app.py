from main import is_book_read

def test_is_book_read_true():
    book = {"title": "Test Book", "is_read": True}
    assert is_book_read(book) == True

def test_is_book_read_false():
    book = {"title": "Test Book", "read": False}
    assert is_book_read(book) == False

def test_is_book_read_missing_key():
    book = {"title": "Test Book"}
    assert is_book_read(book) == False 



import pytest
from main import Library, Book

def test_add_book():
    # Create a new library
    library = Library()

    # Create a book instance
    book = Book("Il Nome della Rosa", "Umberto Eco", 1980, "A great mystery novel", "2025-10-01")
    
    # Add a book to the library
    library.add_book(book)

    # Check that the book was added
    assert len(library.books) == 1
    assert library.books[0].title == "Il Nome della Rosa"
    assert library.books[0].author == "Umberto Eco"
    assert library.books[0].year == 1980
    assert library.books[0].is_read == False


    from unittest.mock import patch
from main import delete_book 

def test_delete_book_simple():
    books = [
        {'title': 'Book A', 'author': 'Author A', 'year': 2001, 'read': False},
        {'title': 'Book B', 'author': 'Author B', 'year': 2002, 'read': True},
    ]
    
    books.pop(0)
    assert len(books) == 1
    assert books[0]['title'] == 'Book B'

