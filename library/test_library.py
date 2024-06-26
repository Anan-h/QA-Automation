import json
import os
import unittest

from book import Book
from library import Library


class TestLibrary(unittest.TestCase):

    #functions from internet to create a library to use in the whole class
    def setUp(self):
        # Create a temporary file for testing
        self.test_file = 'test_library.json'
        self.library = Library(self.test_file)

    def tearDown(self):
        # Remove the temporary file after testing
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_book(self):
        book = Book('Test Title', 'Test Author', 2023, 'Test Genre')
        self.library.add_book(book)
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, 'Test Title')

    def test_edit_book(self):
        book = Book('Test Title', 'Test Author', 2023, 'Test Genre')
        self.library.add_book(book)
        self.library.edit_book(0, title='New Title')
        self.assertEqual(self.library.books[0].title, 'New Title')

    def test_delete_book(self):
        book = Book('Test Title', 'Test Author', 2023, 'Test Genre')
        self.library.add_book(book)
        self.library.delete_book(0)
        self.assertEqual(len(self.library.books), 0)

    def test_list_books(self):
        book = Book('Test Title', 'Test Author', 2023, 'Test Genre')
        self.library.add_book(book)
        books_list = self.library.list_books()
        self.assertEqual(len(books_list), 1)
        self.assertEqual(self.library.books[0].title,'Test Title')

    def test_save_library(self):
        book = Book('Test Title', 'Test Author', 2023, 'Test Genre')
        self.library.add_book(book)
        self.library.save_library()
        with open(self.test_file, 'r') as file:
            data = json.load(file)
            self.assertEqual(len(data), 1)


    def test_load_library(self):
        book_data = [{'title': 'Test Title', 'author': 'Test Author', 'year': 2023, 'genre': 'Test Genre'}]
        with open(self.test_file, 'w') as file:
            json.dump(book_data, file)
        library = Library(self.test_file)
        self.assertEqual(len(library.books), 1)
        self.assertEqual(library.books[0].title, 'Test Title')

    def test_list_book(self):
        book = Book('Test Title', 'Test Author', 2023, 'Test Genre')
        self.library.add_book(book)
        self.library.list_book(0)
        self.assertTrue(self.library.books[0].listed)