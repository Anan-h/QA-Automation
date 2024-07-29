#the library class
import json
from book import Book


class Library:

    def __init__(self, file_path):
        self.books = []
        self.file_path = file_path
        self.load_library()

    def add_book(self, book):
        self.books.append(book)
        self.save_library()

    def edit_book(self, index, title=None, author=None, year=None, genre=None):
        try:
            self.books[index].update(title, author, year, genre)
            self.save_library()
        except IndexError:
            print("Invalid book index")

    def list_books(self):
        return [book.display() for book in self.books]

    def delete_book(self, index):
        try:
            del self.books[index]
            self.save_library()
        except IndexError:
            print("Invalid book index")

    def save_library(self):
        with open(self.file_path, 'w') as file:
            json.dump([book.display() for book in self.books], file, indent=4)

    def load_library(self):
        try:
            with open(self.file_path, 'r') as file:
                book_list = json.load(file)
                for book_dict in book_list:
                    # Convert keys to lowercase
                    book_dict = {k.lower(): v for k, v in book_dict.items()}
                    self.books.append(Book(**book_dict))
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    def list_book(self, index):
        try:
            book = self.books[index]
            book.mark_as_listed()
            self.save_library()
        except IndexError:
            print("Invalid book index")
