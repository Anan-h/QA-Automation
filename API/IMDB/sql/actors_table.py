from API.IMDB.infra.api_wrapper import APIWrapper
from API.IMDB.logic.api_born_on import APIBornOn
from API.IMDB.sql.imdb_data_base import ImdbDataBase


class ActorsTable(ImdbDataBase):
    def __init__(self):
        super().__init__()
        self.api_request = APIWrapper()
        self.request = APIBornOn(self.api_request)
        self.response = self.request.get_actors_born_on_date(3, 5)

    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS actors
        (actor_id TEXT NOT NULL,
        actor_name TEXT NOT NULL,
        movie_id TEXT NOT NULL,
        PRIMARY KEY (actor_id, movie_id),
        FOREIGN KEY (movie_id) REFERENCES movies (id))
        """)

    def insert_into_table(self):
        actors_list = self.response.data['data']['list']
        for i in range(len(actors_list)):
            actor_id = actors_list[i]['id']
            actor_name = actors_list[i]['nameText']['text']
            movies_list = actors_list[i]['nameKnownFor']['edges']
            for j in range(len(movies_list)):
                movie_id = movies_list[j]['node']['knownForTitle']['id']
                self.cur.execute("""INSERT INTO actors (actor_id, actor_name, movie_id) VALUES (?, ?, ?)
                """, (actor_id, actor_name, movie_id))
        self.conn.commit()

    def print_actors(self):
        self.cur.execute("SELECT * FROM actors")
        rows = self.cur.fetchall()
        for row in rows:
            print(row)

    def join(self):
        self.cur.execute('''
            SELECT actors.actor_name, movies.title
            FROM actors
            INNER JOIN movies ON actors.movie_id = movies.id
        ''')

        rows = self.cur.fetchall()
        # Print the results
        for row in rows:
            print(f"Actor: {row[0]}, Movie: {row[1]}")


if __name__ == "__main__":
    actor = ActorsTable()
    actor.create_table()
    actor.insert_into_table()
    actor.print_actors()
    actor.join()
