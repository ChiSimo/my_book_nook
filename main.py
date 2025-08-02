# Import Colorama to add colors to the text
from colorama import Fore, Style, init
# This makes the color to go back to normal after each print
init(autoreset=True)

# This adds a date when a new book joins the library 
from datetime import datetime

# This save and loads books from a file
import json

# Start of the App
print(Fore.CYAN + "📚 Welcome to My book Nook 📚")
print("-----------------------------")


class Book:
    def __init__(self, title, author, year, review, added_on, is_read=False):
        # These lines save the data inside the object
        self.title = title
        self.author = author
        self.year = year
        self.review = review
        self.added_on = added_on   # Date the book was added
        self.is_read = is_read    # Wheter the book is marked as read (default is False)

class Library:
    def __init__(self):
        self.books = []  # This list will hold all the books

    def add_book(self, book):
        self.books.append(book)  # Add a book to the list

    def show_books(self):
        if not self.books:
            # If there are no books, show a friendly message
            print("Your bookshelf is waiting for its first story... grab a cup of coffee and add a book! ☕️📖 ")
            return


def save_books_to_file():
    with open("books.json", "w") as file:
        json_books = []
        for book in library.books:
            json_books.append({
                "title": book.title,
                "author": book.author,
                "year": book.year,
                "review": book.review,
                "added_on": book.added_on,
                "is_read": book.is_read
            })
        json.dump(json_books, file, indent=4)

def load_books_from_file():
    try:
        with open("books.json", "r") as file:
            json_books = json.load(file)
            for data in json_books:
                book = Book(
                    data["title"],
                    data["author"],
                    data["year"],
                    data["review"],
                    data["added_on"],
                    data["is_read"]
                )
                library.add_book(book)
    except FileNotFoundError:
        pass    # No saved books yet - Let's start with a new one!


# This function displays the main menu
def show_menu():
    print(Fore.YELLOW + "\nWhat would you like to do?")
    print("1. Add a book")
    print("2. Show book list")
    print("3. Mark a book as read")
    print("4. Exit")


def add_book():
    print("📔 Let's add a new book to your list! 📔")
    
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = input("Enter the year: ")
    review = input("Write a review ")
    added_on = datetime.now().strftime("%d/%m/%Y")  # Save today's date


    new_book = Book(title, author, year, review, added_on)

    # Add the new book to the list
    library.add_book(new_book)
    save_books_to_file()
 
    print(Fore.GREEN + "\n Book added:")
    print(f"Title: {new_book.title}")
    print(f"Author: {new_book.author}")
    print(f"Year: {new_book.year}")
    print(f"Review: {new_book.review}")

def show_books():
    # If the list is empty tell the user
    if not library.books:
        print("\n Your bookshelf is waiting for its first story... grab a cup of coffee and add a book! ☕️📖")
        return
    
    # Otherwise show the books
    print("\n Welcome on your library corner!:")
    for index, book in enumerate(library.books, start=1):
        print("-----------------------------")
        print(f"Book {index}")
        print(f"Title: {book.title}")
        print(f"Author: {book.author}")
        print(f"Year: {book.year}")
        print(f"Review: {book.review}")
        print(f"📙 Read: {'Yes' if book.is_read else 'Not yet'}")

def mark_as_read():
    if not library.books:
        print("\nOps! There are no books in your Book Nook - start building your collection! 📚")
        return
    
    print("\nTime to close a chapter - which book did you just finish? 📚")
    for index, book in enumerate(library.books, start=1):
        print(f"{index}. {book.title} by {book.author}")

    try:
        choice = int(input("Enter the number of the book: "))
        if 1 <= choice <= len(library.books):
            selected_book = library.books[choice - 1]
            selected_book.is_read = True
            save_books_to_file()
            print(Fore.GREEN + f"\n📙 '{selected_book.title}' marked as read!")
        else:
            print(Fore.RED + "Ops! That wasn't a number. Please enter a valid one. ")
    except ValueError:
        print(Fore.RED + "Ops! That doesn't look like a number. Try again! ")

library = Library()
load_books_from_file()   # Save books when the app starts

while True: 
    show_menu()
    choice = input("What's your next move in the world of books? (1-3): ")

    if choice == "1":
        add_book()
    elif choice == "2":
        show_books()
    elif choice == "3":
        mark_as_read()
    elif choice == "4":
        print(Fore.CYAN + "\nThank you for using My Book Nook - come back soon for another chapter! 📖")
        break
    else:
        print(Fore.RED + "Ops! Please choose 1, 2, 3 or 4 from menu!")
