# the book class
class Book:
    def __init__(self, title, author, year, genre,listed=False):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.listed = listed

    def display(self):

        if self.listed == False:
            listed_str="[ ]"
        else:
            listed_str="[v]"

        return {
            "Title": self.title,
            "Author": self.author,
            "Year": self.year,
            "Genre": self.genre,
            "Listed": self.listed
        }

    def update(self, title=None, author=None, year=None, genre=None):
        if title:
            self.title = title
        if author:
            self.author = author
        if year:
            self.year = year
        if genre:
            self.genre = genre

    def mark_as_listed(self):
        if self.listed:
            print("This book is already listed!")
        else:
            self.listed = True
