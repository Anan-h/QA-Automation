import unittest

from book import Book


class TestBook(unittest.TestCase):

    #function from the internet to build a book and use for the whole class
    def setUp(self):
        self.book = Book('Harry Potter', 'J.K. Rolling', 2000, 'Magic')

    def test_init(self):
        self.assertEqual(self.book.title, 'Harry Potter')
        self.assertEqual(self.book.author, 'J.K. Rolling')
        self.assertEqual(self.book.year, 2000)
        self.assertEqual(self.book.genre, 'Magic')
        self.assertFalse(self.book.listed)

    def test_display_book(self):
        expected_output = {
            "Title": 'Harry Potter',
            "Author": 'J.K. Rolling',
            "Year": 2000,
            "Genre": 'Magic',
            "Listed": False
        }
        self.assertEqual(self.book.display(), expected_output)

    def test_update(self):
        self.book.update(title='Anan', author='Husein', year=2024, genre='Me')
        self.assertEqual(self.book.title, 'Anan')
        self.assertEqual(self.book.author, 'Husein')
        self.assertEqual(self.book.year, 2024)
        self.assertEqual(self.book.genre, 'Me')

        # Test partial update
        self.book.update(title='Anan Husein')
        self.assertEqual(self.book.title, 'Anan Husein')
        self.assertEqual(self.book.author, 'Husein')

    def test_mark_as_listed(self):
        self.book.mark_as_listed()
        self.assertTrue(self.book.listed,)

