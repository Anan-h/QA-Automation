from API.IMDB.infra.api_wrapper import APIWrapper
from API.IMDB.logic.api_popular_movies import APIPopularMovies
from API.IMDB.sql.imdb_data_base import ImdbDataBase


class PopularMoviesTable(ImdbDataBase):

    def __init__(self):
        super().__init__()
        self.api_request = APIWrapper()
        self.request = APIPopularMovies(self.api_request)
        self.response = self.request.get_all_popular_movies()

    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS movies
        (id TEXT PRIMARY KEY,
        title TEXT NOT NULL)
        """)

    def insert_into_table(self):
        movies_list = self.response.data['data']['list']
        for i in range(len(movies_list)):
            movie_id = movies_list[i]['title']['id']
            movie_name = movies_list[i]['title']['originalTitleText']['text']
            self.cur.execute("""INSERT INTO movies (id, title) VALUES (?, ?)
           """, (movie_id, movie_name))
        self.conn.commit()

    def print_movies(self):
        self.cur.execute("SELECT * FROM movies")
        rows = self.cur.fetchall()
        for row in rows:
            print(row)


if __name__ == "__main__":
    movie = PopularMoviesTable()
    movie.create_table()
    movie.insert_into_table()
    movie.print_movies()