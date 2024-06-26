#the app class
from flask import Flask, render_template, request, redirect, url_for, jsonify
from library import Library
from book import Book
class App:
    app = Flask(__name__)



    @staticmethod
    @app.route('/')
    def index():
        return render_template('index.html')

    @staticmethod
    @app.route('/books')
    def list_books():
        library = Library('library.json')
        books = library.list_books()
        return render_template('book_list.html', books=books)

    @staticmethod
    @app.route('/add', methods=['GET', 'POST'])
    def add_book():
        if request.method == 'POST':
            title = request.form['title']
            author = request.form['author']
            year = int(request.form['year'])
            genre = request.form['genre']
            new_book = Book(title, author, year, genre)  # Create a Book object
            library = Library('library.json')
            library.add_book(new_book)  # Pass the Book object to add_book method
            return redirect(url_for('list_books'))
        return render_template('add_book.html')


    @staticmethod
    @app.route('/edit/<int:index>', methods=['GET', 'POST'])
    def edit_book(index):
        library = Library('library.json')
        if request.method == 'POST':
            title = request.form['title']
            author = request.form['author']
            year = int(request.form['year'])
            genre = request.form['genre']
            library.edit_book(index, title, author, year, genre)
            return redirect(url_for('list_books'))
        book = library.books[index].display()
        return render_template('edit_book.html', index=index, book=book)


    @staticmethod
    @app.route('/delete/<int:index>', methods=['POST'])
    def delete_book(index):
        library = Library('library.json')
        library.delete_book(index)
        return redirect(url_for('list_books'))

    @staticmethod
    @app.route('/list/<int:index>', methods=['POST'])
    def list_book(index):
        library = Library('library.json')
        library.list_book(index)
        return redirect(url_for('list_books'))



