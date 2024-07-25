from API.IMDB.sql.imdb_data_base import ImdbDataBase


class CombineTable(ImdbDataBase):
    def __init__(self):
        super().__init__()




if __name__ == "__main__":
    com = CombineTable()
    com.join()
