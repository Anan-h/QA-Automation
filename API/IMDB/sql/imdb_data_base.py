import sqlite3


class ImdbDataBase:
    def __init__(self):
        self.conn = sqlite3.connect('imdb.db')
        self.cur = self.conn.cursor()

    def close_connection(self):
        self.conn.close()
